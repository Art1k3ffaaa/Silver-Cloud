"""
Скрипт восстановления БД из backup при старте на Railway
При первом запуске загружает telegram_bot.db с GitHub
"""
import os
import urllib.request
import shutil
from pathlib import Path

# БД должна быть на Volume в /app/data
if os.path.exists("/app/data"):
    os.makedirs("/app/data", exist_ok=True)
    DB_PATH = "/app/data/telegram_bot.db"
else:
    DB_PATH = "telegram_bot.db"

GITHUB_RAW_URL = "https://raw.githubusercontent.com/Art1k3ffaaa/Silver-Cloud/main/telegram_bot.db"
GITHUB_BACKUP_URL = "https://raw.githubusercontent.com/Art1k3ffaaa/Silver-Cloud/main/telegram_bot.db.backup"
LOCAL_BACKUP = "telegram_bot.db"  # локальная копия для разработки


def restore_database():
    """Восстановить БД из backup если её нет на сервере"""
    
    # Проверяем есть ли БД на Railway Volume
    db_exists = os.path.exists(DB_PATH) and os.path.getsize(DB_PATH) > 1000  # Более 1KB
    
    if db_exists:
        print(f"✅ БД найдена в {DB_PATH}, восстановление не требуется")
        return True
    
    print(f"⚠️  БД не найдена или пуста в {DB_PATH}, восстанавливаем...")
    
    # Сначала пробуем использовать локальную копию
    if os.path.exists(LOCAL_BACKUP) and os.path.getsize(LOCAL_BACKUP) > 1000:
        try:
            print(f"📋 Копируем локальный backup: {LOCAL_BACKUP} → {DB_PATH}")
            shutil.copy2(LOCAL_BACKUP, DB_PATH)
            print("✅ БД успешно восстановлена из локального backup")
            return True
        except Exception as e:
            print(f"❌ Ошибка при копировании locального backup: {e}")
    
    # Пробуем скачать backup с GitHub
    try:
        print(f"📥 Скачиваем БД backup с GitHub...")
        urllib.request.urlretrieve(GITHUB_BACKUP_URL, DB_PATH)
        
        # Проверяем что файл скачался корректно
        if os.path.getsize(DB_PATH) > 1000:
            print(f"✅ БД успешно скачана из backup и восстановлена в {DB_PATH}")
            return True
        else:
            print("⚠️ Backup файл слишком маленький, он может быть пуст")
            
    except Exception as e:
        print(f"❌ Ошибка при скачивании БД backup с GitHub: {e}")
    
    # Если backup не сработал, пробуем основную БД
    try:
        print(f"📥 Пробуем скачать основную БД...")
        urllib.request.urlretrieve(GITHUB_RAW_URL, DB_PATH)
        
        # Проверяем что файл скачался корректно
        if os.path.getsize(DB_PATH) > 1000:
            print(f"✅ БД успешно скачана и восстановлена в {DB_PATH}")
            return True
        else:
            print("❌ Скачанный файл пуст")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка при скачивании БД с GitHub: {e}")
        print("⚠️  БД будет создана заново при первом запуске бота")
        return False


if __name__ == "__main__":
    restore_database()

