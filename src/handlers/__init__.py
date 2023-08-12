from aiogram import Router
from aiogram.filters import CommandStart, Command

import src.handlers.users.comands as user_commands


def prepare_routers() -> list[Router]:
    routers = []

    user_router = Router()

    user_router.message.register(user_commands.start.start, CommandStart())
    user_router.message.register(user_commands.menu.menu, Command("menu"))
    routers.append(user_router)

    return routers
