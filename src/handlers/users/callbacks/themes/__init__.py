from aiogram import Router

from . import add_theme


def prepare_theme_callback_router() -> list[Router]:
    routers = []

    router_add_theme = add_theme.router
    routers.append(router_add_theme)

    return routers
