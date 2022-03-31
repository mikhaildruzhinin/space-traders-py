from space_traders.clients.base import BaseClient


class LocationsClient(BaseClient):
    async def get_location(self, location_symbol: str):
        """Get info on a location"""
        return await self._generate_request(
            method='GET',
            endpoint=f'/locations/{location_symbol}',
        )

    async def get_location_market(self, location_symbol: str):
        """Get info on a location's marketplace"""
        return await self._generate_request(
            method='GET',
            endpoint=f'/locations/{location_symbol}/marketplace',
        )

    async def get_location_ships(self, location_symbol: str):
        """Get the ships at a location"""
        return await self._generate_request(
            method='GET',
            endpoint=f'/locations/{location_symbol}/ships',
        )
