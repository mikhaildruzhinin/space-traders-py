from space_traders.clients.base import BaseClient


class FlightPlanClient(BaseClient):
    async def get_flight_plan(self, flight_plan_id: str):
        """Get info on an existing flight plan"""
        return await self._generate_request(
            method='GET',
            endpoint=f'/my/flight-plans/{flight_plan_id}',
        )

    async def create_flight_plan(self, ship_id: str, destination: str):
        """Submit a new flight plan"""
        return await self._generate_request(
            method='POST',
            endpoint=f'/my/flight-plans',
            params={
                'shipId': ship_id,
                'destination': destination,
            },
        )
