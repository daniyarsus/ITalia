import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Инициализация бота и диспетчера
API_TOKEN = '6301690899:AAFiJMovTcKcxQGcFK3b4EV7-1iMPnC5vEk'  # Замените 'YOUR_BOT_TOKEN' на ваш токен
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Настройка логгирования
logging.basicConfig(level=logging.INFO)

# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привет! Я бот, созданный с помощью aiogram.\nНапишите /help, чтобы узнать больше.")

# Обработчик команды /help
@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    help_text = "Этот бот просто отвечает на команды /start и /help.\n\n"
    help_text += "Команды:\n"
    help_text += "/start - Начать взаимодействие\n"
    help_text += "/help - Получить справку\n"
    await message.answer(help_text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
