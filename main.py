import asyncio

from .service.discordService import DiscordService
from .service.discordHandlers import *

# TODO: Make a list
# Setup and run discord service
services = [
    DiscordService(
        token = 'MY DISCORD TOKEN',
        handlers = [
            CussFilterHandler()
        ]
    )
]

for serv in services:
    serv.Run()