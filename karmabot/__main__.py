import asyncio
from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
import logging

COGS = ["karma", "ping_pong"]


async def main():
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    bot = commands.Bot(command_prefix=">", intents=intents)
    logger = logging.getLogger("discord.karmabot")

    # load extensions
    for cog in COGS:
        await bot.load_extension(cog)

    @bot.event
    async def on_ready():
        assert bot.user is not None
        logger.info(f"Logged in as {bot.user} (ID: {bot.user.id})")

    load_dotenv()
    token = os.getenv("BOT_TOKEN")

    if token is None:
        logger.critical("Environment variable BOT_TOKEN not set, exiting")
    else:
        await bot.start(token)


asyncio.run(main())
