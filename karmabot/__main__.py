from dotenv import load_dotenv
import discord
from discord.ext import commands
import os
import logging

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix=">", intents=intents)
logger = logging.getLogger("discord.karmabot")


@bot.event
async def on_ready():
    assert bot.user is not None
    logger.info(f"Logged in as {bot.user} (ID: {bot.user.id})")


@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send("pong!")


load_dotenv()
token = os.getenv("BOT_TOKEN")

if token is None:
    logger.critical("Environment variable BOT_TOKEN not set, exiting")
else:
    bot.run(token, log_level=logging.INFO)
