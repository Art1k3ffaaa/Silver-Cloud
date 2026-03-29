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
LOCAL_BACKUP = "telegram_bot.db"  # локальная копия для разработки


def restore_database():
    """Восстановить БД из backup если её нет на сервере"""
    
    # Проверяем есть ли БД на Railway Volume
    db_exists = os.path.exists(DB_PATH) and os.path.getsize(DB_PATH) > 0
    
    if db_exists:
        print(f"✅ БД найдена в {DB_PATH}, восстановление не требуется")
        return True
    
    print(f"⚠️  БД не найдена в {DB_PATH}, восстанавливаем...")
    
    # Сначала пробуем использовать локальную копию
    if os.path.exists(LOCAL_BACKUP) and os.path.getsize(LOCAL_BACKUP) > 0:
        try:
            print(f"📋 Копируем локальный backup: {LOCAL_BACKUP} → {DB_PATH}")
            shutil.copy2(LOCAL_BACKUP, DB_PATH)
            print("✅ БД успешно восстановлена из локального backup")
            return True
        except Exception as e:
            print(f"❌ Ошибка при копировании locального backup: {e}")
    
    # Если локального нет, пробуем скачать с GitHub
    try:
        print(f"📥 Скачиваем БД с GitHub...")
        urllib.request.urlretrieve(GITHUB_RAW_URL, DB_PATH)
        
        # Проверяем что файл скачался корректно
        if os.path.getsize(DB_PATH) > 0:
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
