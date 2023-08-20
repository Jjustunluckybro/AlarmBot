from pydantic import ValidationError

from src.models.UserModel import UserModel

from src.data.config import BACKEND_HOST
from src.requests.RequestHandler import IRequestHandler, RequestHandler, ResponseModel
from src.data import statuses
from src.utils.exception import RequestException, ResponseValidationException

from logging import getLogger

module = "users"
logger = getLogger(f"app.requests.{module}")


async def get_user(user_id) -> UserModel:
    url = f"users/get_user/{user_id}"
    request_handler: IRequestHandler = RequestHandler(BACKEND_HOST, module)
    r: ResponseModel = await request_handler.get(url)

    details = r.body
    if r.status == statuses.SUCCESS_200:
        try:
            return UserModel.model_validate_json(details)
        except ValidationError as err:
            raise ResponseValidationException(r.status, "GET", url=url, status=r.status, body=details)
    else:
        logger.error(f"GET/ {url} - status: {r.status}. details: {details}")
        raise RequestException(r.status, details)


async def write_new_user(user_id: str, username: str) -> None:
    user = UserModel(
        telegram_id=user_id,
        user_name=username
    )
    url = f"users/create_user"
    request_handler: IRequestHandler = RequestHandler(BACKEND_HOST, module)
    r: ResponseModel = await request_handler.post(url, user.model_dump())

    details = r.body
    if r.status == statuses.CONFLICT_409:
        logger.info(f"POST/ {url} - user already exist")
        return
    elif r.status == statuses.CREATED_201:
        logger.info(f"POST/ {url} - user created")
        return
    else:
        logger.error(f"POST/ {url} - status: {r.status}. details: {details}")
        raise RequestException(r.status, details)
