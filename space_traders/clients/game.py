from space_traders.clients.base import BaseClient


class GameClient(BaseClient):
    async def get_game_status(self):
        """Use to determine whether the server is alive"""
        return await self._generate_request(
            method='GET',
            endpoint='/game/status',
        )
