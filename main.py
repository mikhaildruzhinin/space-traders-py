import asyncio
import platform
from pprint import pprint
from time import time

import aiohttp

from space_traders.client.client import Client
from space_traders.client.request_factory import RequestFactory
from space_traders.config import BASE_URL


async def main():
    # temporary session to create a new user
    async with aiohttp.ClientSession(base_url=BASE_URL) as session:
        request_factory = RequestFactory(session)
        client = Client(request_factory)

        username = f'user{int(time())}'
        token = (await client.claim_username(username)).get('response', {}).get('token')

    headers = {
        'Authorization': f'Bearer {token}'
    }

    async with aiohttp.ClientSession(base_url=BASE_URL, headers=headers) as session:
        request_factory = RequestFactory(session)
        client = Client(request_factory)

        r = await asyncio.gather(
            client.get_game_status(),
            client.get_account_info(),
            client.get_loans(),
            client.take_loan('STARTUP')
        )
        pprint(r[-1])


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(
            asyncio.WindowsSelectorEventLoopPolicy()
        )
    asyncio.run(main())

