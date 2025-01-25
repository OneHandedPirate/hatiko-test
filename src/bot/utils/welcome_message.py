import asyncio

from aiogram import types

from src.bot.utils import delete_message, Keyboards
from src.core.config import BASE_DIR


async def send_welcome_message(message: types.Message | types.CallbackQuery):
    """
    Удаляет сообщение и отправляет приветствие с клавиатурой гл. меню
    """
    source_message = (
        message.message if isinstance(message, types.CallbackQuery) else message
    )
    asyncio.create_task(delete_message(source_message))

    image_path = f"{BASE_DIR}/src/bot/images/check.png"
    image = types.FSInputFile(image_path)

    await source_message.answer_photo(
        photo=image,
        caption="Добро пожаловать в бот проверки IMEI",
        reply_markup=Keyboards.get_main_menu_kbd(),
    )
