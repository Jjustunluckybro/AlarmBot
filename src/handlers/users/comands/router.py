from aiogram import Router
from aiogram.filters import CommandStart, Command

from . import menu, start, help


def prepare_user_commands_router() -> Router:

    user_command_router = Router(name="router_user_command")

    user_command_router.message.register(start, CommandStart())
    user_command_router.message.register(menu, Command("menu"))
    user_command_router.message.register(help, Command("help"))

    return user_command_router
