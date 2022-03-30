from typing import (
    Dict,
    Optional,
    Union,
)

from space_traders.client.request_factory import RequestFactory


class Client:
    def __init__(
        self,
        request_factory: RequestFactory,
    ):
        self.__request_factory = request_factory

    # account
    async def get_account(self):
        """Get information on your account"""
        return await self.__request_factory.generate(
            method='GET',
            endpoint='/my/account'
        )

    # flight plans
    async def get_flight_plan(self, flight_plan_id: str):
        """Get info on an existing flight plan"""
        return await self.__request_factory.generate(
            method='GET',
            endpoint=f'/my/flight-plans/{flight_plan_id}',
        )

    async def create_flight_plan(self, ship_id: str, destination: str):
        """Submit a new flight plan"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint=f'/my/flight-plans',
            params={
                'shipId': ship_id,
                'destination': destination,
            },
        )

    # game
    async def get_game_status(self):
        """Use to determine whether the server is alive"""
        return await self.__request_factory.generate(
            method='GET',
            endpoint='/game/status',
        )

    # leaderboard
    async def get_leaderboard(self):
        """Use to see the current net worth of the top players"""
        return await self.__request_factory.generate(
            method='GET',
            endpoint='/game/leaderboard/net-worth',
        )

    # loans
    async def get_user_loans(self):
        """Get your loans"""
        return await self.__request_factory.generate(
            method='GET',
            endpoint='/my/loans',
        )

    async def pay_loan(self, loan_id: str):
        """Pay off your loan"""
        return await self.__request_factory.generate(
            method='PUT',
            endpoint=f'/my/loans/{loan_id}',
        )

    async def take_loan(self, type: str):
        """Take out a loan"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint='/my/loans',
            params={'type': type},
        ),

    # locations
    async def get_location(self, location_symbol: str):
        """Get info on a location"""
        return await self.__request_factory.generate(
            method='GET',
            endpoint=f'/locations/{location_symbol}',
        )

    async def get_location_market(self, location_symbol: str):
        """Get info on a location's marketplace"""
        return await self.__request_factory.generate(
            method='GET',
            endpoint=f'/locations/{location_symbol}/marketplace',
        )

    async def get_location_ships(self, location_symbol: str):
        """Get the ships at a location"""
        return await self.__request_factory.generate(
            method='GET',
            endpoint=f'/locations/{location_symbol}/ships',
        )

    # purchase orders
    async def purchase(self, ship_id: str, good: str, quantity: int):
        """Place a new purchase order"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint='/my/purchase-orders',
            params={
                'shipId': ship_id,
                'good': good,
                'quantity': quantity,
            },
        )

    # sell orders
    async def sell(self, ship_id: str, good: str, quantity: int):
        """Place a new sell order"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint='/my/sell-orders',
            params={
                'shipId': ship_id,
                'good': good,
                'quantity': quantity,
            },
        )

    # ships
    async def buy_ship(self, location: str, type: str):
        """Buy a new ship"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint='/my/ships',
            params={
                'location': location,
                'type': type,
            },
        )

    async def get_user_ship(self, ship_id: str):
        """Get your ship info"""
        return await self.__request_factory.generate(
            method='GET',
            endpoint=f'/my/ships/{ship_id}',
        )

    async def get_user_ships(self):
        """Get your ships"""
        return await self.__request_factory.generate(
            method='GET',
            endpoint='/my/ships',
        )

    async def jettison_cargo(self, ship_id: str, good: str, quantity: int):
        """Jettison cargo"""
        return await self.__request_factory.generate(
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
        return await self.__request_factory.generate(
            method='DELETE',
            endpoint=f'/my/ships/{ship_id}',
        )

    async def transfer_cargo(self, from_ship_id: str, to_ship_id: str, good: str, quantity: int):
        """Transfer cargo between ships"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint=f'/my/ships/{from_ship_id}/transfer',
            params={
                'toShipId': to_ship_id,
                'good': good,
                'quantity': quantity,
            },
        )

    # structures
    async def create_structure(self, location: str, type: str):
        """Create a new structure"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint='/my/structures',
            params={
                'location': location,
                'type': type,
            },
        )

    async def deposit_to_user_structure(self, structure_id: str, ship_id: str, good: str, quantity: int):
        """Deposit goods to a structure you own"""
        return await self.__request_factory.generate(
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
        return await self.__request_factory.generate(
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
        return await self.__request_factory.generate(
            method='POST',
            endpoint=f'/structures/{structure_id}',
        )

    async def transfer_from_structure(self, structure_id: str, ship_id: str, good: str, quantity: int):
        """Transfer goods from your structure to a ship"""
        return await self.__request_factory.generate(
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
        return await self.__request_factory.generate(
            method='POST',
            endpoint=f'/my/structures/{structure_id}',
        )

    async def get_user_structures(self):
        """Use to see all of your structures"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint='/my/structures',
        )

    # systems
    async def get_available_ships(self, system: str):
        """Get a list of all available ships in the system"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint=f'/systems/{system}/ship-listings',
        )

    async def get_flight_plans(self, system: str):
        """Get all active flight plans in the system"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint=f'/systems/{system}/flight-plans',
        )

    async def get_docked_ships(self, system: str):
        """Get info on a system's docked ships"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint=f'/systems/{system}/ships',
        )

    async def get_locations(self, system: str):
        """Get location info for a system"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint=f'/systems/{system}/locations',
        )

    async def get_system(self, system: str):
        """Get systems info"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint=f'/systems/{system}',
        )

    # types
    async def get_goods(self):
        """Get available goods"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint='/types/goods',
        )

    async def get_loans(self):
        """Get available loans"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint='/types/loans',
        )

    async def get_structures(self):
        """Get available structures"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint='/types/structures',
        )

    async def get_ships(self, class_: Optional[str] = None):
        """Get info on available ships"""
        return await self.__request_factory.generate(
            method='GET',
            endpoint='/types/ships',
            params={'class': class_} if class_ else {},
        )

    # user
    async def claim_username(self, username: str):
        """Claim a username and get a token"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint=f'/users/{username}/claim',
        )

    # warp jump
    async def warp_jump(self, ship_id: str):
        """Claim a username and get a token"""
        return await self.__request_factory.generate(
            method='POST',
            endpoint=f'/my/warp-jumps',
            params={'shipId': ship_id},
        )
