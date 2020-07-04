import asyncio
import discord as d

from .discordService import DiscordHandler

class PoggersHandler (DiscordHandler):
    async def on_message (self, message):
        if (message.content.lower() == "poggers"):
            await message.channel.send("Poggers")

    async def on_ready (self):
        print('PoggersHandler Loaded')