from space_traders.clients.base import BaseClient


class LeaderboardClient(BaseClient):
    async def get_leaderboard(self):
        """Use to see the current net worth of the top players"""
        return await self._generate_request(
            method='GET',
            endpoint='/game/leaderboard/net-worth',
        )
