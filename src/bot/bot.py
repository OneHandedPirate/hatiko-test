import asyncio

from aiogram import Bot, Dispatcher

from src.bot.utils import set_menu_commands, bot_logger
from src.core.config import settings
from src.bot.handlers import main_router, info_router, check_router
from src.bot.middlewares import WhiteListMiddleware


async def main():
    bot_logger.info("Initializing bot...")
    bot = Bot(token=settings.tg_bot.token)
    dp = Dispatcher()

    dp.include_routers(main_router, info_router, check_router)

    dp.update.middleware(WhiteListMiddleware())

    await set_menu_commands(bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
