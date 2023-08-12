from aiogram import types


async def start(msg: types.message) -> None:
    await msg.answer("hi, to open menu, use command '/menu'")
    