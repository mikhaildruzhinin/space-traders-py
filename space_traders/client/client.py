import asyncio
from typing import (
    Dict,
    Union,
)

import aiohttp

from space_traders.client.request_factory import RequestFactory


class Client:
    __base_url = 'https://api.spacetraders.io'

    def __init__(
        self,
        request_factory: RequestFactory,
    ):
        self.request_factory = request_factory

    @property
    def base_url(self):
        return self.__base_url

    async def get_status(
        self,
    ) -> Dict[str, Union[int, str]]:
        return await self.request_factory.generate(
            method='get',
            endpoint='/game/status'
        )

    async def claim_username(
        self,
        username: str
    ) -> Dict[str, Union[int, str]]:
        return await self.request_factory.generate(
            method='post',
            endpoint=f'/users/{username}/claim'
        )

    async def get_account_info(
        self
    ) -> Dict[str, Union[int, str]]:
        return await self.request_factory.generate(
            method='get',
            endpoint=f'/my/account'
        )

    async def get_loans(
        self
    ) -> Dict[str, Union[int, str]]:
        return await self.request_factory.generate(
            method='get',
            endpoint=f'/types/loans'
        )

    async def take_loan(
        self,
        type: str,
    ) -> Dict[str, Union[int, str]]:
        return await self.request_factory.generate(
            method='post',
            endpoint='/my/loans',
            params={'type': type}
        )
