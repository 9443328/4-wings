import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, Update
from aiohttp import web

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

MY_TEXT = "Great. Now take the parameters from the previous image, multiply them together, multiply the result by 4, and then add .github.io."

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(MY_TEXT)

@dp.message(F.text)
async def any_text(message: Message):
    await message.answer(MY_TEXT)


async def handle_webhook(request):
    url = str(request.url)
    if request.method == "POST":
        json_data = await request.json()
        update = Update.model_validate(json_data, context={"bot": bot})
        await dp.feed_update(bot, update)
        return web.Response(text="ok")
    return web.Response(text="Method Not Allowed", status=405)

app = web.Application()
app.router.add_post("/api/webhook", handle_webhook)

