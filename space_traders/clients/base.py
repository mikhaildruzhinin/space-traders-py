from abc import ABC
from typing import (
    Dict,
    Optional,
    Union,
)

import aiohttp


class BaseClient(ABC):
    def __init__(
        self,
        session: aiohttp.ClientSession,
    ):
        self._methods = {
            'GET': session.get,
            'POST': session.post,
            'PUT': session.put,
            'DELETE': session.delete,
        }

    @property
    def methods(self):
        return self._methods

    async def _generate_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Union[int, str]]] = None,
    ):
        """Generate HTTP request"""
        if not params:
            params = {}
        async with self.methods[method](endpoint, params=params) as response:
            return {
                'status_code': response.status,
                'response': await response.json()
            }
