from aiogram import types

from src.keyboards.menu import create_keyboard


async def menu(msg: types.message) -> None:
    keyboard = create_keyboard()
    await msg.answer(text="Меню", reply_markup=keyboard.as_markup())