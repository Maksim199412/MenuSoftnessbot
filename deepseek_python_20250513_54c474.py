from aiogram import Bot, Dispatcher, types, executor
import logging

# Настройки
API_TOKEN = 'ВАШ_ТОКЕН'  # ← Замените на свой!
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Меню
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "💖 *Меню на нежность и не только!*\n"
        "✨ Выберите действие:",
        reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
            .add("💝 Создать заказ")
            .add("📋 Моё меню", "📊 Мои долги"),
        parse_mode="Markdown"
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)