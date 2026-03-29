"""
Синхронный модуль для работы с БД основного бота
Использует SQLite для сохранения заказов и статистики
"""
import sqlite3
import os
from datetime import datetime
from typing import List, Optional, Dict, Tuple

# На Railway используем /app/data для Volume, на локальной машине текущая директория
if os.path.exists("/app/data"):
    os.makedirs("/app/data", exist_ok=True)
    DB_PATH = "/app/data/telegram_bot.db"
else:
    DB_PATH = os.path.join(os.path.dirname(__file__), "telegram_bot.db")


class Database:
    """Класс для работы с БД"""
    
    def __init__(self, db_path: str = DB_PATH):
        self.db_path = db_path
        self.init_db()
    
    def get_connection(self):
        """Получить соединение с БД"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_db(self):
        """Инициализация БД и создание таблиц"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE NOT NULL,
                username TEXT,
                first_name TEXT,
                registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                product TEXT NOT NULL,
                product_id TEXT,
                flavors TEXT,
                place TEXT,
                quantity INTEGER DEFAULT 1,
                total_price REAL DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'pending',
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)
        
        cursor.execute("PRAGMA table_info(orders)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'total_price' not in columns:
            cursor.execute("ALTER TABLE orders ADD COLUMN total_price REAL DEFAULT 0")
        
        if 'product_id' not in columns:
            cursor.execute("ALTER TABLE orders ADD COLUMN product_id TEXT")
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_stats (
                user_id INTEGER PRIMARY KEY UNIQUE NOT NULL,
                completed_deals INTEGER DEFAULT 0,
                pending_orders INTEGER DEFAULT 0,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS flavor_stock (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id TEXT NOT NULL,
                flavor_name TEXT NOT NULL,
                quantity INTEGER DEFAULT 0,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(product_id, flavor_name)
            )
        """)
        
        conn.commit()
        conn.close()
    
    def add_user(self, user_id: int, username: Optional[str] = None, 
                 first_name: Optional[str] = None) -> bool:
        """Добавить нового пользователя"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT OR IGNORE INTO users (user_id, username, first_name)
                VALUES (?, ?, ?)
                """,
                (user_id, username, first_name)
            )
            cursor.execute(
                "INSERT OR IGNORE INTO user_stats (user_id) VALUES (?)",
                (user_id,)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Ошибка при добавлении пользователя: {e}")
            return False
    
    def get_user(self, user_id: int) -> Optional[Dict]:
        """Получить пользователя по ID"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, user_id, username, first_name, registered_at FROM users WHERE user_id = ?",
                (user_id,)
            )
            row = cursor.fetchone()
            conn.close()
            if row:
                return dict(row)
            return None
        except Exception as e:
            print(f"Ошибка при получении пользователя: {e}")
            return None
    
    def add_order(self, user_id: int, product: str, flavors: str, 
                  place: str, quantity: int = 1, total_price: float = 0, product_id: str = None) -> Optional[int]:
        """Добавить новый заказ, возвращает order_id"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            self.add_user(user_id)
            
            cursor.execute(
                """
                INSERT INTO orders (user_id, product, product_id, flavors, place, quantity, total_price, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, 'pending')
                """,
                (user_id, product, product_id, flavors, place, quantity, total_price)
            )
            conn.commit()
            order_id = cursor.lastrowid
            conn.close()
            return order_id
        except Exception as e:
            print(f"Ошибка при добавлении заказа: {e}")
            return None
    
    def get_all_orders(self) -> List[Dict]:
        """Получить все заказы"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, user_id, product, flavors, place, quantity, total_price, created_at, status 
                FROM orders 
                ORDER BY created_at DESC
                """
            )
            rows = cursor.fetchall()
            conn.close()
            return [dict(row) for row in rows]
        except Exception as e:
            print(f"Ошибка при получении заказов: {e}")
            return []
    
    def get_user_orders(self, user_id: int) -> List[Dict]:
        """Получить заказы пользователя"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, user_id, product, flavors, place, quantity, total_price, created_at, status 
                FROM orders 
                WHERE user_id = ? 
                ORDER BY created_at DESC
                """,
                (user_id,)
            )
            rows = cursor.fetchall()
            conn.close()
            return [dict(row) for row in rows]
        except Exception as e:
            print(f"Ошибка при получении заказов пользователя: {e}")
            return []
    
    def update_order_status(self, order_id: int, status: str) -> bool:
        """Обновить статус заказа"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE orders SET status = ? WHERE id = ?",
                (status, order_id)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Ошибка при обновлении статуса: {e}")
            return False
    
    def get_user_stats(self, user_id: int) -> Optional[Dict]:
        """Получить статистику пользователя"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT user_id, completed_deals, pending_orders, updated_at FROM user_stats WHERE user_id = ?",
                (user_id,)
            )
            row = cursor.fetchone()
            conn.close()
            if row:
                return dict(row)
            return None
        except Exception as e:
            print(f"Ошибка при получении статистики: {e}")
            return None
    
    def increment_completed_deals(self, user_id: int) -> bool:
        """Увеличить счетчик осуществленных сделок"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute(
                "INSERT OR IGNORE INTO user_stats (user_id) VALUES (?)",
                (user_id,)
            )
            
            cursor.execute(
                """
                UPDATE user_stats 
                SET completed_deals = completed_deals + 1, updated_at = CURRENT_TIMESTAMP
                WHERE user_id = ?
                """,
                (user_id,)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Ошибка при увеличении счетчика: {e}")
            return False
    
    def get_completed_deals_count(self, user_id: int) -> int:
        """Получить количество осуществленных сделок"""
        stats = self.get_user_stats(user_id)
        return stats['completed_deals'] if stats else 0
    
    def get_pending_orders_count(self, user_id: int) -> int:
        """Получить количество ожидающих заказов"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT COUNT(*) FROM orders WHERE user_id = ? AND status = 'pending'",
                (user_id,)
            )
            count = cursor.fetchone()[0]
            conn.close()
            return count
        except Exception as e:
            print(f"Ошибка при получении количества ожидающих заказов: {e}")
            return 0
    
    def get_order(self, order_id: int) -> Optional[Dict]:
        """Получить информацию о заказе"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, user_id, product, flavors, place, quantity, total_price, created_at, status 
                FROM orders 
                WHERE id = ?
                """,
                (order_id,)
            )
            row = cursor.fetchone()
            conn.close()
            if row:
                return dict(row)
            return None
        except Exception as e:
            print(f"Ошибка при получении заказа: {e}")
            return None
    
    def get_pending_orders(self) -> List[Dict]:
        """Получить все ожидающие заказы (статус 'pending')"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, user_id, product, flavors, place, quantity, total_price, created_at, status 
                FROM orders 
                WHERE status = 'pending'
                ORDER BY created_at DESC
                """
            )
            rows = cursor.fetchall()
            conn.close()
            return [dict(row) for row in rows]
        except Exception as e:
            print(f"Ошибка при получении ожидающих заказов: {e}")
            return []
    
    def get_confirmed_orders(self) -> List[Dict]:
        """Получить все подтвержденные заказы (статус 'confirmed', 'completed')"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, user_id, product, flavors, place, quantity, total_price, created_at, status 
                FROM orders 
                WHERE status IN ('confirmed', 'completed')
                ORDER BY created_at DESC
                """
            )
            rows = cursor.fetchall()
            conn.close()
            return [dict(row) for row in rows]
        except Exception as e:
            print(f"Ошибка при получении подтвержденных заказов: {e}")
            return []
    
    def get_order_with_user_info(self, order_id: int) -> Optional[Dict]:
        """Получить информацию о заказе вместе с данными пользователя"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT o.id, o.user_id, o.product, o.flavors, o.place, o.quantity, o.total_price, o.created_at, o.status,
                       u.username, u.first_name
                FROM orders o
                LEFT JOIN users u ON o.user_id = u.user_id
                WHERE o.id = ?
                """,
                (order_id,)
            )
            row = cursor.fetchone()
            conn.close()
            if row:
                return dict(row)
            return None
        except Exception as e:
            print(f"Ошибка при получении заказа с информацией пользователя: {e}")
            return None
    
    def get_customers_with_confirmed_orders(self) -> List[Dict]:
        """Получить список уникальных пользователей с подтвержденными заказами"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT DISTINCT 
                    u.user_id, 
                    u.username, 
                    u.first_name,
                    COUNT(o.id) as confirmed_count
                FROM users u
                LEFT JOIN orders o ON u.user_id = o.user_id AND o.status IN ('confirmed', 'completed')
                WHERE EXISTS (
                    SELECT 1 FROM orders WHERE user_id = u.user_id AND status IN ('confirmed', 'completed')
                )
                GROUP BY u.user_id
                ORDER BY confirmed_count DESC
                """
            )
            rows = cursor.fetchall()
            conn.close()
            return [dict(row) for row in rows]
        except Exception as e:
            print(f"Ошибка при получении пользователей с подтвержденными заказами: {e}")
            return []
    
    def get_user_confirmed_orders(self, user_id: int) -> List[Dict]:
        """Получить все подтвержденные заказы конкретного пользователя"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT id, user_id, product, flavors, place, quantity, total_price, created_at, status 
                FROM orders 
                WHERE user_id = ? AND status IN ('confirmed', 'completed')
                ORDER BY created_at DESC
                """,
                (user_id,)
            )
            rows = cursor.fetchall()
            conn.close()
            return [dict(row) for row in rows]
        except Exception as e:
            print(f"Ошибка при получении заказов пользователя: {e}")
            return []
    
    def delete_user_with_orders(self, user_id: int) -> bool:
        """Удалить пользователя и все его заказы из БД"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute("DELETE FROM orders WHERE user_id = ?", (user_id,))
            cursor.execute("DELETE FROM user_stats WHERE user_id = ?", (user_id,))
            cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Ошибка при удалении пользователя: {e}")
            return False

    def get_total_users_count(self) -> int:
        """Получить общее количество пользователей (за всё время)"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM users")
            count = cursor.fetchone()[0]
            conn.close()
            return count
        except Exception as e:
            print(f"Ошибка при получении количества пользователей: {e}")
            return 0
    
    def get_total_completed_orders_count(self) -> int:
        """Получить общее количество выполненных заказов (за всё время)"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT COUNT(*) FROM orders WHERE status IN ('confirmed', 'completed')"
            )
            count = cursor.fetchone()[0]
            conn.close()
            return count
        except Exception as e:
            print(f"Ошибка при получении количества выполненных заказов: {e}")
            return 0
    
    def get_total_earnings(self) -> float:
        """Получить общий заработок (сумма всех цен выполненных заказов за всё время)"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT SUM(total_price) FROM orders WHERE status IN ('confirmed', 'completed')"
            )
            result = cursor.fetchone()[0]
            conn.close()
            return result if result is not None else 0.0
        except Exception as e:
            print(f"Ошибка при получении общего заработка: {e}")
            return 0.0
    
    def get_flavor_stock(self, product_id: str, flavor_name: str) -> int:
        """Получить остаток конкретного вкуса товара"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT quantity FROM flavor_stock WHERE product_id = ? AND flavor_name = ?",
                (product_id, flavor_name)
            )
            row = cursor.fetchone()
            conn.close()
            return row[0] if row else 0
        except Exception as e:
            print(f"Ошибка при получении остатка вкуса: {e}")
            return 0
    
    def set_flavor_stock(self, product_id: str, flavor_name: str, quantity: int) -> bool:
        """Установить остаток конкретного вкуса товара"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT OR REPLACE INTO flavor_stock (product_id, flavor_name, quantity, updated_at)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
                """,
                (product_id, flavor_name, quantity)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Ошибка при установке остатка вкуса: {e}")
            return False
    
    def decrease_flavor_stock(self, product_id: str, flavor_name: str, quantity: int) -> bool:
        """Уменьшить остаток конкретного вкуса товара"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            current_stock = self.get_flavor_stock(product_id, flavor_name)
            new_stock = max(0, current_stock - quantity)
            
            cursor.execute(
                """
                INSERT OR REPLACE INTO flavor_stock (product_id, flavor_name, quantity, updated_at)
                VALUES (?, ?, ?, CURRENT_TIMESTAMP)
                """,
                (product_id, flavor_name, new_stock)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Ошибка при уменьшении остатка вкуса: {e}")
            return False
    
    def get_product_flavors_stock(self, product_id: str) -> Dict[str, int]:
        """Получить остатки всех вкусов для товара"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT flavor_name, quantity FROM flavor_stock WHERE product_id = ?",
                (product_id,)
            )
            rows = cursor.fetchall()
            conn.close()
            return {row[0]: row[1] for row in rows}
        except Exception as e:
            print(f"Ошибка при получении остатков вкусов: {e}")
            return {}


db = Database()
