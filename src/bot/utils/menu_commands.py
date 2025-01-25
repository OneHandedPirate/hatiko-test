from aiogram import Bot
from aiogram.types import BotCommand


async def set_menu_commands(bot: Bot):
    """Add menu commands to bot"""
    commands = [
        BotCommand(command="/start", description="Начни с этой команды"),
    ]

    await bot.set_my_commands(commands)
