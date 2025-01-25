import asyncio

from aiogram import Router, F
from aiogram import types

from src.bot.utils import delete_message, Keyboards


router = Router()


@router.callback_query(F.data == "info")
async def about_bot(callback: types.CallbackQuery):
    asyncio.create_task(delete_message(callback.message))

    info: str = (
        "Простой бот проверки IMEI\n"
        "Предоставляет информацию о модели телефона и стране продажи\n\n"
        "Создан в рамках тестового задания для компании Хатико-техника."
    )

    await callback.message.answer(info, reply_markup=Keyboards.get_back_to_main_kbd())
