from space_traders.clients.base import BaseClient


class SystemsClient(BaseClient):
    async def get_available_ships(self, system: str):
        """Get a list of all available ships in the system"""
        return await self._generate_request(
            method='POST',
            endpoint=f'/systems/{system}/ship-listings',
        )

    async def get_flight_plans(self, system: str):
        """Get all active flight plans in the system"""
        return await self._generate_request(
            method='POST',
            endpoint=f'/systems/{system}/flight-plans',
        )

    async def get_docked_ships(self, system: str):
        """Get info on a system's docked ships"""
        return await self._generate_request(
            method='POST',
            endpoint=f'/systems/{system}/ships',
        )

    async def get_locations(self, system: str):
        """Get location info for a system"""
        return await self._generate_request(
            method='POST',
            endpoint=f'/systems/{system}/locations',
        )

    async def get_system(self, system: str):
        """Get systems info"""
        return await self._generate_request(
            method='POST',
            endpoint=f'/systems/{system}',
        )
