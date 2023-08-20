from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.data import callback_answers


def create_finish_inline_keyboard(name: str = "") -> InlineKeyboardBuilder:
    """

    :param name: name of modul to finish, will show to ui in button
    :return:
    """
    builder = InlineKeyboardBuilder()
    builder.button(text=f"Завершить {name}", callback_data=callback_answers.FINISH_STATE)

    return builder
