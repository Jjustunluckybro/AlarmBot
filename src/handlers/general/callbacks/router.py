from aiogram import Router

from src.data import callback_answers
from src.handlers.general.callbacks.finish_state import finish_state


def prepare_general_callbacks_router() -> list[Router]:
    router = Router(name="router_general_callbacks")

    router.callback_query.register(finish_state, lambda x: x.data == callback_answers.FINISH_STATE)
    routers = [
        router
    ]

    return routers
