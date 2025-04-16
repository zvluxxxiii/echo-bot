import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

TOKEN = "7784516018:AAGLtEIemEUQDGYnUoYxj9sDcGRiW3tpc5M"
GROUP_ID = -1002294772560

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

user_cache = {}

# Приветствие при /start
@dp.message(F.text, F.text.lower() == "/start")
async def handle_start(message: Message):
    await message.answer(
        "⋆｡°✩₊\n/ᐠ – ˕ –マ\n\n"
        "Привет. Это “Эхо с небес”.\n"
        "Если тебе тяжело — напиши.\n"
        "Мы не судим, не исправляем, не умничаем.\n"
        "Мы просто рядом.\n\n"
        "✩ ꒰՞•ﻌ•՞꒱\n"
        "Ты не один.\n"
        "Ты не одна.\n"
        "И это место — для тебя.\n\n"
        "⭒ﾟ･｡☆･｡\n"
        "Ответ может прийти не сразу,\n"
        "но тебя обязательно услышат.\n\n"
        "Чтобы написать конкретному админу,\n"
        "укажи хештег в конце сообщения — например: #мики"
    )

# ЛС → Админам
@dp.message(F.chat.type == "private", F.text)
async def forward_to_admins(message: Message):
    sent = await bot.send_message(
        GROUP_ID,
        f"✉️ Сообщение от @{message.from_user.username or 'без ника'} (ID: {message.from_user.id}):\n{message.text}"
    )
    user_cache[sent.message_id] = message.from_user.id

# Ответ админа → пользователю
@dp.message(F.chat.id == GROUP_ID, F.reply_to_message)
async def reply_from_admins(message: Message):
    original_id = message.reply_to_message.message_id
    if original_id in user_cache:
        user_id = user_cache[original_id]
        await bot.send_message(user_id, f"⋆｡°✩₊\n{message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
