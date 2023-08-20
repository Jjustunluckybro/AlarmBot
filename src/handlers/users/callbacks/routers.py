from aiogram import Router
from .themes import prepare_theme_callback_router


def prepare_user_callbacks_routers() -> list[Router]:
    routers = []

    routers += prepare_theme_callback_router()

    return routers
