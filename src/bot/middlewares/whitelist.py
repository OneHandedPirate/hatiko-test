from aiogram import BaseMiddleware
from aiogram.types import Update

from src.core.config import settings
from src.bot.utils import bot_logger


class WhiteListMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Update, data: dict):
        user_id = None

        if event.message:
            user_id = event.message.from_user.id
        elif event.callback_query:
            user_id = event.callback_query.from_user.id
        elif event.inline_query:
            user_id = event.inline_query.from_user.id

        if (user_id and user_id not in settings.tg_bot.allowed_users) or not user_id:
            bot_logger.info("Unauthorized user tried to access bot: %s", user_id)
            await event.message.answer("В доступе отказано, извините :(")
            return None
        return await handler(event, data)
