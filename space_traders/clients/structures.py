from space_traders.clients.base import BaseClient


class StructuresClient(BaseClient):
    async def create_structure(self, location: str, type: str):
        """Create a new structure"""
        return await self._generate_request(
            method='POST',
            endpoint='/my/structures',
            params={
                'location': location,
                'type': type,
            },
        )

    async def deposit_to_user_structure(self, structure_id: str, ship_id: str, good: str, quantity: int):
        """Deposit goods to a structure you own"""
        return await self._generate_request(
            method='POST',
            endpoint=f'/my/structures/{structure_id}/deposit',
            params={
                'shipId': ship_id,
                'good': good,
                'quantity': quantity,
            },
        )

    async def deposit_to_structure(self, structure_id: str, ship_id: str, good: str, quantity: int):
        """Deposit goods to a structure"""
        return await self._generate_request(
            method='POST',
            endpoint=f'/structures/{structure_id}/deposit',
            params={
                'shipId': ship_id,
                'good': good,
                'quantity': quantity,
            },
        )

    async def get_structure(self, structure_id: str):
        """See specific structure"""
        return await self._generate_request(
            method='POST',
            endpoint=f'/structures/{structure_id}',
        )

    async def transfer_from_structure(self, structure_id: str, ship_id: str, good: str, quantity: int):
        """Transfer goods from your structure to a ship"""
        return await self._generate_request(
            method='POST',
            endpoint=f'/my/structures/{structure_id}/transfer',
            params={
                'shipId': ship_id,
                'good': good,
                'quantity': quantity,
            },
        )

    async def get_user_structure(self, structure_id: str):
        """Use to see a specific structure"""
        return await self._generate_request(
            method='POST',
            endpoint=f'/my/structures/{structure_id}',
        )

    async def get_user_structures(self):
        """Use to see all of your structures"""
        return await self._generate_request(
            method='POST',
            endpoint='/my/structures',
        )
