from typing import (
    Dict,
    Optional,
)

import aiohttp


class RequestFactory:
    def __init__(
        self,
        session: aiohttp.ClientSession
    ):
        self.__methods = {
            'GET': session.get,
            'POST': session.post,
            'PUT': session.put,
            'DELETE': session.delete,
        }

    async def generate(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, str]] = None,
    ):
        if not params:
            params = {}
        async with self.__methods[method](endpoint, params=params) as response:
            return {
                'status_code': response.status,
                'response': await response.json()
            }
