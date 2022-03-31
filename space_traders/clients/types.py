from typing import Optional

from space_traders.clients.base import BaseClient


class TypesClient(BaseClient):
    async def get_goods(self):
        """Get available goods"""
        return await self._generate_request(
            method='POST',
            endpoint='/types/goods',
        )

    async def get_loans(self):
        """Get available loans"""
        return await self._generate_request(
            method='POST',
            endpoint='/types/loans',
        )

    async def get_structures(self):
        """Get available structures"""
        return await self._generate_request(
            method='POST',
            endpoint='/types/structures',
        )

    async def get_ships(self, class_: Optional[str] = None):
        """Get info on available ships"""
        return await self._generate_request(
            method='GET',
            endpoint='/types/ships',
            params={'class': class_} if class_ else {},
        )
