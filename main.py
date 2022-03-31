import asyncio
import platform
from time import time

import aiohttp

from space_traders.clients.game import GameClient
from space_traders.clients.user import UserClient
from space_traders.config import BASE_URL


async def main():
    # temporary session to create a new user
    async with aiohttp.ClientSession(base_url=BASE_URL) as session:
        client = UserClient(session)

        username = f'user{int(time())}'
        token = (await client.claim_username(username)).get('response', {}).get('token')

    headers = {
        'Authorization': f'Bearer {token}'
    }

    async with aiohttp.ClientSession(base_url=BASE_URL, headers=headers) as session:
        client = GameClient(session)

        r = await client.get_game_status()
        print(r)


if __name__ == '__main__':
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(
            asyncio.WindowsSelectorEventLoopPolicy()
        )
    asyncio.run(main())
