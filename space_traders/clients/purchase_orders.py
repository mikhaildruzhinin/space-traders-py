from space_traders.clients.base import BaseClient


class PurchaseOrdersClient(BaseClient):
    async def purchase(self, ship_id: str, good: str, quantity: int):
        """Place a new purchase order"""
        return await self._generate_request(
            method='POST',
            endpoint='/my/purchase-orders',
            params={
                'shipId': ship_id,
                'good': good,
                'quantity': quantity,
            },
        )
