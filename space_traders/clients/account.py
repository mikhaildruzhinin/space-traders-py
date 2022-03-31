from space_traders.clients.base import BaseClient


class AccountClient(BaseClient):
    async def get_account(self):
        """Get information on your account"""
        return await self._generate_request(
            method='GET',
            endpoint='/my/account'
        )
