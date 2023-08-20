from json import JSONDecodeError

from src.data.config import BACKEND_HOST
from src.models.ThemeModel import ThemeModel, ThemeModelToWrite

from logging import getLogger
import json

from src.requests.RequestHandler import RequestHandler, IRequestHandler, ResponseModel
from src.data import statuses
from src.utils.exception import RequestException, ResponseValidationException

module = "themes"
logger = getLogger(f"app.requests.{module}")


async def get_all_user_themes(user_id) -> list[ThemeModel]:
    """
    Make request to find all themes that belong to user with input id
    if no themes belong user, return empty list
    :param user_id: user telegram id
    :return: list of ThemeModel
    """
    url = f"{module}/get_all_themes_by_condition"
    body = {
        "links": {
            "user_id": str(user_id)
        }
    }
    request_handler: IRequestHandler = RequestHandler(BACKEND_HOST, module)
    r: ResponseModel = await request_handler.post(url, body)

    if r.status == statuses.NOT_FOUND_404:
        return []
    elif r.status != statuses.SUCCESS_200:
        logger.error(f"POST/ {url} status: {r.status}. details: {r.body}")
        raise RequestException(r.status, r.body)

    try:
        details: dict = json.loads(r.body)
    except JSONDecodeError:
        logger.error(f"POST/ invalid response {url}, unexpected body: {body}")
        raise ResponseValidationException(r.status, "POST", status=r.status, body=r.body, url=url)

    themes = []
    for theme in details:
        themes.append(ThemeModel.model_validate(theme))
    return themes


async def add_new_theme(theme: ThemeModelToWrite) -> str:
    """
    Make request to write new theme in db
    :param theme:
    :return: theme id
    """
    url = f"{module}/create_theme"
    request_handler = RequestHandler(BACKEND_HOST, module)
    r: ResponseModel = await request_handler.post(url, theme.model_dump())

    if r.status != statuses.CREATED_201:
        logger.error(f"POST/ {url} status: {r.status}. details: {r.body}")
        raise RequestException(r.status, r.body)

    return r.body


async def delete_theme(theme_id: str) -> str:
    """

    :param theme_id:
    :return:
    """
    url = f"{module}/delete_theme/{theme_id}"
    request_handler = RequestHandler(BACKEND_HOST, module)
    r: ResponseModel = await request_handler.delete(url)

    if r.status != statuses.SUCCESS_200:
        logger.error(f"DELETE/ {url} status: {r.status}. details: {r.body}")
        raise RequestException(r.status, r.body)

    return r.body
