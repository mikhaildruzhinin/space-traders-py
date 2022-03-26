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
        self.session = session
        self.methods = {
            'get': self.session.get,
            'post': self.session.post,
        }

    async def generate(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, str]] = None,
    ):
        if not params:
            params = {}
        async with self.methods[method](endpoint, params=params) as response:
            return {
                'status_code': response.status,
                'response': await response.json()
            }
