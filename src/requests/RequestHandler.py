from abc import ABC, abstractmethod
from logging import getLogger

from aiogram.client.session import aiohttp
from pydantic import BaseModel


class ResponseModel(BaseModel):
    body: str
    status: int


class IRequestHandler(ABC):

    @abstractmethod
    async def get(self, url: str) -> ResponseModel:
        """GET request"""
        raise NotImplemented

    @abstractmethod
    async def post(self, url: str, body: dict) -> ResponseModel:
        """POST request"""
        raise NotImplementedError

    @abstractmethod
    async def patch(self, url: str, body: dict) -> ResponseModel:
        """PATCH request"""
        raise NotImplementedError

    @abstractmethod
    async def delete(self, url: str, body: dict) -> ResponseModel:
        raise NotImplementedError


class RequestHandler(IRequestHandler):

    def __init__(self, host: str, module: str):
        """

        :param host: backend host
        :param module: modul name to logger
        """
        self.logger = getLogger(f"app.request.{module}.RequestHandler")
        self.host = host

    async def get(self, url: str) -> ResponseModel:
        """"""
        url = f"{self.host}/{url}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                self.logger.info(f"GET/ send request - url: {url}")
                details: str = await r.text()
                status = r.status
                self.logger.info(f"GET/ get response - url: {url} - status: {r.status}. details: {details}")

        return ResponseModel(body=details, status=status)

    async def post(self, url: str, body: dict) -> ResponseModel:
        """"""
        url = f"{self.host}/{url}"

        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=body) as r:
                self.logger.info(f"POST/ send request - url: {url}")
                details: str = await r.text()
                status = r.status
                self.logger.info(f"POST/ get response - url: {url} - status: {r.status}. details: {details}")

        return ResponseModel(body=details, status=status)

    async def patch(self, url: str, body: dict) -> ResponseModel:
        """"""
        url = f"{self.host}/{url}"

        async with aiohttp.ClientSession() as session:
            async with session.patch(url, json=body) as r:
                self.logger.info(f"PATCH/ send request - url: {url}")
                details: str = await r.text()
                status = r.status
                self.logger.info(f"PATCH/ get response - url: {url} - status: {r.status}. details: {details}")

        return ResponseModel(body=details, status=status)

    async def delete(self, url: str, body: dict | None = None) -> ResponseModel:
        url = f"{self.host}/{url}"
        body = {} if body is None else body
        async with aiohttp.ClientSession() as session:
            async with session.delete(url, json=body) as r:
                self.logger.info(f"DELETE/ send request - url: {url}")
                details: str = await r.text()
                status = r.status
                self.logger.info(f"DELETE/ get response - url: {url} - status: {r.status}. details: {details}")

        return ResponseModel(body=details, status=status)
