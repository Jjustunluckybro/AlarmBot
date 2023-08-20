from aiogram import Router

from src.handlers.general.callbacks.router import prepare_general_callbacks_router


def prepare_all_general_routers() -> list[Router]:
    routers = []
    routers += prepare_general_callbacks_router()
    return routers
