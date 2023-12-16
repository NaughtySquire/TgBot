import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold


token = "6844191624:AAESVrUo7DVg98trqQX0ZJdrnTJihGi4GGU"
dispather = Dispatcher()

@dispather.message()
async def handle_message(message: types.Message):
    arr = ["mem.png"]
    photo = FSInputFile(random.choice(arr))
    await message.answer_photo(photo)

async def main() -> None:
    bot = Bot(token)
    await dispather.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())