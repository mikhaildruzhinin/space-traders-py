from space_traders.clients.base import BaseClient


class SellOrdersClient(BaseClient):
    async def sell(self, ship_id: str, good: str, quantity: int):
        """Place a new sell order"""
        return await self._generate_request(
            method='POST',
            endpoint='/my/sell-orders',
            params={
                'shipId': ship_id,
                'good': good,
                'quantity': quantity,
            },
        )
