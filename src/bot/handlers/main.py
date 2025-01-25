from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.context import FSMContext

from src.bot.utils import send_welcome_message


router = Router()


@router.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await state.clear()
    await send_welcome_message(message)


@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback_query: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await send_welcome_message(callback_query)
