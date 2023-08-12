from typing import List

from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, KeyboardBuilder


def create_keyboard() -> InlineKeyboardBuilder:
    builder = InlineKeyboardBuilder()

    user_themes = ["Theme 1", "Theme 2", "Theme 3", "Theme 4", "Theme 5"]

    for theme in user_themes:
        builder.button(text=theme, callback_data=f"open_{theme}")

    builder.button(text="Создать новую тему", callback_data="add_theme")
    builder.button(text="Удалить тему", callback_data="del_theme")

    builder.adjust(1, True)

    return builder
