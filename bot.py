
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from flask import Flask, request

# Инициализация Flask
app = Flask(__name__)

# Инициализация Telegram Bot API
TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # URL вашего Vercel-деплоя
application = ApplicationBuilder().token(TOKEN).updater(None).build()

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Я бот, работающий через Vercel.")

# Регистрируем обработчик команды
application.add_handler(CommandHandler("start", start))

# Flask маршрут для вебхуков
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    request_data = request.get_json(force=True)
    update = Update.de_json(request_data, application.bot)
    application.process_update(update)
    return "OK", 200

# Запуск приложения
if __name__ == "__main__":
    application.bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}")

'''
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Загрузка переменных окружения из .env (локально)
load_dotenv()

# Получение токена из переменной окружения
TOKEN = os.getenv("TELEGRAM_TOKEN")


# Обработка команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Привет! Я бот.")


# Создание и запуск бота
if __name__ == "__main__":
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
'''

