from aiogram import Router

import src.handlers.users.comands as user_commands
import src.handlers.users.callbacks.themes as user_themes_callbacks
from src.handlers.general.routers import prepare_all_general_routers

from src.handlers.users.user_router import prepare_all_user_routers

from src.handlers.users.callbacks.themes.add_theme import router as router_add_theme
from src.handlers.users.callbacks.themes import prepare_theme_callback_router


def prepare_routers() -> list[Router]:
    """
    Collect all app routers and return it's as a list
    :return:
    """
    routers = []

    routers += prepare_all_user_routers()
    routers += prepare_all_general_routers()

    return routers
