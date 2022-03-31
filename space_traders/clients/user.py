from space_traders.clients.base import BaseClient


class UserClient(BaseClient):
    # user
    async def claim_username(self, username: str):
        """Claim a username and get a token"""
        return await self._generate_request(
            method='POST',
            endpoint=f'/users/{username}/claim',
        )
