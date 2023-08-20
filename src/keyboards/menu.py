from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.models.ThemeModel import ThemeModel

from src.data import callback_answers


async def create_user_themes_keyboard(user_themes: list[ThemeModel]) -> InlineKeyboardBuilder:

    builder = InlineKeyboardBuilder()

    if not user_themes:
        builder.button(text="Создать новую тему", callback_data=callback_answers.ADD_THEME)
        return builder

    for theme in user_themes:
        builder.button(text=theme.name, callback_data=callback_answers.open_theme(theme.id))

    builder.button(text="Создать новую тему", callback_data=callback_answers.ADD_THEME)
    builder.button(text="Удалить тему", callback_data=callback_answers.DELETE_THEME)

    builder.adjust(1, True)

    return builder
