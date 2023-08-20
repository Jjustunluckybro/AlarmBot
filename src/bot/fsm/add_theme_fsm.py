from aiogram.fsm.state import StatesGroup, State


class AddTheme(StatesGroup):
    write_theme_name = State()
    write_theme_description = State()

