from aiogram import types

from src.keyboards.menu import create_user_themes_keyboard
from src.requests.themes import get_all_user_themes


async def menu(msg: types.message) -> None:
    user_id = msg.from_user.id
    user_themes = await get_all_user_themes(user_id)
    keyboard = await create_user_themes_keyboard(user_themes)
    await msg.answer(text="Меню", reply_markup=keyboard.as_markup())
