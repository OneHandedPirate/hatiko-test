from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Keyboards:
    BUTTONS = {
        "info": types.InlineKeyboardButton(text="Информация", callback_data="info"),
        "back_to_main": types.InlineKeyboardButton(
            text="В главное меню", callback_data="back_to_main"
        ),
        "check_imei": types.InlineKeyboardButton(
            text="Проверить IMEI", callback_data="check_imei"
        ),
        "check_another": types.InlineKeyboardButton(
            text="Проверить еще один", callback_data="check_imei"
        ),
    }

    @classmethod
    def build_kbd(cls, *args: str, max_width: int = 1):
        if not all(btn in cls.BUTTONS for btn in args):
            raise ValueError("Invalid button(s) passed")

        builder = InlineKeyboardBuilder()
        builder.max_width = max_width
        builder.add(*[cls.BUTTONS[btn] for btn in args])

        return builder.as_markup()

    @classmethod
    def get_main_menu_kbd(cls):
        return cls.build_kbd("info", "check_imei", max_width=2)

    @classmethod
    def get_back_to_main_kbd(cls):
        return cls.build_kbd("back_to_main")

    @classmethod
    def get_after_check_kbd(cls):
        return cls.build_kbd("check_another", "back_to_main")
