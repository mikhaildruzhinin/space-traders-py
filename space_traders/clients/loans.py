from space_traders.clients.base import BaseClient


class LoansClient(BaseClient):
    async def get_user_loans(self):
        """Get your loans"""
        return await self._generate_request(
            method='GET',
            endpoint='/my/loans',
        )

    async def pay_loan(self, loan_id: str):
        """Pay off your loan"""
        return await self._generate_request(
            method='PUT',
            endpoint=f'/my/loans/{loan_id}',
        )

    async def take_loan(self, type: str):
        """Take out a loan"""
        return await self._generate_request(
            method='POST',
            endpoint='/my/loans',
            params={'type': type},
        ),
