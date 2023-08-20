import logging
import asyncio
import sys
import src.handlers as handlers

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from src.data.config import BOT_TOKEN

logger = logging.getLogger('app.main')


def setup_handlers(dp: Dispatcher) -> None:
    routers = handlers.prepare_routers()
    logger.info(f"prepare routers: {[router.name for router in routers]}")
    dp.include_routers(*routers)


async def main():
    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    setup_handlers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped")
