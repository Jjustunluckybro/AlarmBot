from pydantic import ValidationError

from src.models.UserModel import UserModel
import aiohttp

from src.data.config import BACKEND_HOST
from src.utils import statuses
from src.utils.exception import RequestException

from logging import getLogger

logger = getLogger("requests")


async def get_user(user_id) -> UserModel:
    url = f"{BACKEND_HOST}/users/get_user/{user_id}"
    logger.info(f"GET/ {url}")

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:

            details = await r.text()
            if r.status == statuses.SUCCESS_200:
                logger.info(f"GET Success {url}")
                try:
                    return UserModel.model_validate_json(details)
                except ValidationError as err:
                    logger.error(f"Validation error, body: {details}")
                    raise err
            else:
                logger.error(f"GET Failed {url} - status: {r.status}. details: {details}")
                raise RequestException(r.status, details)


async def write_new_user(user_id: str, username: str) -> None:
    user = UserModel(
        telegram_id=user_id,
        user_name=username
    )
    url = f"{BACKEND_HOST}/users/create_user"
    logger.info(f"POST/ {url}")

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=user.model_dump()) as r:

            details = await r.text()
            if r.status == statuses.CONFLICT_409:
                logger.info(f"POST Success {url} - user already exist")
                return
            elif r.status == statuses.CREATED_201:
                logger.info(f"POST Success {url} - user created")
                return
            else:
                logger.error(f"POST Failed {url} - status: {r.status}. details: {details}")
                raise RequestException(r.status, details)
