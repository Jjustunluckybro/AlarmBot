from aiogram import types
from pydantic import ValidationError

from src.requests.users import write_new_user
from src.utils.exception import RequestException


async def start(msg: types.message) -> None:
    username = msg.from_user.username
    user_id = str(msg.from_user.id)
    try:
        await write_new_user(user_id, username)
    except RequestException as err:
        ...
    except ValidationError as err:
        ...

    await msg.answer("hi, to open menu, use command '/menu'")
    