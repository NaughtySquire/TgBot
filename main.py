from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="6844191624:AAESVrUo7DVg98trqQX0ZJdrnTJihGi4GGU")
dispather = Dispatcher(bot)

@dispather.message_handler()
async def handle_message(message: types.Message):
    await message.answer(message.text)

executor.start_polling(dispather, skip_updates=True)
