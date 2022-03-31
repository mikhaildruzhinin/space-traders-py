from space_traders.clients.base import BaseClient


class WarpJumpClient(BaseClient):
    # warp jump
    async def warp_jump(self, ship_id: str):
        """Claim a username and get a token"""
        return await self._generate_request(
            method='POST',
            endpoint=f'/my/warp-jumps',
            params={'shipId': ship_id},
        )
