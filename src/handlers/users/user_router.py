from aiogram import Router
from src.handlers.users.callbacks.routers import prepare_user_callbacks_routers
from src.handlers.users.comands import prepare_user_commands_router


def prepare_all_user_routers() -> list[Router]:
    """
    Collect all user routers
    :return: list of all routers
    """
    # Append user commands router
    routers = [prepare_user_commands_router()]

    # Append all user callbacks routers
    routers += prepare_user_callbacks_routers()

    return routers
