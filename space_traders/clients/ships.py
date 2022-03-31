from space_traders.clients.base import BaseClient


class ShipsClient(BaseClient):
    async def buy_ship(self, location: str, type: str):
        """Buy a new ship"""
        return await self._generate_request(
            method='POST',
            endpoint='/my/ships',
            params={
                'location': location,
                'type': type,
            },
        )

    async def get_user_ship(self, ship_id: str):
        """Get your ship info"""
        return await self._generate_request(
            method='GET',
            endpoint=f'/my/ships/{ship_id}',
        )

    async def get_user_ships(self):
        """Get your ships"""
        return await self._generate_request(
            method='GET',
            endpoint='/my/ships',
        )

    async def jettison_cargo(self, ship_id: str, good: str, quantity: int):
        """Jettison cargo"""
        return await self._generate_request(
            method='POST',
            endpoint=f'/my/ships/{ship_id}/jettison',
            params={
                'shipId': ship_id,
                'good': good,
                'quantity': quantity,
            },
        )

    async def scrap_ship(self, ship_id: str):
        """Scrap your ship for credits"""
        return await self._generate_request(
            method='DELETE',
            endpoint=f'/my/ships/{ship_id}',
        )

    async def transfer_cargo(self, from_ship_id: str, to_ship_id: str, good: str, quantity: int):
        """Transfer cargo between ships"""
        return await self._generate_request(
            method='POST',
            endpoint=f'/my/ships/{from_ship_id}/transfer',
            params={
                'toShipId': to_ship_id,
                'good': good,
                'quantity': quantity,
            },
        )
