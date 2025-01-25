import asyncio


import aiohttp
from aiogram import Router, F
from aiogram import types
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from src.bot.utils import delete_message, Keyboards, validate_imei, bot_logger
from src.core.config import settings


router = Router()


class ImeiCheckStates(StatesGroup):
    waiting_for_imei = State()


@router.callback_query(F.data == "check_imei")
async def check_imei_enter(callback_query: types.CallbackQuery, state: FSMContext):
    asyncio.create_task(delete_message(callback_query.message))

    await callback_query.message.answer(
        "Введите номер IMEI", reply_markup=Keyboards.get_back_to_main_kbd()
    )

    await state.set_state(ImeiCheckStates.waiting_for_imei)


@router.message(F.text, ImeiCheckStates.waiting_for_imei)
async def input_imei(message: types.Message, state: FSMContext):
    asyncio.create_task(delete_message(message))

    if not validate_imei(message.text):
        await message.answer(
            "Невалидный IMEI\n"
            "IMEI должен содержать 15 символов и включать только цифры\n\n"
            "Попробуйте еще раз или нажмите кнопку ниже для перехода в главное меню",
            reply_markup=Keyboards.get_back_to_main_kbd(),
        )
        return

    new_message = await message.answer("Ждем ответа...")

    try:
        async with aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=10)
        ) as aiohttp_session:
            body = {"imei": message.text, "token": settings.api.token}

            res = await aiohttp_session.post(
                f"{settings.api.protocol}://{settings.api.host}:{settings.api.port}/api/check-imei",
                json=body,
            )

            json_response = await res.json()

            if res.status == 400:
                await new_message.edit_text(
                    json_response.get("detail"),
                    reply_markup=Keyboards.get_after_check_kbd(),
                )
                await state.clear()
                return

            if res.status != 200:
                raise Exception("Invalid API response")


            await new_message.edit_text(
                f"Информация:\n\n"
                f"📱 Модель: {json_response.get('properties')['deviceName']}\n"
                f"🌏 Страна продажи: {json_response.get('properties')['purchaseCountry']}",
                reply_markup=Keyboards.get_after_check_kbd(),
            )

            await state.clear()
    except Exception as e:
        bot_logger.exception(
            "Exception occurred while fetching IMEI data: %s", str(e), exc_info=True
        )
        await new_message.edit_text(
            "Что то пошло не так.\n"
            "Попробуйте ввести IMEI еще раз или нажмите кнопку "
            "ниже для перехода в главное меню",
            reply_markup=Keyboards.get_back_to_main_kbd(),
        )
