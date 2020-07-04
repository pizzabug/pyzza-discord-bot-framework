from typing import List
import asyncio
import discord as d

from .service import Service

"""
DiscordHandler
    Does handling for each job required for the bot. Allows for
    multithreading for multiple checks and jobs.

    [new DiscordHandle].discord_client
        Contains the Discord client for manipulation of responding.

    [new DiscordHandle].on_message
        Is called by master thread when message is received.

    [new DiscordHandle].on_ready
        Is called by master thread when master client is ready.
"""

# TODO: Create a queue for sending; stop using the library directly.

class DiscordHandler ():
    def Run (self, discord_client : d.Client):
        self.discord_client = discord_client

    async def on_message (self, message : str):
        pass

    async def on_ready (self):
        pass

    

"""
DiscordClient
    Will process through each handler.
"""

# TODO: Do multithreading.

class DiscordClient (d.Client):
    def __init__ (self, handlers):
        self.handlers = handlers
        for handle in self.handlers:
            handle.Run(self)
        super().__init__()

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.discord_client.user))
        
        # Call on_ready for every handler
        for handler in self.handlers:
            await (handler.on_ready ())
	
    async def on_message(self, message):
        # Call on_message for every handler
        for handler in self.handlers:
            await (handler.on_message (message))

    
    

class DiscordService (Service):

    def __init__ (self, token, handlers):
        # Setting Discord Client
        self.token = token
        self.handlers = handlers

        # Calling parent method
        super ().__init__ ('DiscordService')

    def Run (self):
        # Starting Discord Client
        discordClient = DiscordClient (self.handlers)
        discordClient.run (self.token)
        
        # Calling parent method
        super ().Run ()