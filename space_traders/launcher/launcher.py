from pathlib import Path
from time import time
from typing import Optional

import aiofiles
import aiohttp

from space_traders.clients.game import GameClient
from space_traders.clients.user import UserClient
from space_traders.config import (
    BASE_URL,
    USER_FILE,
)
from space_traders.logger.logger import logger


class Launcher:
    def __init__(self, sign_up: bool, username: Optional[str] = None):
        self.username = username or f'user{int(time())}'
        self.sign_up = sign_up

    async def launch(self):
        Path(USER_FILE).touch(exist_ok=True)

        if self.sign_up:
            headers = {}
        else:
            async with aiofiles.open(USER_FILE, mode='r', encoding='utf-8') as f:
                user_data = await f.read()
            if ',' not in user_data:
                logger.error('no user data')
                return
            _, token = user_data.split(',') # TODO: check username

            headers = {
                'Authorization': f'Bearer {token}'
            }

        async with aiohttp.ClientSession(base_url=BASE_URL, headers=headers) as session:
            user_client = UserClient(session)

            if self.sign_up:
                async with aiofiles.open(USER_FILE, mode='w', encoding='utf-8') as f:
                    user_data = await user_client.claim_username(self.username)
                    token = user_data.get('response', {}).get('token')
                    await f.write(f'{self.username},{token}')
            else:
                game_client = GameClient(session)
                r = await game_client.get_game_status()
                logger.info(r)
