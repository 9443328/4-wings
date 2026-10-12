import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message


TOKEN = "8461181717:AAH3zf9IBJS04kiXDPi6ocO1f9A5f8AbK7k"

bot = Bot(token=TOKEN)
dp = Dispatcher()

MY_TEXT = "Great. Now take the parameters from the previous image, multiply them together, multiply the result by 4, and then add .github.io."

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(MY_TEXT)

@dp.message(F.text)
async def any_text(message: Message):
    await message.answer(MY_TEXT)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
