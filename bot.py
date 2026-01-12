# bot.py - основной файл бота
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os

# Получаем токен из переменной окружения
TOKEN = os.getenv("TOKEN")

# Функция, которая срабатывает на команду /start
async def start(update, context):
    await update.message.reply_text("Привет! Я работаю! 🎉")

# Функция, которая отвечает на любое сообщение
async def echo(update, context):
    await update.message.reply_text(f"Вы сказали: {update.message.text}")

# Главная функция
def main():
    # Создаем бота
    app = Application.builder().token(TOKEN).build()
    
    # Регистрируем команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, echo))
    
    # Запускаем бота
    print("Бот запущен! 🚀")
    app.run_polling()

if __name__ == '__main__':

    main()
