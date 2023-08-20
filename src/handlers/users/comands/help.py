from aiogram import types


async def help(msg: types.message) -> None:
    text = """
    Используйте команду '/menu', чтобы открыть список своих тем, удалить или создать новые
    """
    await msg.answer(text)
