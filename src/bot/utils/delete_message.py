import asyncio
from contextlib import suppress

from aiogram import types
from aiogram.exceptions import TelegramNotFound, TelegramBadRequest


async def delete_message(message: types.Message, sleep_time: int = 0):
    """Delete message"""
    await asyncio.sleep(sleep_time)
    with suppress(TelegramNotFound, TelegramBadRequest):
        await message.delete()
