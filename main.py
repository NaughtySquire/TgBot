import asyncio
from random import randint
from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile

token = "6844191624:AAESVrUo7DVg98trqQX0ZJdrnTJihGi4GGU"
dispather = Dispatcher()

@dispather.message()
async def handle_message(message: types.Message):
    photo = FSInputFile(f"Magic 8 ball/{randint(1, 20)}.jpg")
    await message.answer_photo(photo)

async def main() -> None:
    bot = Bot(token)
    await dispather.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
