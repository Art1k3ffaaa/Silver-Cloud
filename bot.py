import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

try:
    from restore_db import restore_database
    restore_database()
except Exception as e:
    print(f"⚠️ Ошибка восстановления БД: {e}")

from db_main_bot import db
# ==================== НАСТРОЙКИ ====================
BOT_TOKEN = os.getenv('BOT_TOKEN') or '8316568148:AAHAeGcxY9ttW3MpjVMZP8URh__2YkJI87M'

# ==================== ЯЗЫКИ ====================
LANGUAGES = {
    "ru": {
        "language_select": "🌍 Выберите язык / Select language / Valige keel:",
        "main_menu": "👋 Добро пожаловать!\n\nВыберите, что вас интересует:",
        "check_stock": "📦 Наличие товара",
        "order": "🛒 Оформить заказ",
        "bulk_order": "📦 Оптовые заказы",
        "bulk_order_response": "Обратитесь к @Sellamng",
        "managers": "👥 Менеджеры",
        "managers_text": "👥 Наши менеджеры:\n\n{contact}\n\nНапишите нам для оформления заказа или уточнения информации",
        "order_choose_flavor": "Выберите вкус для {product}:",
        "order_flavor_selected": "Выбранные вкусы: {flavors}.",
        "order_choose_quantity": "Укажите количество для {flavor}:",
        "order_choose_place": "Теперь выберите место доставки:",
        "order_place_button": "Перейти к выбору места",
        "order_place_mustamae": "Мустамяе [FREE]",
        "order_place_centre": "Центр [FREE]",
        "order_place_lasnamae": "Ласнамяе [FREE]",
        "order_place_kopli": "Копли [+4€]",
        "order_place_oismae": "Ыйсмяе [+3€]",
        "order_place_dpd": "DPD [+4€]",
        "order_select_taste_first": "Сначала выберите вкус",
        "choose_flavor": "Выберите вкус:",
        "stock_snus": "Снюс",
        "stock_ecigs": "Э. сигареты",
        "stock_liquids": "Жижи",
        "coming_soon": " (скоро)",
        "coming_soon_text": "Скоро...",
        "order_not_available": "Товар недоступен",
        "order_quantity_unit": "шт.",
        "order_accept_text": "Заказ принят:\nТовар: {product}\nВкусы:\n{flavors}\nМесто: {place}\n\nИтого:\nТовар: {product_price}€\nДоставка: {delivery_price}\nПолная цена: {total_price}€",
        "order_contact_text": "Свяжитесь в Telegram: {contact}",
        "order_contact_mustamae": "@MayBeHim",
        "order_contact_centre": "@V1ne233 и @MayBeHim",
        "order_contact_lasnamae": "@V1ne233",
        "order_contact_kopli": "@MayBeHim",
        "order_contact_oismae": "@MayBeHim",
        "order_contact_dpd": "@V1ne233 и @MayBeHim",
        "category_prefix": "Категория:",
        "choose_item": "Выберите товар:",
        "flavors": {
            "Apple Juice": "🍎 Apple Juice",
            "Banana Hit": "🍌 Banana Hit",
            "Black Currant": "🖤 Black Currant",
            "Blueberry": "🫐 Blueberry",
            "Cherry": "🍒 Cherry",
            "Cola": "🥤 Cola",
            "Cold Dry": "❄️ Cold Dry",
            "Double Fresh": "🌬️ Double Fresh",
            "Forest Berries": "🌲 Forest Berries",
            "Grape": "🍇 Grape",
            "Ice Spearmint": "🧊 Ice Spearmint",
            "Peach": "🍑 Peach",
            "Pineapple": "🍍 Pineapple",
            "Watermelon": "🍉 Watermelon",
            "CLASSIC": "🎯 Classic",
            "EUCALYPTUS": "🌿 Eucalyptus",
            "FRUIT COCKTAIL": "🍹 Fruit Cocktail",
            "MENTHOL": "❄️ Menthol",
            "WINTERGREEN": "🌲 Wintergreen",
            "LAVAFIRE": "🌋🔥 LAVAFIRE",
            "BLUEBERRY ICE": "🫐❄️ BLUEBERRY ICE",
            "BERRY PEACH": "🍓🍑 BERRY PEACH",
            "GRAPE ICE": "🍇❄️ GRAPE ICE",
            "BLUE RASPBERRY": "💙🍓 BLUE RASPBERRY",
            "BERRY": "🫐 BERRY",
            "BLUEBERRY WATERMELON": "🫐🍉 BLUEBERRY WATERMELON",
            "DRAGON FRUIT BANANA CHERRY": "🐉🍌 DRAGON FRUIT BANANA CHERRY",
            "PINEAPPLE PASSION FRUIT LIME": "🍍🥒 PINEAPPLE PASSION FRUIT LIME",
            "CHERRY COLA": "🍒🥤 CHERRY COLA",
            "POMEGRANATE LEMONADE": "🍒🍋 POMEGRANATE LEMONADE",
            "PERFUME LEMON": "🍋✨ PERFUME LEMON",
            "PEACH MANGO WATERMELON": "🍑🥭 PEACH MANGO WATERMELON",
            "STRAWBERRY WATERMELON": "🍓🍉 STRAWBERRY WATERMELON",
            "BLUE RAZZ LEMON": "🫐🍋 BLUE RAZZ LEMON",
            "STRAWBERRY ICE CREAM": "🍓🍦 STRAWBERRY ICE CREAM",
            "WATERMELON BUBBLE GUM": "🍉🎀 WATERMELON BUBBLE GUM",
            "KIWI PASSION FRUIT GUAVA": "🥝🍐 KIWI PASSION FRUIT GUAVA",
            "MIXED BERRIES": "🫐🍓 MIXED BERRIES",
            "PURPLE CANDY": "💜🍬 PURPLE CANDY",
            "PINEAPPLE COLADA": "🍍🥥 PINEAPPLE COLADA",
            "BLACKBERRY LEMON": "🖤🍋 BLACKBERRY LEMON",
            "STRAWBERRY RASPBERRY CHERRY ICE": "🍓🧊 STRAWBERRY RASPBERRY CHERRY ICE",
            "SOUR WATERMELON GUMMY": "🍉🍬 SOUR WATERMELON GUMMY",
            "PINK LEMONADE": "🍋💕 PINK LEMONADE",
            "GRAPE CHERRY": "🍇🍒 GRAPE CHERRY",
            "PINK GRAPEFRUIT": "🍑💕 PINK GRAPEFRUIT",
            "BLUEBERRY CHERRY CRANBERRY": "🫐🍒 BLUEBERRY CHERRY CRANBERRY",
            "CHERRY LIME RASPBERRY": "🍒🟢 CHERRY LIME RASPBERRY",
            "BLUEBERRY SOUR RASPBERRY": "🫐🍓 BLUEBERRY SOUR RASPBERRY",
            "LEMON LIME": "🍋🟢 LEMON LIME",
            "BLUEBERRY LEMONADE": "🫐🍋 BLUEBERRY LEMONADE",
            "FIZZY CHERRY": "🍒✨ FIZZY CHERRY",
            "MR BLUE": "💙❄️ MR BLUE",
            "BLACK ICE": "🖤❄️ BLACK ICE",
            "WATERMELON ICE": "🍉❄️ WATERMELON ICE",
            "BLUEBERRY RASPBERRY": "🫐🍓 BLUEBERRY RASPBERRY",
            "STRAWBERRY BANANA": "🍓🍌 STRAWBERRY BANANA",
            "SKY MINT": "🌌🍃 SKY MINT"
        },
        "catalog": "📦 Каталог товаров:\n\nВыберите товар, чтобы увидеть вкусы и описание:",
        "category_snus": "Снюс",
        "category_ecigs": "Э. сигареты",
        "category_liquids": "Жижи",
        "order_text": "✅ Вы хотите заказать: {product}\n\nДля оформления заказа напишите нам:\n👤 {contact}\n\nУкажите:\n• Название товара\n• Выбранный вкус\n• Количество\n• Адрес доставки",
        "product_not_found": "Товар не найден",
        "back_catalog": "◀️ Назад к каталогу",
        "back_menu": "◀️ Назад в меню",
        "order_button": "🛒 Заказать",
        "back_product": "◀️ Назад к товару",
        "change_language": "🌍 Изменить язык",
        "in_stock": "✅ В наличии",
        "out_of_stock": "❌ Нет в наличии",
        "clear_history": "🔄 История очищена. Введите /start для начала заново.",
        "personal_cabinet": "👤 Личный кабинет",
        "personal_cabinet_title": "👤 Ваш личный кабинет",
        "orders_completed": "✅ Осуществленных сделок: {count}",
        "orders_sum": "💰 Сумма заказов: {sum}€",
        "no_orders": "У вас еще нет осуществленных сделок",
        "referral_system": "🎁 Реферальная система",
        "referral_title": "🎁 Реферальная система",
        "referral_text": "При приглашении 20 людей вы получаете любой товар на выбор абсолютно бесплатно.\n\nЧтобы получить личную пригласительную ссылку напишите @Sellamng",
        "insufficient_stock_single": "❌ К сожалению, этого вкуса осталось только {stock} шт.",
        "insufficient_stock_multiple": "❌ {flavor}: осталось только {stock} шт, а вы выбрали {qty} шт.",
        "continue_shopping": "➕ Добавить другой товар",
        "finish_order": "✅ Завершить заказ",
        "cart_title": "🛒 Ваша корзина",
        "cart_summary": "Выбранные товары:",
        "order_summary_text": "Заказ готов к оформлению!",
        "total_items": "Всего товаров: {count}",
        "total_sum": "Сумма: {sum}€",
    },
    "en": {
        "language_select": "🌍 Select language / Выберите язык / Valige keel:",
        "main_menu": "👋 Welcome!\n\nChoose what interests you:",
        "check_stock": "📦 Stock status",
        "order": "🛒 Place an order",
        "bulk_order": "📦 Bulk orders",
        "bulk_order_response": "Contact @Sellamng",
        "managers": "👥 Managers",
        "managers_text": "👥 Our managers:\n\n{contact}\n\nContact us to place an order or get more information",
        "order_choose_flavor": "Choose flavor for {product}:",
        "order_flavor_selected": "Selected flavors: {flavors}.",
        "order_choose_quantity": "Select quantity for {flavor}:",
        "order_choose_place": "Now select delivery location:",
        "order_place_button": "Go to location selection",
        "order_place_mustamae": "Mustamäe [FREE]",
        "order_place_centre": "City centre [FREE]",
        "order_place_lasnamae": "Lasnamäe [FREE]",
        "order_place_kopli": "Kopli [+4€]",
        "order_place_oismae": "Õismäe [+3€]",
        "order_place_dpd": "DPD [+4€]",
        "order_select_taste_first": "Choose flavor first",
        "choose_flavor": "Choose flavor:",
        "stock_snus": "Snus",
        "stock_ecigs": "E-cigarettes",
        "stock_liquids": "Liquids",
        "coming_soon": " (coming soon)",
        "coming_soon_text": "Soon...",
        "order_not_available": "Product unavailable",
        "order_quantity_unit": "pcs",
        "order_accept_text": "Order accepted:\nProduct: {product}\nFlavors:\n{flavors}\nPlace: {place}\n\nTotal:\nProduct: {product_price}€\nDelivery: {delivery_price}\nFull price: {total_price}€",
        "order_contact_text": "Contact on Telegram: {contact}",
        "order_contact_mustamae": "@MayBeHim",
        "order_contact_centre": "@V1ne233 and @MayBeHim",
        "order_contact_lasnamae": "@V1ne233",
        "order_contact_kopli": "@MayBeHim",
        "order_contact_oismae": "@MayBeHim",
        "order_contact_dpd": "@V1ne233 and @MayBeHim",
        "category_prefix": "Category:",
        "choose_item": "Choose product:",
        "flavors": {
            "Apple Juice": "🍎 Apple Juice",
            "Banana Hit": "🍌 Banana Hit",
            "Black Currant": "🖤 Black Currant",
            "Blueberry": "🫐 Blueberry",
            "Cherry": "🍒 Cherry",
            "Cola": "🥤 Cola",
            "Cold Dry": "❄️ Cold Dry",
            "Double Fresh": "🌬️ Double Fresh",
            "Forest Berries": "🌲 Forest Berries",
            "Grape": "🍇 Grape",
            "Ice Spearmint": "🧊 Ice Spearmint",
            "Peach": "🍑 Peach",
            "Pineapple": "🍍 Pineapple",
            "Watermelon": "🍉 Watermelon",
            "CLASSIC": "🎯 Classic",
            "EUCALYPTUS": "🌿 Eucalyptus",
            "FRUIT COCKTAIL": "🍹 Fruit Cocktail",
            "MENTHOL": "❄️ Menthol",
            "WINTERGREEN": "🌲 Wintergreen",
            "LAVAFIRE": "🌋🔥 LAVAFIRE",
            "BLUEBERRY ICE": "🫐❄️ BLUEBERRY ICE",
            "BERRY PEACH": "🍓🍑 BERRY PEACH",
            "GRAPE ICE": "🍇❄️ GRAPE ICE",
            "BLUE RASPBERRY": "💙🍓 BLUE RASPBERRY",
            "BERRY": "🫐 BERRY",
            "BLUEBERRY WATERMELON": "🫐🍉 BLUEBERRY WATERMELON",
            "DRAGON FRUIT BANANA CHERRY": "🐉🍌 DRAGON FRUIT BANANA CHERRY",
            "PINEAPPLE PASSION FRUIT LIME": "🍍🥒 PINEAPPLE PASSION FRUIT LIME",
            "CHERRY COLA": "🍒🥤 CHERRY COLA",
            "POMEGRANATE LEMONADE": "🍒🍋 POMEGRANATE LEMONADE",
            "PERFUME LEMON": "🍋✨ PERFUME LEMON",
            "PEACH MANGO WATERMELON": "🍑🥭 PEACH MANGO WATERMELON",
            "STRAWBERRY WATERMELON": "🍓🍉 STRAWBERRY WATERMELON",
            "BLUE RAZZ LEMON": "🫐🍋 BLUE RAZZ LEMON",
            "STRAWBERRY ICE CREAM": "🍓🍦 STRAWBERRY ICE CREAM",
            "WATERMELON BUBBLE GUM": "🍉🎀 WATERMELON BUBBLE GUM",
            "KIWI PASSION FRUIT GUAVA": "🥝🍐 KIWI PASSION FRUIT GUAVA",
            "MIXED BERRIES": "🫐🍓 MIXED BERRIES",
            "PURPLE CANDY": "💜🍬 PURPLE CANDY",
            "PINEAPPLE COLADA": "🍍🥥 PINEAPPLE COLADA",
            "BLACKBERRY LEMON": "🖤🍋 BLACKBERRY LEMON",
            "STRAWBERRY RASPBERRY CHERRY ICE": "🍓🧊 STRAWBERRY RASPBERRY CHERRY ICE",
            "SOUR WATERMELON GUMMY": "🍉🍬 SOUR WATERMELON GUMMY",
            "PINK LEMONADE": "🍋💕 PINK LEMONADE",
            "GRAPE CHERRY": "🍇🍒 GRAPE CHERRY",
            "PINK GRAPEFRUIT": "🍑💕 PINK GRAPEFRUIT",
            "BLUEBERRY CHERRY CRANBERRY": "🫐🍒 BLUEBERRY CHERRY CRANBERRY",
            "CHERRY LIME RASPBERRY": "🍒🟢 CHERRY LIME RASPBERRY",
            "BLUEBERRY SOUR RASPBERRY": "🫐🍓 BLUEBERRY SOUR RASPBERRY",
            "LEMON LIME": "🍋🟢 LEMON LIME",
            "BLUEBERRY LEMONADE": "🫐🍋 BLUEBERRY LEMONADE",
            "FIZZY CHERRY": "🍒✨ FIZZY CHERRY",
            "MR BLUE": "💙❄️ MR BLUE",
            "BLACK ICE": "🖤❄️ BLACK ICE",
            "WATERMELON ICE": "🍉❄️ WATERMELON ICE",
            "BLUEBERRY RASPBERRY": "🫐🍓 BLUEBERRY RASPBERRY",
            "STRAWBERRY BANANA": "🍓🍌 STRAWBERRY BANANA",
            "SKY MINT": "🌌🍃 SKY MINT"
        },
        "catalog": "📦 Product Catalog:\n\nSelect a product to see flavors and description:",
        "category_snus": "Snus",
        "category_ecigs": "puffs",
        "category_liquids": "Liquids",
        "order_text": "✅ You want to order: {product}\n\nTo complete your order, contact us:\n👤 {contact}\n\nPlease specify:\n• Product name\n• Selected flavor\n• Quantity\n• Delivery address",
        "product_not_found": "Product not found",
        "back_catalog": "◀️ Back to catalog",
        "back_menu": "◀️ Back to menu",
        "order_button": "🛒 Order",
        "back_product": "◀️ Back to product",
        "change_language": "🌍 Change language",
        "in_stock": "✅ In stock",
        "out_of_stock": "❌ Out of stock",
        "clear_history": "🔄 History cleared. Enter /start to begin again.",
        "personal_cabinet": "👤 Personal Cabinet",
        "personal_cabinet_title": "👤 Your Personal Cabinet",
        "orders_completed": "✅ Completed transactions: {count}",
        "orders_sum": "💰 Total orders: {sum}€",
        "no_orders": "You have no completed transactions yet",
        "referral_system": "🎁 Referral System",
        "referral_title": "🎁 Referral System",
        "referral_text": "Invite 20 people and get any product of your choice absolutely free.\n\nTo get your personal referral link, contact @Sellamng",
        "insufficient_stock_single": "❌ Unfortunately, only {stock} pcs of this flavor are left.",
        "insufficient_stock_multiple": "❌ {flavor}: only {stock} pcs available, but you selected {qty} pcs.",
        "continue_shopping": "➕ Add another product",
        "finish_order": "✅ Finish order",
        "cart_title": "🛒 Your cart",
        "cart_summary": "Selected products:",
        "order_summary_text": "Order ready for checkout!",
        "total_items": "Total items: {count}",
        "total_sum": "Total: {sum}€",
    },
    "et": {
        "language_select": "🌍 Valige keel / Select language / Выберите язык:",
        "main_menu": "👋 Tere tulemast!\n\nValige, mis teid huvitab:",
        "check_stock": "📦 Toote olemasolu",
        "order": "🛒 Telli",
        "bulk_order": "📦 Suured tellimused",
        "bulk_order_response": "Võtke ühendust @Sellamng",
        "managers": "👥 Juhid",
        "managers_text": "👥 Meie juhid:\n\n{contact}\n\nVõtke meiega ühendust tellimuse esitamiseks või informatsiooni saamiseks",
        "order_choose_flavor": "Valige maitse jaoks {product}:",
        "order_flavor_selected": "Valitud maitsed: {flavors}.",
        "order_choose_quantity": "Valige kogus jaoks {flavor}:",
        "order_choose_place": "Nüüd valige tarnekoht:",
        "order_place_button": "Mine asukoha valikule",
        "order_place_mustamae": "Mustamäe [FREE]",
        "order_place_centre": "Kesklinn [FREE]",
        "order_place_lasnamae": "Lasnamäe [FREE]",
        "order_place_kopli": "Kopli [+4€]",
        "order_place_oismae": "Õismäe [+3€]",
        "order_place_dpd": "DPD [+4€]",
        "order_select_taste_first": "Kõigepealt valige maitse",
        "choose_flavor": "Valige maitse:",
        "stock_snus": "Snus",
        "stock_ecigs": "E-sigaretid",
        "stock_liquids": "Vedelikud",
        "coming_soon": " (varsti saadaval)",
        "coming_soon_text": "Varsti...",
        "order_not_available": "Toode pole saadaval",
        "order_quantity_unit": "tk",
        "order_accept_text": "Tellimus vastu võetud:\nToode: {product}\nMaitsed:\n{flavors}\nKoht: {place}\n\nKokku:\nToode: {product_price}€\nTarne: {delivery_price}\nTotaal hind: {total_price}€",
        "order_contact_text": "Võtke ühendust Telegramis: {contact}",
        "order_contact_mustamae": "@MayBeHim",
        "order_contact_centre": "@V1ne233 ja @MayBeHim",
        "order_contact_lasnamae": "@V1ne233",
        "order_contact_kopli": "@MayBeHim",
        "order_contact_oismae": "@MayBeHim",
        "order_contact_dpd": "@V1ne233 ja @MayBeHim",
        "category_prefix": "Kategooria:",
        "choose_item": "Valige toode:",
        "flavors": {
            "Apple Juice": "🍎 Apple Juice",
            "Banana Hit": "🍌 Banana Hit",
            "Black Currant": "🖤 Black Currant",
            "Blueberry": "🫐 Blueberry",
            "Cherry": "🍒 Cherry",
            "Cola": "🥤 Cola",
            "Cold Dry": "❄️ Cold Dry",
            "Double Fresh": "🌬️ Double Fresh",
            "Forest Berries": "🌲 Forest Berries",
            "Grape": "🍇 Grape",
            "Ice Spearmint": "🧊 Ice Spearmint",
            "Peach": "🍑 Peach",
            "Pineapple": "🍍 Pineapple",
            "Watermelon": "🍉 Watermelon",
            "CLASSIC": "🎯 Classic",
            "EUCALYPTUS": "🌿 Eucalyptus",
            "FRUIT COCKTAIL": "🍹 Fruit Cocktail",
            "MENTHOL": "❄️ Menthol",
            "WINTERGREEN": "🌲 Wintergreen",
            "LAVAFIRE": "🌋🔥 LAVAFIRE",
            "BLUEBERRY ICE": "🫐❄️ BLUEBERRY ICE",
            "BERRY PEACH": "🍓🍑 BERRY PEACH",
            "GRAPE ICE": "🍇❄️ GRAPE ICE",
            "BLUE RASPBERRY": "💙🍓 BLUE RASPBERRY",
            "BERRY": "🫐 BERRY",
            "BLUEBERRY WATERMELON": "🫐🍉 BLUEBERRY WATERMELON",
            "DRAGON FRUIT BANANA CHERRY": "🐉🍌 DRAGON FRUIT BANANA CHERRY",
            "PINEAPPLE PASSION FRUIT LIME": "🍍🥒 PINEAPPLE PASSION FRUIT LIME",
            "CHERRY COLA": "🍒🥤 CHERRY COLA",
            "POMEGRANATE LEMONADE": "🍒🍋 POMEGRANATE LEMONADE",
            "PERFUME LEMON": "🍋✨ PERFUME LEMON",
            "PEACH MANGO WATERMELON": "🍑🥭 PEACH MANGO WATERMELON",
            "STRAWBERRY WATERMELON": "🍓🍉 STRAWBERRY WATERMELON",
            "BLUE RAZZ LEMON": "🫐🍋 BLUE RAZZ LEMON",
            "STRAWBERRY ICE CREAM": "🍓🍦 STRAWBERRY ICE CREAM",
            "WATERMELON BUBBLE GUM": "🍉🎀 WATERMELON BUBBLE GUM",
            "KIWI PASSION FRUIT GUAVA": "🥝🍐 KIWI PASSION FRUIT GUAVA",
            "MIXED BERRIES": "🫐🍓 MIXED BERRIES",
            "PURPLE CANDY": "💜🍬 PURPLE CANDY",
            "PINEAPPLE COLADA": "🍍🥥 PINEAPPLE COLADA",
            "BLACKBERRY LEMON": "🖤🍋 BLACKBERRY LEMON",
            "STRAWBERRY RASPBERRY CHERRY ICE": "🍓🧊 STRAWBERRY RASPBERRY CHERRY ICE",
            "SOUR WATERMELON GUMMY": "🍉🍬 SOUR WATERMELON GUMMY",
            "PINK LEMONADE": "🍋💕 PINK LEMONADE",
            "GRAPE CHERRY": "🍇🍒 GRAPE CHERRY",
            "PINK GRAPEFRUIT": "🍑💕 PINK GRAPEFRUIT",
            "BLUEBERRY CHERRY CRANBERRY": "🫐🍒 BLUEBERRY CHERRY CRANBERRY",
            "CHERRY LIME RASPBERRY": "🍒🟢 CHERRY LIME RASPBERRY",
            "BLUEBERRY SOUR RASPBERRY": "🫐🍓 BLUEBERRY SOUR RASPBERRY",
            "LEMON LIME": "🍋🟢 LEMON LIME",
            "BLUEBERRY LEMONADE": "🫐🍋 BLUEBERRY LEMONADE",
            "FIZZY CHERRY": "🍒✨ FIZZY CHERRY",
            "MR BLUE": "💙❄️ MR BLUE",
            "BLACK ICE": "🖤❄️ BLACK ICE",
            "WATERMELON ICE": "🍉❄️ WATERMELON ICE",
            "BLUEBERRY RASPBERRY": "🫐🍓 BLUEBERRY RASPBERRY",
            "STRAWBERRY BANANA": "🍓🍌 STRAWBERRY BANANA",
            "SKY MINT": "🌌🍃 SKY MINT"
        },
        "catalog": "📦 Toodete kataloog:\n\nValige toode, et näha maitseid ja kirjeldust:",
        "category_snus": "Snus",
        "category_ecigs": "puffs",
        "category_liquids": "vedelikud",
        "order_text": "✅ Soovite tellida: {product}\n\nTellimuse esitamiseks võtke meiega ühendust:\n👤 {contact}\n\nMärkige järgmised andmed:\n• Toote nimi\n• Valitud maitse\n• Kogus\n• Tarneaadress",
        "product_not_found": "Toodet ei leitud",
        "back_catalog": "◀️ Tagasi kataloogi",
        "back_menu": "◀️ Tagasi menüüsse",
        "order_button": "🛒 Telli",
        "back_product": "◀️ Tagasi toote juurde",
        "change_language": "🌍 Muuda keelt",
        "in_stock": "✅ Saadaval",
        "out_of_stock": "❌ Pole saadaval",
        "clear_history": "🔄 Ajalugu kustutatud. Alustamiseks sisestage /start.",
        "personal_cabinet": "👤 Isiklik kabinet",
        "personal_cabinet_title": "👤 Teie isiklik kabinet",
        "orders_completed": "✅ Lõpetatud tehingud: {count}",
        "continue_shopping": "➕ Lisa muu toode",
        "finish_order": "✅ Lõpeta tellimus",
        "cart_title": "🛒 Teie ostukorv",
        "cart_summary": "Valitud tooted:",
        "order_summary_text": "Tellimus on paratamatu!",
        "total_items": "Kokku tooteid: {count}",
        "total_sum": "Summa: {sum}€",
        "orders_sum": "💰 Tellimuste kogusumma: {sum}€",
        "no_orders": "Teil pole veel lõpetatud tehinguid",
        "referral_system": "🎁 Referraaliprogramm",
        "referral_title": "🎁 Referraaliprogramm",
        "referral_text": "Kutsuge 20 inimest ja saage oma valitud toode täiesti tasuta.\n\nOmapoolse referraallingi saamiseks võtke ühendust @Sellamng",
        "insufficient_stock_single": "❌ Kahjuks on sellest maitsest jäänud vaid {stock} tk.",
        "insufficient_stock_multiple": "❌ {flavor}: saadaval on vaid {stock} tk, kuid te valisite {qty} tk.",
    }
}

# Хранилище языков пользователей
user_languages = {}

# Хранилище текущего заказа пользователя
user_order_session = {}

# Хранилище последних сообщений бота для очистки
user_message_ids = {}

# Хранилище сообщений пользователя для очистки
user_message_ids_customer = {}

# Хранилище завершённых заказов пользователей
# Структура: {user_id: {"completed": 5, "pending": 2, ...}}

# Хранилище для редактирования остатков вкусов в админ-панели
# Структура: {user_id: {"product_id": "snus1", "flavor": "Apple Juice", "quantity": 5}}
admin_flavor_edit_session = {}

# ==================== ЦЕНУ ====================
# Цены на товары (легко редактируется)
PRICES = {
    "snus1": 8,  # Цена Cuba Black 66mg в евро
    "snus2": 10,   # Цена Baron 77mg в евро
    "liquid1": 15,  # Vozol
    "liquid2": 15,  # Elfliq
    "liquid3": 15   # HQD liquid
}

# ==================== ФУНКЦИИ ОСТАТКОВ ====================
def format_flavor_with_stock(user_id, product_id, flavor):
    """Форматировать вкус с информацией об остатке ДЛЯ ЗАКАЗА
    
    Returns:
        - "❌ {flavor_display}" если остаток = 0
        - "✖️{quantity} {flavor_display}" если есть остаток
    """
    stock = db.get_flavor_stock(product_id, flavor)
    flavor_display = localize_flavor(user_id, flavor)
    
    if stock == 0:
        return f"❌ {flavor_display}"
    else:
        return f"✖️{stock} {flavor_display}"


def format_flavor_for_stock_view(user_id, product_id, flavor):
    """Форматировать вкус с информацией об остатке ДЛЯ НАЛИЧИЯ ТОВАРА
    
    Returns:
        - "❌ {flavor_display}" если остаток = 0
        - "✅ {flavor_display}" если есть остаток
    """
    stock = db.get_flavor_stock(product_id, flavor)
    flavor_display = localize_flavor(user_id, flavor)
    
    if stock == 0:
        return f"❌ {flavor_display}"
    else:
        return f"✅ {flavor_display}"


def get_available_flavors(product_id, flavors_list):
    """Получить список доступных вкусов (с остатком > 0)"""
    available = []
    for flavor in flavors_list:
        if db.get_flavor_stock(product_id, flavor) > 0:
            available.append(flavor)
    return available


def get_delivery_price(place):
    """Get delivery price based on location"""
    if place in ["mustamae", "centre", "lasnamae"]:
        return 0
    elif place == "kopli":
        return 4
    elif place == "oismae":
        return 3
    elif place == "dpd":
        return 4
    return 0

def extract_delivery_price_from_text(place_text):
    """Extract delivery price from place text like 'Мустамяе [FREE]' or 'Копли [+4€]'"""
    if "FREE" in place_text:
        return 0
    elif "+4€" in place_text:
        return 4
    elif "+3€" in place_text:
        return 3
    return 0

# ==================== ТОВАРЫ ====================
PRODUCTS = {
    "snus": [
        {
            "id": "snus1",
            "name": "Cuba Black 66mg",
            "in_stock": True,
            "flavors": ["Apple Juice", "Banana Hit", "Black Currant", "Blueberry", "Cherry", "Cola", "Cold Dry", "Double Fresh", "Forest Berries", "Grape", "Ice Spearmint", "Peach", "Pineapple", "Watermelon"]
        },
        {
            "id": "snus2",
            "name": "Baron 77mg",
            "in_stock": True,
            "flavors": ["CLASSIC", "EUCALYPTUS", "FRUIT COCKTAIL", "MENTHOL", "WINTERGREEN"]
        }
    ],
    "ecigs": [],
    "liquids": [
        {
            "id": "liquid1",
            "name": "Vozol",
            "in_stock": True,
            "flavors": ["LAVAFIRE", "BLUEBERRY ICE", "BERRY PEACH", "GRAPE ICE", "BLUE RASPBERRY", "BERRY", "BLUEBERRY WATERMELON", "DRAGON FRUIT BANANA CHERRY", "PINEAPPLE PASSION FRUIT LIME", "CHERRY COLA", "POMEGRANATE LEMONADE", "PERFUME LEMON", "PEACH MANGO WATERMELON", "STRAWBERRY WATERMELON", "BLUE RAZZ LEMON", "STRAWBERRY ICE CREAM", "WATERMELON BUBBLE GUM", "KIWI PASSION FRUIT GUAVA", "MIXED BERRIES", "PURPLE CANDY"]
        },
        {
            "id": "liquid2",
            "name": "Elfliq",
            "in_stock": True,
            "flavors": ["PINEAPPLE COLADA", "BLACKBERRY LEMON", "STRAWBERRY RASPBERRY CHERRY ICE", "SOUR WATERMELON GUMMY", "PINK LEMONADE", "GRAPE CHERRY", "PINK GRAPEFRUIT"]
        },
        {
            "id": "liquid3",
            "name": "HQD liquid",
            "in_stock": True,
            "flavors": ["BLUEBERRY CHERRY CRANBERRY", "CHERRY LIME RASPBERRY", "BLUEBERRY SOUR RASPBERRY", "LEMON LIME", "BLUEBERRY LEMONADE", "FIZZY CHERRY", "MR BLUE", "BLACK ICE", "WATERMELON ICE", "BLUEBERRY RASPBERRY", "STRAWBERRY BANANA", "SKY MINT"]
        }
    ]
}

ORDER_CONTACT = "1. @MayBeHim\n2. @V1ne233"

# ==================== ИНИЦИАЛИЗАЦИЯ ====================
bot = telebot.TeleBot(BOT_TOKEN)

# Регистрация команд в меню бота
bot.set_my_commands([
    telebot.types.BotCommand("start", "🌍 Выбор языка / Select language / Valige keel"),
    telebot.types.BotCommand("clear", "🔄 Очистить историю / Clear history / Kustuta ajalugu"),
    telebot.types.BotCommand("admin", "🔐 Админ-панель / Admin panel"),
    telebot.types.BotCommand("help", "ℹ️ Справка / Help")
])

# ==================== АДМИНИСТРАТОРЫ ====================
# Список разрешённых ID администраторов (легко редактируется)
ADMIN_IDS = {
    8238828402,
    1062486871,
    8217276872
}


# ==================== КЛАВИАТУРЫ ====================
def language_keyboard():
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🇷🇺 Русский", callback_data="lang:ru"))
    kb.add(InlineKeyboardButton("🇬🇧 English", callback_data="lang:en"))
    kb.add(InlineKeyboardButton("🇪🇪 Eesti", callback_data="lang:et"))
    return kb


def get_text(user_id, key):
    """Получить перевод текста для пользователя"""
    lang = user_languages.get(user_id, "ru")
    return LANGUAGES[lang].get(key, key)


def localize_flavor(user_id, flavor):
    lang = user_languages.get(user_id, "ru")
    return LANGUAGES[lang].get("flavors", {}).get(flavor, flavor)


def get_product_display_name(product):
    """Получить название товара с ценой для отображения в интерфейсе
    
    Args:
        product (dict): Словарь товара с полями 'id' и 'name'
    
    Returns:
        str: Название товара с ценой в формате "Название [цена€]" или просто "Название"
    """
    price = PRICES.get(product['id'])
    if price:
        return f"{product['name']} [{price}€]"
    return product['name']


def get_order_contact(place):
    if place == "mustamae":
        return "order_contact_mustamae"
    if place == "lasnamae":
        return "order_contact_lasnamae"
    if place == "centre":
        return "order_contact_centre"
    if place == "kopli":
        return "order_contact_kopli"
    if place == "oismae":
        return "order_contact_oismae"
    if place == "dpd":
        return "order_contact_dpd"
    return "order_contact_mustamae"


def track_message(user_id, message_id):
    user_message_ids.setdefault(user_id, []).append(message_id)


def track_customer_message(user_id, message_id):
    """Отслеживаем сообщения пользователя для последующей очистки"""
    user_message_ids_customer.setdefault(user_id, []).append(message_id)


def get_completed_orders_count(user_id):
    """
    Получить количество завершённых заказов пользователя
    
    Returns:
        int: Количество завершённых заказов
    """
    return db.get_completed_deals_count(user_id)


def add_completed_order(user_id):
    """
    Добавить завершённый заказ для пользователя
    
    Args:
        user_id: ID пользователя
    """
    db.add_user(user_id)
    db.increment_completed_deals(user_id)


def send_tracked_message(user_id, *args, **kwargs):
    msg = bot.send_message(user_id, *args, **kwargs)
    track_message(user_id, msg.message_id)
    return msg


def clear_user_history(user_id):
    user_languages.pop(user_id, None)
    user_order_session.pop(user_id, None)
    # Удаляем сообщения бота
    for mid in user_message_ids.pop(user_id, []):
        try:
            bot.delete_message(user_id, mid)
        except Exception:
            pass
    # Удаляем сообщения пользователя
    for mid in user_message_ids_customer.pop(user_id, []):
        try:
            bot.delete_message(user_id, mid)
        except Exception:
            pass


def get_product_by_id(product_id):
    for category_items in PRODUCTS.values():
        for item in category_items:
            if item.get("id") == product_id:
                return item
    return None


def main_menu_keyboard(user_id):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(get_text(user_id, "check_stock"), callback_data="view_stock"))
    kb.add(InlineKeyboardButton(get_text(user_id, "order"), callback_data="order_flow"))
    kb.add(InlineKeyboardButton(get_text(user_id, "bulk_order"), callback_data="bulk_order"))
    kb.add(InlineKeyboardButton(get_text(user_id, "personal_cabinet"), callback_data="personal_cabinet"))
    kb.add(InlineKeyboardButton(get_text(user_id, "referral_system"), callback_data="referral_system"))
    kb.add(InlineKeyboardButton(get_text(user_id, "managers"), callback_data="show_managers"))
    return kb


def managers_keyboard(user_id):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="main_menu"))
    return kb


def catalog_keyboard(user_id):
    kb = InlineKeyboardMarkup()
    for product_id, product in PRODUCTS.items():
        kb.add(InlineKeyboardButton(
            text=f"{product['name']}",
            callback_data=f"product:{product_id}"
        ))
    kb.add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="main_menu"))
    return kb


def product_keyboard(product_id, user_id):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(get_text(user_id, "order_button"), callback_data=f"order:{product_id}"))
    kb.add(InlineKeyboardButton(get_text(user_id, "back_catalog"), callback_data="catalog"))
    return kb


def back_keyboard(product_id, user_id):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(get_text(user_id, "back_product"), callback_data=f"product:{product_id}"))
    return kb


def order_product_keyboard(user_id):
    kb = InlineKeyboardMarkup()
    for product_list in PRODUCTS.values():
        for product in product_list:
            product_display = get_product_display_name(product)
            kb.add(InlineKeyboardButton(product_display, callback_data=f"order_product:{product['id']}"))
    kb.add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="main_menu"))
    return kb


def order_quantity_keyboard(user_id, product_id):
    kb = InlineKeyboardMarkup()
    
    # Эмодзи цифры для красивого отображения
    emoji_numbers = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    
    # Создаем кнопки в сетке 3 колонки
    buttons_row = []
    for qty in range(1, 11):
        buttons_row.append(InlineKeyboardButton(emoji_numbers[qty-1], callback_data=f"order_qty:{qty}"))
        if len(buttons_row) == 3:  # Добавляем по 3 в ряду
            kb.add(*buttons_row)
            buttons_row = []
    
    # Добавляем оставшиеся кнопки
    if buttons_row:
        kb.add(*buttons_row)
    
    kb.add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="main_menu"))
    return kb


def order_place_keyboard(user_id):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(get_text(user_id, "order_place_mustamae"), callback_data="order_place:mustamae"))
    kb.add(InlineKeyboardButton(get_text(user_id, "order_place_centre"), callback_data="order_place:centre"))
    kb.add(InlineKeyboardButton(get_text(user_id, "order_place_lasnamae"), callback_data="order_place:lasnamae"))
    kb.add(InlineKeyboardButton(get_text(user_id, "order_place_kopli"), callback_data="order_place:kopli"))
    kb.add(InlineKeyboardButton(get_text(user_id, "order_place_oismae"), callback_data="order_place:oismae"))
    kb.add(InlineKeyboardButton(get_text(user_id, "order_place_dpd"), callback_data="order_place:dpd"))
    kb.add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="main_menu"))
    return kb


def order_complete_keyboard(user_id):
    """Клавиатура для завершенного заказа - только кнопка в меню"""
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="main_menu"))
    return kb


def order_continue_keyboard(user_id):
    """Клавиатура для продолжения покупок - добавить товар или завершить"""
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(get_text(user_id, "continue_shopping"), callback_data="order_flow"))
    kb.add(InlineKeyboardButton(get_text(user_id, "finish_order"), callback_data="order_place_now"))
    kb.add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="main_menu"))
    return kb


def format_cart_summary(user_id):
    """Форматировать содержимое корзины для отображения пользователю"""
    data = user_order_session.get(user_id, {})
    products = data.get("products", [])
    
    if not products:
        return get_text(user_id, "cart_empty") if "cart_empty" in get_text(user_id, "cart_title") else ""
    
    summary = f"{get_text(user_id, 'cart_summary')}\n\n"
    total_items = 0
    total_sum = 0
    
    for product_data in products:
        product_id = product_data.get("product_id")
        product = get_product_by_id(product_id)
        flavors = product_data.get("flavors", {})
        
        if product and flavors:
            product_price = PRICES.get(product_id, 8)
            for flavor, qty in flavors.items():
                total_items += qty
                item_price = qty * product_price
                total_sum += item_price
                flavor_display = localize_flavor(user_id, flavor)
                summary += f"• {product['name']} - {flavor_display}: {qty} шт. ({item_price}€)\n"
    
    summary += f"\n{get_text(user_id, 'total_items').format(count=total_items)}\n"
    summary += f"{get_text(user_id, 'total_sum').format(sum=total_sum)}\n"
    
    return summary


# ==================== ХЭНДЛЕРЫ ====================
@bot.message_handler(commands=["start"])
def cmd_start(message):
    user_id = message.chat.id
    username = message.chat.username
    first_name = message.chat.first_name
    
    # Регистрируем пользователя в БД
    db.add_user(user_id, username, first_name)
    
    # Отслеживаем сообщение пользователя (/start команду)
    track_customer_message(user_id, message.message_id)
    # Очищаем всю историю пользователя перед началом новой сессии
    clear_user_history(user_id)
    # Отслеживаем первое сообщение бота для последующей очистки
    msg = bot.send_message(
        user_id,
        LANGUAGES["ru"]["language_select"],
        reply_markup=language_keyboard()
    )
    track_message(user_id, msg.message_id)


@bot.message_handler(commands=["clear"])
def cmd_clear(message):
    """Команда /clear — очищает историю пользователя (язык, заказ, сообщения)"""
    user_id = message.chat.id
    # Отслеживаем сообщение пользователя (/clear команду) перед очисткой
    track_customer_message(user_id, message.message_id)
    
    # Получаем язык пользователя перед очисткой (или используем русский по умолчанию)
    user_lang = user_languages.get(user_id, "ru")
    
    # Очищаем всю историю пользователя
    clear_user_history(user_id)
    
    # Отправляем подтверждение на языке пользователя
    confirmation_text = {
        "ru": "🔄 История очищена. Введите /start для начала заново.",
        "en": "🔄 History cleared. Enter /start to begin again.",
        "et": "🔄 Ajalugu kustutatud. Alustamiseks sisestage /start."
    }
    
    confirmation_msg = bot.send_message(user_id, confirmation_text.get(user_lang, confirmation_text["ru"]))
    # Отслеживаем подтверждающее сообщение для следующей очистки
    track_message(user_id, confirmation_msg.message_id)


@bot.message_handler(commands=["admin"])
def cmd_admin(message):
    """Команда /admin - вход в админ-панель"""
    user_id = message.chat.id
    track_customer_message(user_id, message.message_id)
    
    # Проверяем, есть ли user_id в списке разрешённых администраторов
    if user_id not in ADMIN_IDS:
        msg = bot.send_message(user_id, "❌ Доступ запрещён. Вы не администратор.")
        track_message(user_id, msg.message_id)
        return
    
    # Открываем админ-панель для авторизованного пользователя
    show_admin_menu(user_id)


def show_admin_menu(user_id):
    """Показать меню администратора"""
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("📊 Статистика", callback_data="admin_stats"))
    kb.add(InlineKeyboardButton("🔄 Изменить количество", callback_data="admin_edit_stock"))
    kb.add(InlineKeyboardButton("⏳ Ожидающие заказы", callback_data="admin_pending_orders"))
    kb.add(InlineKeyboardButton("✅ База клиентов", callback_data="admin_confirmed_orders"))
    kb.add(InlineKeyboardButton("❌ Выход", callback_data="admin_logout"))
    
    msg = bot.send_message(
        user_id,
        "📋 Меню администратора:\n\n✅ Добро пожаловать в админ-панель!",
        reply_markup=kb
    )
    track_message(user_id, msg.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "admin_stats")
def admin_show_stats(call):
    """Показать статистику"""
    user_id = call.message.chat.id
    
    if user_id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ Доступ запрещен", show_alert=True)
        return
    
    # Получаем глобальную статистику
    total_users = db.get_total_users_count()
    total_orders = db.get_total_completed_orders_count()
    total_earnings = db.get_total_earnings()
    
    stats_text = f"""
📊 Статистика бота:

👥 Всего пользователей: {total_users}
🛒 Выполнено заказов: {total_orders}
💰 Общий заработок: {total_earnings:.2f}€

🕐 Активные сессии:
  • Пользователей: {len(user_languages)}
  • Заказов: {len(user_order_session)}
"""
    
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("◀️ Назад", callback_data="admin_back_menu"))
    
    bot.edit_message_text(stats_text, call.message.chat.id, call.message.message_id, reply_markup=kb)
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == "admin_back_menu")
def admin_back_menu(call):
    """Вернуться в меню адмитра"""
    user_id = call.message.chat.id
    
    # Проверяем, есть ли user_id в списке разрешённых администраторов
    if user_id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ Доступ запрещен", show_alert=True)
        return
    
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("📊 Статистика", callback_data="admin_stats"))
    kb.add(InlineKeyboardButton("🔄 Изменить количество", callback_data="admin_edit_stock"))
    kb.add(InlineKeyboardButton("⏳ Ожидающие заказы", callback_data="admin_pending_orders"))
    kb.add(InlineKeyboardButton("✅ База клиентов", callback_data="admin_confirmed_orders"))
    kb.add(InlineKeyboardButton("❌ Выход", callback_data="admin_logout"))
    
    bot.edit_message_text(
        "📋 Меню администратора",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=kb
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == "admin_logout")
def admin_logout(call):
    """Выход из админ-панели"""
    user_id = call.message.chat.id
    # При выходе просто показываем сообщение (нет необходимости отслеживать сессию)
    
    bot.edit_message_text(
        "👋 Вы вышли из панели администратора.",
        call.message.chat.id,
        call.message.message_id
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == "admin_edit_stock")
def admin_edit_stock(call):
    """Показать список товаров для редактирования остатков"""
    user_id = call.message.chat.id
    
    if user_id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ Доступ запрещен", show_alert=True)
        return
    
    text = "🔄 Выберите товар для редактирования остатков вкусов:\n\n"
    
    kb = InlineKeyboardMarkup()
    for category_name, products in PRODUCTS.items():
        for product in products:
            kb.add(InlineKeyboardButton(product['name'], callback_data=f"admin_edit_flavors:{product['id']}"))
    
    kb.add(InlineKeyboardButton("◀️ Назад", callback_data="admin_back_menu"))
    
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb)
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_edit_flavors:"))
def admin_edit_flavors(call):
    """Показать список вкусов товара для редактирования"""
    user_id = call.message.chat.id
    
    if user_id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ Доступ запрещен", show_alert=True)
        return
    
    product_id = call.data.split(":")[1]
    product = get_product_by_id(product_id)
    
    if not product:
        bot.answer_callback_query(call.id, "❌ Товар не найден", show_alert=True)
        return
    
    text = f"🔄 Редактирование остатков: {product['name']}\n\n"
    
    kb = InlineKeyboardMarkup(row_width=1)
    for flavor in product['flavors']:
        stock = db.get_flavor_stock(product_id, flavor)
        button_text = f"{format_flavor_with_stock(user_id, product_id, flavor)} — {stock} шт"
        kb.add(InlineKeyboardButton(button_text, callback_data=f"admin_edit_flavor_qty:{product_id}:{flavor}"))
    
    kb.add(InlineKeyboardButton("◀️ Назад", callback_data="admin_edit_stock"))
    
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb)
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_edit_flavor_qty:"))
def admin_edit_flavor_qty(call):
    """Открыть окно редактирования количества для вкуса"""
    user_id = call.message.chat.id
    
    if user_id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ Доступ запрещен", show_alert=True)
        return
    
    parts = call.data.split(":")
    product_id = parts[1]
    flavor = ":".join(parts[2:])  # В случае если название вкуса содержит ':'
    
    product = get_product_by_id(product_id)
    if not product:
        bot.answer_callback_query(call.id, "❌ Товар не найден", show_alert=True)
        return
    
    current_stock = db.get_flavor_stock(product_id, flavor)
    flavor_display = localize_flavor(user_id, flavor)
    
    # Сохраняем текущую сессию редактирования
    admin_flavor_edit_session[user_id] = {
        "product_id": product_id,
        "flavor": flavor,
        "quantity": current_stock
    }
    
    text = f"""
🔄 Редактирование: {product['name']}
Вкус: {flavor_display}

Текущее количество: {current_stock} шт

Используйте кнопки ниже для изменения:
"""
    
    kb = InlineKeyboardMarkup()
    # Первый ряд: -10, -1, Текущее значение, +1, +10
    kb.row(
        InlineKeyboardButton("➖➖ -10", callback_data=f"admin_qty_change:{product_id}:{flavor}:-10"),
        InlineKeyboardButton("➖ -1", callback_data=f"admin_qty_change:{product_id}:{flavor}:-1")
    )
    kb.row(
        InlineKeyboardButton(f"📊 {current_stock}", callback_data="admin_qty_info")
    )
    kb.row(
        InlineKeyboardButton("➕ +1", callback_data=f"admin_qty_change:{product_id}:{flavor}:1"),
        InlineKeyboardButton("➕➕ +10", callback_data=f"admin_qty_change:{product_id}:{flavor}:10")
    )
    kb.row(
        InlineKeyboardButton("✅ Подтвердить", callback_data=f"admin_qty_confirm:{product_id}:{flavor}"),
        InlineKeyboardButton("❌ Отмена", callback_data=f"admin_edit_flavors:{product_id}")
    )
    
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb)
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_qty_change:"))
def admin_qty_change(call):
    """Изменить количество"""
    user_id = call.message.chat.id
    
    if user_id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ Доступ запрещен", show_alert=True)
        return
    
    parts = call.data.split(":")
    product_id = parts[1]
    flavor = ":".join(parts[2:-1])
    change = int(parts[-1])
    
    # Получаем текущую сессию
    session = admin_flavor_edit_session.get(user_id, {})
    current_qty = session.get("quantity", 0)
    
    # Изменяем количество
    new_qty = max(0, current_qty + change)
    session["quantity"] = new_qty
    admin_flavor_edit_session[user_id] = session
    
    product = get_product_by_id(product_id)
    flavor_display = localize_flavor(user_id, flavor)
    
    text = f"""
🔄 Редактирование: {product['name']}
Вкус: {flavor_display}

Текущее количество: {new_qty} шт

Используйте кнопки ниже для изменения:
"""
    
    kb = InlineKeyboardMarkup()
    kb.row(
        InlineKeyboardButton("➖➖ -10", callback_data=f"admin_qty_change:{product_id}:{flavor}:-10"),
        InlineKeyboardButton("➖ -1", callback_data=f"admin_qty_change:{product_id}:{flavor}:-1")
    )
    kb.row(
        InlineKeyboardButton(f"📊 {new_qty}", callback_data="admin_qty_info")
    )
    kb.row(
        InlineKeyboardButton("➕ +1", callback_data=f"admin_qty_change:{product_id}:{flavor}:1"),
        InlineKeyboardButton("➕➕ +10", callback_data=f"admin_qty_change:{product_id}:{flavor}:10")
    )
    kb.row(
        InlineKeyboardButton("✅ Подтвердить", callback_data=f"admin_qty_confirm:{product_id}:{flavor}"),
        InlineKeyboardButton("❌ Отмена", callback_data=f"admin_edit_flavors:{product_id}")
    )
    
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb)
    bot.answer_callback_query(call.id, "✅ Количество обновлено")


@bot.callback_query_handler(func=lambda call: call.data == "admin_qty_info")
def admin_qty_info(call):
    """Просто информационная кнопка"""
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_qty_confirm:"))
def admin_qty_confirm(call):
    """Подтвердить изменение количества"""
    user_id = call.message.chat.id
    
    if user_id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ Доступ запрещен", show_alert=True)
        return
    
    parts = call.data.split(":")
    product_id = parts[1]
    flavor = ":".join(parts[2:])
    
    session = admin_flavor_edit_session.get(user_id, {})
    new_qty = session.get("quantity", 0)
    
    # Сохраняем в БД
    db.set_flavor_stock(product_id, flavor, new_qty)
    
    # Очищаем сессию
    admin_flavor_edit_session.pop(user_id, None)
    
    bot.answer_callback_query(call.id, "✅ Количество сохранено", show_alert=True)
    
    # Возвращаемся к списку вкусов
    admin_edit_flavors(call)


@bot.callback_query_handler(func=lambda call: call.data == "admin_pending_orders")
def admin_show_pending_orders(call):
    """Показать все ожидающие заказы"""
    user_id = call.message.chat.id
    
    if user_id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ Доступ запрещен", show_alert=True)
        return
    
    pending_orders = db.get_pending_orders()
    
    if not pending_orders:
        text = "🔔 Нет ожидающих заказов"
        kb = InlineKeyboardMarkup()
        kb.add(InlineKeyboardButton("◀️ Назад", callback_data="admin_back_menu"))
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb)
        bot.answer_callback_query(call.id)
        return
    
    # Показываем список ожидающих заказов с кнопками для действий
    text = f"⏳ Ожидающие заказы ({len(pending_orders)}):\n\n"
    
    kb = InlineKeyboardMarkup()
    for order in pending_orders[:10]:  # Показываем первые 10
        order_text = f"#{order['id']} - {order['product']}"
        kb.add(InlineKeyboardButton(order_text, callback_data=f"admin_order_detail:{order['id']}"))
    
    kb.add(InlineKeyboardButton("◀️ Назад", callback_data="admin_back_menu"))
    
    text += f"Всего ожидающих: {len(pending_orders)}"
    if len(pending_orders) > 10:
        text += f"\n(Показаны первые 10)"
    
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb)
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == "admin_confirmed_orders")
def admin_show_confirmed_orders(call):
    """Показать все подтвержденные заказы (база клиентов)"""
    user_id = call.message.chat.id
    
    # Проверяем, есть ли user_id в списке разрешённых администраторов
    if user_id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ Доступ запрещен", show_alert=True)
        return
    
    # Получаем список клиентов с подтвержденными заказами
    customers = db.get_customers_with_confirmed_orders()
    
    if not customers:
        text = "📭 Нет подтвержденных заказов"
        kb = InlineKeyboardMarkup()
        kb.add(InlineKeyboardButton("◀️ Назад", callback_data="admin_back_menu"))
        bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb)
        bot.answer_callback_query(call.id)
        return
    
    # Показываем список клиентов с подтвержденными заказами
    text = f"✅ База клиентов ({len(customers)}):\n\n"
    
    kb = InlineKeyboardMarkup()
    for customer in customers:
        # Формируем отображаемое имя
        display_name = customer['first_name'] or customer['username'] or f"ID: {customer['user_id']}"
        button_text = f"👤 {display_name}"
        kb.add(InlineKeyboardButton(button_text, callback_data=f"admin_customer_detail:{customer['user_id']}"))
    
    kb.add(InlineKeyboardButton("◀️ Назад", callback_data="admin_back_menu"))
    
    text += "Щелкните на клиента для просмотра деталей"
    
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb)
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_customer_detail:"))
def admin_customer_detail(call):
    """Показать детали клиента - ID и количество подтвержденных заказов"""
    user_id = call.message.chat.id
    
    if user_id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ Доступ запрещен", show_alert=True)
        return
    
    customer_id = int(call.data.split(":")[1])
    
    # Получаем информацию о пользователе
    customer = db.get_user(customer_id)
    
    if not customer:
        bot.answer_callback_query(call.id, "❌ Пользователь не найден", show_alert=True)
        return
    
    # Получаем количество подтвержденных заказов
    confirmed_orders = db.get_user_confirmed_orders(customer_id)
    confirmed_count = len(confirmed_orders)
    
    # Рассчитываем общую сумму всех заказов
    total_amount = 0
    for order in confirmed_orders:
        order_total = order.get('total_price', 0)
        if order_total == 0:
            # Для старых заказов, если total_price не сохранен
            product_price = order['quantity'] * PRICES.get(order.get('product_id', 'snus1'), 8)
            delivery_price = extract_delivery_price_from_text(order['place'])
            order_total = product_price + delivery_price
        total_amount += order_total
    
    # Формируем информацию о клиенте
    display_name = customer.get('first_name') or customer.get('username') or "Без имени"
    
    text = f"""
👤 Информация о клиенте
━━━━━━━━━━━━━━━━━━
📍 ID пользователя: {customer_id}
👤 Имя: {display_name}
✅ Подтвержденных заказов: {confirmed_count}
💰 Сумма всех заказов: {total_amount}€
"""
    
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton("🧹 Удалить данные", callback_data=f"admin_delete_customer:{customer_id}"))
    kb.add(InlineKeyboardButton("◀️ Назад", callback_data="admin_confirmed_orders"))
    
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb)
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_delete_customer:"))
def admin_delete_customer(call):
    """Удалить данные клиента"""
    user_id = call.message.chat.id
    
    # Проверяем, есть ли user_id в списке разрешённых администраторов
    if user_id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ Доступ запрещен", show_alert=True)
        return
    
    customer_id = int(call.data.split(":")[1])
    
    # Удаляем клиента и его заказы из БД
    if db.delete_user_with_orders(customer_id):
        bot.answer_callback_query(call.id, "✅ Данные клиента удалены", show_alert=True)
        # Возвращаемся к списку клиентов
        admin_show_confirmed_orders(call)
    else:
        bot.answer_callback_query(call.id, "❌ Ошибка при удалении данных", show_alert=True)


@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_order_detail:"))
def admin_order_detail(call):
    """Показать детали заказа и действия"""
    user_id = call.message.chat.id
    
    if user_id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ Доступ запрещен", show_alert=True)
        return
    
    order_id = int(call.data.split(":")[1])
    order = db.get_order_with_user_info(order_id)
    
    if not order:
        bot.answer_callback_query(call.id, "❌ Заказ не найден", show_alert=True)
        return
    
    # Форматируем дату
    from datetime import datetime
    try:
        created_at = datetime.fromisoformat(order['created_at']).strftime("%d.%m.%Y %H:%M")
    except:
        created_at = order['created_at']
    
    user_info = f"👤 {order['username'] or 'Без имени'} (ID: {order['user_id']})"
    if order['first_name']:
        user_info = f"👤 {order['first_name']} {order['username'] or ''} (ID: {order['user_id']})"
    
    # Используем сохраненные цены из заказа
    total_price = order.get('total_price', 0)
    delivery_price = extract_delivery_price_from_text(order['place'])
    if total_price == 0:
        # Для старых заказов, если total_price не сохранен
        product_price = order['quantity'] * PRICES.get(order.get('product_id', 'snus1'), 8)
        total_price = product_price + delivery_price
    else:
        product_price = total_price - delivery_price
    delivery_text = "FREE" if delivery_price == 0 else f"{delivery_price}€"
    
    text = f"""
📦 Заказ #{order['id']}
━━━━━━━━━━━━━━━━━━
{user_info}

🛍️ Товар: {order['product']}
🍬 Вкусы: {order['flavors']}
📍 Место: {order['place']}
📊 Количество: {order['quantity']}
📅 Дата: {created_at}
📌 Статус: {order['status']}

💰 Итого:
   Товар: {product_price}€
   Доставка: {delivery_text}
   Полная цена: {total_price}€
"""
    
    kb = InlineKeyboardMarkup()
    
    # Показываем действия в зависимости от статуса
    if order['status'] == 'pending':
        kb.add(InlineKeyboardButton("✅ Подтвердить", callback_data=f"admin_confirm_order:{order_id}"), InlineKeyboardButton("❌ Отклонить", callback_data=f"admin_reject_order:{order_id}"))
    elif order['status'] in ('confirmed', 'completed'):
        kb.add(InlineKeyboardButton("⏳ Вернуть в ожидание", callback_data=f"admin_pending_order:{order_id}"))
    
    kb.add(InlineKeyboardButton("◀️ Назад", callback_data="admin_back_menu"))
    
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=kb)
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_confirm_order:"))
def admin_confirm_order(call):
    """Подтвердить заказ"""
    user_id = call.message.chat.id
    
    if user_id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ Доступ запрещен", show_alert=True)
        return
    
    order_id = int(call.data.split(":")[1])
    
    # Получаем информацию о заказе, включая user_id
    order = db.get_order_with_user_info(order_id)
    
    if order:
        # ТЕПЕРЬ уменьшаем остатки при подтверждении
        product_id = order.get('product_id')
        if product_id and order.get('flavors'):
            # Парсим flavors из строки
            flavors_text = order['flavors']  # например "Apple: 2, Cherry: 1"
            try:
                import re
                # Ищем все вкусы и количества
                matches = re.findall(r'(.+?):\s*(\d+)', flavors_text)
                for flavor_display, qty_str in matches:
                    flavor = flavor_display.strip()
                    qty = int(qty_str)
                    # Уменьшаем остаток (qty должен быть quantity из заказа)
                    db.decrease_flavor_stock(product_id, flavor, qty)
            except Exception as e:
                print(f"Ошибка при уменьшении остатков: {e}")
    
    # Обновляем статус на 'confirmed'
    if db.update_order_status(order_id, 'confirmed'):
        # Увеличиваем счетчик осуществленных заказов для пользователя
        if order:
            db.increment_completed_deals(order['user_id'])
        
        bot.answer_callback_query(call.id, "✅ Заказ подтвержден", show_alert=True)
        # Возвращаемся к списку ожидающих заказов
        admin_show_pending_orders(call)
    else:
        bot.answer_callback_query(call.id, "❌ Ошибка при подтверждении", show_alert=True)


@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_reject_order:"))
def admin_reject_order(call):
    """Отклонить заказ"""
    user_id = call.message.chat.id
    
    if user_id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ Доступ запрещен", show_alert=True)
        return
    
    order_id = int(call.data.split(":")[1])
    
    # Обновляем статус на 'rejected'
    if db.update_order_status(order_id, 'rejected'):
        bot.answer_callback_query(call.id, "❌ Заказ отклонен", show_alert=True)
        # Возвращаемся к списку ожидающих заказов
        admin_show_pending_orders(call)
    else:
        bot.answer_callback_query(call.id, "❌ Ошибка при отклонении заказа", show_alert=True)


@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_pending_order:"))
def admin_pending_order(call):
    """Вернуть заказ в статус ожидания"""
    user_id = call.message.chat.id
    
    if user_id not in ADMIN_IDS:
        bot.answer_callback_query(call.id, "❌ Доступ запрещен", show_alert=True)
        return
    
    order_id = int(call.data.split(":")[1])
    
    # Обновляем статус на 'pending'
    if db.update_order_status(order_id, 'pending'):
        bot.answer_callback_query(call.id, "⏳ Заказ возвращен в ожидание", show_alert=True)
        # Возвращаемся к списку подтвержденных заказов
        admin_show_confirmed_orders(call)
    else:
        bot.answer_callback_query(call.id, "❌ Ошибка при изменении статуса", show_alert=True)


@bot.message_handler(commands=["help"])
def cmd_help(message):
    """Команда /help - справка"""
    user_id = message.chat.id
    track_customer_message(user_id, message.message_id)
    
    help_text = """
ℹ️ Справка команд:

/start - начало работы (выбор языка)
/admin - вход в админ-панель
/clear - очистить историю чата
/help - эта справка

🛍️ В боте доступно:
  • Просмотр наличия товара
  • Оформление заказов
  • Информация о менеджерах
  • Большие оптовые заказы
"""
    
    msg = bot.send_message(user_id, help_text)
    track_message(user_id, msg.message_id)


@bot.message_handler(content_types=["text"])
def handle_text_messages(message):
    """Отслеживаем все текстовые сообщения для очистки истории"""
    user_id = message.chat.id
    track_customer_message(user_id, message.message_id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("lang:"))
def select_language(call):
    user_id = call.message.chat.id
    lang = call.data.split(":")[1]
    user_languages[user_id] = lang
    
    # Показываем главное меню после выбора языка
    bot.edit_message_text(
        get_text(user_id, "main_menu"),
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=main_menu_keyboard(user_id)
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == "main_menu")
def show_main_menu(call):
    user_id = call.message.chat.id
    bot.edit_message_text(
        get_text(user_id, "main_menu"),
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=main_menu_keyboard(user_id)
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == "bulk_order")
def show_bulk_order(call):
    user_id = call.message.chat.id
    bot.edit_message_text(
        get_text(user_id, "bulk_order_response"),
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="main_menu"))
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == "view_stock")
def show_stock(call):
    user_id = call.message.chat.id
    coming_soon = get_text(user_id, "coming_soon")
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(get_text(user_id, "stock_snus"), callback_data="category:snus"))
    kb.add(InlineKeyboardButton(f"{get_text(user_id, 'stock_ecigs')}{coming_soon}", callback_data="nolink"))
    kb.add(InlineKeyboardButton(get_text(user_id, "stock_liquids"), callback_data="category:liquids"))
    kb.add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="main_menu"))
    bot.edit_message_text(
        get_text(user_id, "check_stock"),
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=kb
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == "order_flow")
def order_flow(call):
    user_id = call.message.chat.id
    data = user_order_session.get(user_id, {})
    
    # Сохраняем текущий товар если он выбран
    current_flavors = data.get("flavors", {})
    if current_flavors and "product_id" in data and data.get("product_id"):
        if "products" not in data:
            data["products"] = []
        
        # Добавляем текущий товар в список
        product_data = {
            "product_id": data.get("product_id"),
            "flavors": current_flavors.copy()
        }
        
        # Проверяем, не добавили ли мы уже это товар с этими вкусами
        product_exist = False
        for existing_product in data["products"]:
            if existing_product["product_id"] == data["product_id"]:
                # Объединяем вкусы если товар уже в корзине
                existing_product["flavors"].update(current_flavors)
                product_exist = True
                break
        
        if not product_exist:
            data["products"].append(product_data)
        
        # Очищаем текущую сессию товара
        data["flavors"] = {}
        data["current_flavor"] = None
        data["product_id"] = None
    
    # Инициализируем products если их еще нет
    if "products" not in data:
        data["products"] = []
    
    user_order_session[user_id] = data
    
    # Показываем выбор категории
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(get_text(user_id, "category_snus"), callback_data="order_category:snus"))
    kb.add(InlineKeyboardButton(get_text(user_id, "category_liquids"), callback_data="order_category:liquids"))
    kb.add(InlineKeyboardButton(f"{get_text(user_id, 'category_ecigs')} {get_text(user_id, 'coming_soon')}", callback_data="nolink"))
    kb.add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="main_menu"))
    
    text = get_text(user_id, "choose_item")
    
    bot.edit_message_text(
        text,
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=kb
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("order_category:"))
def order_category_select(call):
    user_id = call.message.chat.id
    category = call.data.split(":", 1)[1]
    
    if category not in PRODUCTS:
        bot.answer_callback_query(call.id, "❌ Категория не найдена", show_alert=True)
        return
    
    products = PRODUCTS[category]
    
    if not products:
        bot.answer_callback_query(call.id, "❌ Товары в этой категории отсутствуют", show_alert=True)
        return
    
    # Показываем товары выбранной категории
    kb = InlineKeyboardMarkup()
    for product in products:
        product_display = get_product_display_name(product)
        kb.add(InlineKeyboardButton(product_display, callback_data=f"order_product_select:{product['id']}"))
    kb.add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="order_flow"))
    
    bot.edit_message_text(
        get_text(user_id, "choose_item"),
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=kb
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("order_product_select:"))
def order_product_select(call):
    user_id = call.message.chat.id
    product_id = call.data.split(":", 1)[1]
    product = get_product_by_id(product_id)
    if not product:
        bot.answer_callback_query(call.id, get_text(user_id, "product_not_found"), show_alert=True)
        return

    # Получаем текущую сессию
    data = user_order_session.get(user_id, {"products": []})
    
    # Сохраняем предыдущий товар если он был выбран
    prev_flavors = data.get("flavors", {})
    if prev_flavors and data.get("product_id"):
        if "products" not in data:
            data["products"] = []
        
        prev_product_data = {
            "product_id": data.get("product_id"),
            "flavors": prev_flavors.copy()
        }
        
        # Проверяем, не добавили ли мы уже это товар
        product_exist = False
        for existing_product in data["products"]:
            if existing_product["product_id"] == data.get("product_id"):
                existing_product["flavors"].update(prev_flavors)
                product_exist = True
                break
        
        if not product_exist and prev_flavors:
            data["products"].append(prev_product_data)
    
    # Инициализируем новый товар
    data["product_id"] = product_id
    data["flavors"] = {}
    data["current_flavor"] = None
    
    # Убеждаемся, что products существует
    if "products" not in data:
        data["products"] = []
    
    user_order_session[user_id] = data

    bot.edit_message_text(
        get_text(user_id, "order_choose_flavor").format(product=get_product_display_name(product)),
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=order_flavor_keyboard(user_id)
    )
    bot.answer_callback_query(call.id)


def order_flavor_keyboard(user_id):
    data = user_order_session.get(user_id, {})
    product_id = data.get("product_id")
    if not product_id:
        product_id = "snus1"  # Default fallback
    
    product = get_product_by_id(product_id)
    flavors = data.get("flavors", {})

    kb = InlineKeyboardMarkup()
    for flavor in product.get("flavors", []):
        qty = flavors.get(flavor)
        flavor_with_stock = format_flavor_with_stock(user_id, product_id, flavor)
        
        # Если остаток 0, блокируем кнопку, иначе показываем возможность выбора
        if db.get_flavor_stock(product_id, flavor) == 0:
            # Блокированная кнопка - невозможно выбрать
            label = f"{flavor_with_stock}" + (f" ({qty})" if qty else "")
            kb.add(InlineKeyboardButton(label, callback_data="nolink"))
        else:
            # Активная кнопка
            label = f"{flavor_with_stock}" + (f" ({qty})" if qty else "")
            kb.add(InlineKeyboardButton(label, callback_data=f"order_flavor:{flavor}"))

    if flavors:
        kb.add(InlineKeyboardButton(get_text(user_id, "order_place_button"), callback_data="order_place_now"))
    kb.add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="main_menu"))
    return kb


@bot.callback_query_handler(func=lambda call: call.data.startswith("order_flavor:"))
def order_flavor(call):
    user_id = call.message.chat.id
    flavor = call.data.split(":", 1)[1]
    data = user_order_session.get(user_id)
    if not data:
        bot.answer_callback_query(call.id, get_text(user_id, "order_select_taste_first"), show_alert=True)
        return

    data["current_flavor"] = flavor
    user_order_session[user_id] = data
    
    product_id = data.get("product_id", "snus1")

    bot.edit_message_text(
        get_text(user_id, "order_choose_quantity").format(flavor=localize_flavor(user_id, flavor)),
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=order_quantity_keyboard(user_id, product_id)
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == "order_place_now")
def order_place_now(call):
    user_id = call.message.chat.id
    data = user_order_session.get(user_id)
    
    # Сохраняем текущий товар в список products
    current_flavors = data.get("flavors", {})
    if current_flavors and "product_id" in data and data.get("product_id"):
        if "products" not in data:
            data["products"] = []
        
        product_data = {
            "product_id": data.get("product_id"),
            "flavors": current_flavors.copy()
        }
        
        # Проверяем, не есть ли уже такой товар
        product_exist = False
        for existing_product in data["products"]:
            if existing_product["product_id"] == data["product_id"]:
                existing_product["flavors"].update(current_flavors)
                product_exist = True
                break
        
        if not product_exist:
            data["products"].append(product_data)
    
    if not data or not data.get("products") or sum(len(p.get("flavors", {})) for p in data.get("products", [])) == 0:
        bot.answer_callback_query(call.id, get_text(user_id, "order_select_taste_first"), show_alert=True)
        return

    user_order_session[user_id] = data

    bot.edit_message_text(
        get_text(user_id, "order_choose_place"),
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=order_place_keyboard(user_id)
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("order_qty:"))
def order_qty(call):
    user_id = call.message.chat.id
    qty = int(call.data.split(":")[1])
    data = user_order_session.get(user_id)
    if not data or not data.get("current_flavor"):
        bot.answer_callback_query(call.id, get_text(user_id, "order_select_taste_first"), show_alert=True)
        return

    flavor = data["current_flavor"]
    product_id = data.get("product_id")
    
    # Проверяем наличие товара
    available_stock = db.get_flavor_stock(product_id, flavor)
    if qty > available_stock:
        error_msg = get_text(user_id, "insufficient_stock_single").format(stock=available_stock)
        bot.answer_callback_query(
            call.id, 
            error_msg,
            show_alert=True
        )
        return
    
    # Инициализируем products если это новый заказ
    if "products" not in data:
        data["products"] = []
    
    flavors = data.get("flavors", {})
    flavors[flavor] = qty
    data["flavors"] = flavors
    data["current_flavor"] = None
    user_order_session[user_id] = data

    qty_unit = get_text(user_id, "order_quantity_unit")
    selected = ", ".join([f"{localize_flavor(user_id, f)} ({q} {qty_unit})" for f, q in flavors.items()])
    
    # Формируем текст с текущим товаром
    product = get_product_by_id(product_id)
    current_product_text = f"\n✅ {get_text(user_id, 'cart_title')}:\n{product['name']}\n{selected}\n"
    
    bot.edit_message_text(
        get_text(user_id, "order_flavor_selected").format(flavors=selected) + current_product_text,
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=order_continue_keyboard(user_id)
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("order_place:"))
def order_place(call):
    user_id = call.message.chat.id
    place = call.data.split(":")[1]
    data = user_order_session.get(user_id)
    
    if not data or not data.get("products") or len(data.get("products", [])) == 0:
        bot.answer_callback_query(call.id, "Сначала выберите товар и вкусы", show_alert=True)
        return
    
    # Проверяем наличие товаров для всех товаров в корзине
    for product_info in data["products"]:
        product_id = product_info.get("product_id")
        flavors = product_info.get("flavors", {})
        
        for flavor, qty in flavors.items():
            available_stock = db.get_flavor_stock(product_id, flavor)
            if qty > available_stock:
                flavor_display = localize_flavor(user_id, flavor)
                error_msg = get_text(user_id, "insufficient_stock_multiple").format(
                    flavor=flavor_display,
                    stock=available_stock,
                    qty=qty
                )
                bot.answer_callback_query(call.id, error_msg, show_alert=True)
                return

    place_text = get_text(user_id, f"order_place_{place}") if place else place
    contact_key = get_order_contact(place)
    contact_text = get_text(user_id, "order_contact_text").format(contact=get_text(user_id, contact_key))

    bot.answer_callback_query(call.id)
    
    # Расчитываем цены для всех товаров
    qty_unit = get_text(user_id, "order_quantity_unit")
    total_quantity = 0
    product_price = 0
    all_items_text = ""
    
    # Обрабатываем каждый товар в корзине
    for product_info in data["products"]:
        product_id = product_info.get("product_id")
        product = get_product_by_id(product_id)
        flavors = product_info.get("flavors", {})
        
        for flavor, qty in flavors.items():
            total_quantity += qty
            item_price = qty * PRICES.get(product_id, 8)
            product_price += item_price
            
            flavor_display = localize_flavor(user_id, flavor)
            all_items_text += f"- {product['name']} ({flavor_display}): {qty} {qty_unit} ({item_price}€)\n"
    
    delivery_price = get_delivery_price(place)
    total_price = product_price + delivery_price
    
    # Сохраняем один заказ со ВСЕМИ товарами
    all_flavors_str = ""
    for product_info in data["products"]:
        product_id = product_info.get("product_id")
        product = get_product_by_id(product_id)
        flavors = product_info.get("flavors", {})
        
        for flavor, qty in flavors.items():
            flavor_display = localize_flavor(user_id, flavor)
            all_flavors_str += f"{product['name']} ({flavor_display}): {qty}\n"
    
    db.add_user(user_id)
    order_id = db.add_order(
        user_id=user_id,
        product="Комбо заказ" if len(data["products"]) > 1 else get_product_by_id(data["products"][0]["product_id"])["name"],
        product_id=",".join([p["product_id"] for p in data["products"]]),
        flavors=all_flavors_str.strip(),
        place=place_text,
        quantity=total_quantity,
        total_price=total_price
    )
    
    # Формируем финальное сообщение
    delivery_text = "FREE" if delivery_price == 0 else f"{delivery_price}€"
    
    final_text = f"✅ {get_text(user_id, 'cart_title')}\n"
    final_text += f"{'='*30}\n\n"
    final_text += all_items_text + "\n"
    final_text += f"📦 {get_text(user_id, 'total_items').format(count=total_quantity)}\n"
    final_text += f"📍 {get_text(user_id, 'order_choose_place').split(chr(58))[0]}: {place_text}\n\n"
    final_text += f"💰 {get_text(user_id, 'total_sum').split(chr(58))[0]}:\n"
    final_text += f"  • Товары: {product_price}€\n"
    final_text += f"  • Доставка: {delivery_text}\n"
    final_text += f"  • Итого: {total_price}€\n\n"
    final_text += contact_text

    bot.edit_message_text(
        final_text,
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=order_complete_keyboard(user_id)
    )
    user_order_session.pop(user_id, None)


@bot.callback_query_handler(func=lambda call: call.data == "nolink")
def nolink(call):
    user_id = call.message.chat.id
    bot.answer_callback_query(call.id, get_text(user_id, "coming_soon_text"), show_alert=False)

@bot.callback_query_handler(func=lambda call: call.data.startswith("category:"))
def show_category(call):
    user_id = call.message.chat.id
    category = call.data.split(":")[1]
    items = PRODUCTS.get(category, [])
    kb = InlineKeyboardMarkup()
    for item in items:
        # Проверяем наличие остатков вкусов
        has_stock = any(db.get_flavor_stock(item['id'], flavor) > 0 for flavor in item.get("flavors", []))
        status = "✅" if has_stock else "❌"
        kb.add(InlineKeyboardButton(f"{status} {item['name']}", callback_data=f"item:{item['id']}:{category}"))
    kb.add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="main_menu"))
    category_name = get_text(user_id, f"category_{category}")
    bot.edit_message_text(
        f"{get_text(user_id, 'category_prefix')}{category_name}\n{get_text(user_id, 'choose_item')}",
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=kb
    )
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda call: call.data.startswith("item:"))
def show_item_flavors(call):
    user_id = call.message.chat.id
    parts = call.data.split(":")
    item_id = parts[1]
    category = parts[2]
    items = PRODUCTS.get(category, [])
    item = next((i for i in items if i["id"] == item_id), None)
    if not item:
        bot.answer_callback_query(call.id, get_text(user_id, "product_not_found"))
        return
    kb = InlineKeyboardMarkup()
    for flavor in item["flavors"]:
        flavor_with_stock = format_flavor_for_stock_view(user_id, item['id'], flavor)
        kb.add(InlineKeyboardButton(flavor_with_stock, callback_data="none"))
    kb.add(InlineKeyboardButton(get_text(user_id, "back_catalog"), callback_data=f"category:{category}"))
    kb.add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="main_menu"))
    bot.edit_message_text(
        f"{item['name']}\n\n{get_text(user_id, 'choose_flavor')}",
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=kb
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == "personal_cabinet")
def show_personal_cabinet(call):
    """
    Обработчик для отображения личного кабинета пользователя
    Показывает количество заказов и сумму всех заказов
    """
    user_id = call.message.chat.id
    
    # Получаем количество заказов из БД
    completed_count = db.get_completed_deals_count(user_id)
    pending_count = db.get_pending_orders_count(user_id)
    
    # Получаем все подтвержденные заказы для расчета суммы
    confirmed_orders = db.get_user_confirmed_orders(user_id)
    total_amount = 0
    for order in confirmed_orders:
        order_total = order.get('total_price', 0)
        if order_total == 0:
            # Для старых заказов, если total_price не сохранен
            product_price = order['quantity'] * PRICES.get(order.get('product_id', 'snus1'), 8)
            delivery_price = extract_delivery_price_from_text(order['place'])
            order_total = product_price + delivery_price
        total_amount += order_total
    
    # Формируем текст сообщения
    cabinet_text = f"{get_text(user_id, 'personal_cabinet_title')}\n\n"
    
    if completed_count == 0:
        cabinet_text += f"{get_text(user_id, 'no_orders')}\n\n"
    else:
        cabinet_text += f"{get_text(user_id, 'orders_completed').format(count=completed_count)}\n"
        cabinet_text += f"{get_text(user_id, 'orders_sum').format(sum=total_amount)}\n\n"
    
    # Добавляем информацию о ожидающих заказах
    if pending_count > 0:
        cabinet_text += f"⏳ Ожидающих заказов: {pending_count}"
    
    # Создаём клавиатуру с кнопкой возврата
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="main_menu"))
    
    # Редактируем сообщение
    bot.edit_message_text(
        cabinet_text,
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=kb
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == "show_managers")
def show_managers(call):
    user_id = call.message.chat.id
    managers_text = get_text(user_id, "managers_text").format(contact=ORDER_CONTACT)
    bot.edit_message_text(
        managers_text,
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=managers_keyboard(user_id)
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data == "referral_system")
def show_referral_system(call):
    """Показать информацию о реферальной системе"""
    user_id = call.message.chat.id
    
    referral_text = f"{get_text(user_id, 'referral_title')}\n\n{get_text(user_id, 'referral_text')}"
    
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton(get_text(user_id, "back_menu"), callback_data="main_menu"))
    
    bot.edit_message_text(
        referral_text,
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=kb
    )
    bot.answer_callback_query(call.id)


@bot.message_handler(commands=["catalog"])
def cmd_catalog(message):
    user_id = message.chat.id
    # Если язык не выбран, показываем выбор языка
    if user_id not in user_languages:
        msg = send_tracked_message(
            user_id,
            LANGUAGES["ru"]["language_select"],
            reply_markup=language_keyboard()
        )
        track_message(user_id, msg.message_id)
    else:
        msg = send_tracked_message(
            user_id,
            get_text(user_id, "main_menu"),
            reply_markup=main_menu_keyboard(user_id)
        )
        track_message(user_id, msg.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "catalog")
def show_catalog(call):
    user_id = call.message.chat.id
    catalog_text = get_text(user_id, "catalog").format(contact=ORDER_CONTACT)
    bot.edit_message_text(
        catalog_text,
        chat_id=user_id,
        message_id=call.message.message_id,
        reply_markup=catalog_keyboard(user_id)
    )
    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("product:"))
def show_product(call):
    user_id = call.message.chat.id
    product_id = call.data.split(":")[1]
    product = PRODUCTS.get(product_id)

    if not product:
        bot.answer_callback_query(call.id, get_text(user_id, "product_not_found"))
        return

    stock_status = get_text(user_id, "in_stock") if product["in_stock"] else get_text(user_id, "out_of_stock")
    flavors_text = "\n".join(f"  {localize_flavor(user_id, f)}" for f in product["flavors"])
    text = (
        f"{product['name']}\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"📝 {product['description']}\n\n"
        f"🍬 {get_text(user_id, 'choose_flavor')}\n{flavors_text}\n\n"
        f"💰 Цена: {product['price']}\n"
        f"📦 Статус: {stock_status}"
    )

    # Создаем клавиатуру в зависимости от наличия товара
    if product["in_stock"]:
        keyboard = product_keyboard(product_id, user_id)
    else:
        # Если товара нет в наличии, показываем только кнопку назад
        kb = InlineKeyboardMarkup()
        kb.add(InlineKeyboardButton(get_text(user_id, "back_catalog"), callback_data="catalog"))
        keyboard = kb

    if product.get("photo_url"):
        try:
            bot.delete_message(user_id, call.message.message_id)
            bot.send_photo(
                user_id,
                photo=product["photo_url"],
                caption=text,
                reply_markup=keyboard
            )
        except Exception:
            bot.send_message(user_id, text, reply_markup=keyboard)
    else:
        try:
            bot.edit_message_text(
                text,
                chat_id=user_id,
                message_id=call.message.message_id,
                reply_markup=keyboard
            )
        except Exception:
            bot.send_message(user_id, text, reply_markup=keyboard)

    bot.answer_callback_query(call.id)


@bot.callback_query_handler(func=lambda call: call.data.startswith("order:"))
def handle_order(call):
    user_id = call.message.chat.id
    product_id = call.data.split(":")[1]
    product = PRODUCTS.get(product_id)

    text = get_text(user_id, "order_text").format(
        product=product['name'],
        contact=ORDER_CONTACT
    )

    keyboard = back_keyboard(product_id, user_id)

    try:
        bot.edit_message_caption(
            caption=text,
            chat_id=user_id,
            message_id=call.message.message_id,
            reply_markup=keyboard
        )
    except Exception:
        try:
            bot.edit_message_text(
                text,
                chat_id=user_id,
                message_id=call.message.message_id,
                reply_markup=keyboard
            )
        except Exception:
            bot.send_message(user_id, text, reply_markup=keyboard)

    bot.answer_callback_query(call.id)


# ==================== ЗАПУСК ====================
print("🤖 Бот запущен! Нажмите Ctrl+C для остановки.")
bot.infinity_polling()
