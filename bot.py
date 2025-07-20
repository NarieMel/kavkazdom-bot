from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# 🔐 ВСТАВЬ СЮДА СВОЙ ТОКЕН
TOKEN = '8120091186:AAEj6kDMpwdlhhCylbNbWieAjH64uCXaes4'

# 👋 Приветствие + главное меню
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["📦 Каталог", "📞 Контакты"],
                ["📐 Размеры", "🛒 Заказать"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    welcome_text = (
        "👋 Добро пожаловать в магазин Kavkazdom!\n\n"
        "Мы создаём сценические, свадебные и этнические костюмы народов Кавказа.\n"
        "Выберите нужный раздел ниже 👇"
    )
    await update.message.reply_text(welcome_text, reply_markup=reply_markup)

# 📞 Контакты
async def contacts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Контакты:\n"
        "Телефон: +7 999 999-99-99\n"
        "Instagram: @nariemelikishvili\n"
        "Сайт: www.kavkazdom.ru"
    )

# 📐 Размерная таблица
async def size(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📏 Размерная таблица:\n[Здесь будет ссылка или изображение]")

# 🛒 Как заказать
async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📝 Чтобы оформить заказ, пришлите:\n"
        "1. Название товара\n"
        "2. Размер\n"
        "3. Количество\n"
        "4. Ваше имя и номер телефона"
    )

# 🎛 Обработка нажатий на кнопки
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    # Контакты
    if text == "📞 контакты":
        await contacts(update, context)

    # Размеры
    elif text == "📐 размеры":
        await size(update, context)

    # Заказать
    elif text == "🛒 заказать":
        await order(update, context)

    # Каталог — показать кнопки разделов
    elif text == "📦 каталог":
        keyboard = [["Мужская одежда", "Женская одежда"],
                    ["Детская одежда", "Аксессуары"],
                    ["🔙 Назад в меню"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("📂 Выберите раздел каталога:", reply_markup=reply_markup)

    # Категория: Мужская одежда
    elif text == "мужская одежда":
        keyboard = [["🔙 Назад в меню"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("🧥 Мужская одежда:\n- Черкески\n- Башлыки\n- Пояса", reply_markup=reply_markup)

    # Категория: Женская одежда
    elif text == "женская одежда":
        keyboard = [["🔙 Назад в меню"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("👗 Женская одежда:\n- Платья\n- Пояса\n- Шапочки", reply_markup=reply_markup)

    # Категория: Детская одежда
    elif text == "детская одежда":
        keyboard = [["🔙 Назад в меню"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("🧒 Детская одежда:\n- Мини-костюмы\n- Аксессуары", reply_markup=reply_markup)

    # Категория: Аксессуары
    elif text == "аксессуары":
        keyboard = [["🔙 Назад в меню"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("🎀 Аксессуары:\n- Пояса\n- Украшения\n- Ткани", reply_markup=reply_markup)

    # 🔙 Назад в меню — главное меню
    elif text == "🔙 назад в меню":
        keyboard = [["📦 Каталог", "📞 Контакты"],
                    ["📐 Размеры", "🛒 Заказать"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("🔙 Вы вернулись в главное меню:", reply_markup=reply_markup)

    # Неизвестный ввод
    else:
        await update.message.reply_text("🤖 Не поняла. Напишите /start или выберите из меню.")


# 🚀 Запуск бота
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("contacts", contacts))
app.add_handler(CommandHandler("order", order))
app.add_handler(CommandHandler("size", size))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
