import argparse
import asyncio
import platform
from typing import Optional

from space_traders.launcher.launcher import Launcher

parser = argparse.ArgumentParser()

parser.add_argument(
    '--username',
    '-u',
    dest='username',
    action='store',
    type=str,
    help='username'
)
parser.add_argument(
    '--signup',
    '-s',
    dest='sign_up',
    action='store_true',
    help='generate token for a new user and exit'
)

args = parser.parse_args()


def main(sign_up: bool, username: Optional[str] = None):
    if platform.system() == 'Windows':
        asyncio.set_event_loop_policy(
            asyncio.WindowsSelectorEventLoopPolicy()
        )

    asyncio.run(
        Launcher(
            username=username,
            sign_up=sign_up,
        ).launch()
    )


if __name__ == '__main__':
    main(
        username=args.username,
        sign_up=args.sign_up,
    )
