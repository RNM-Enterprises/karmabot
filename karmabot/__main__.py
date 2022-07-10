from dotenv import load_dotenv
import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"logged in, bot ready")


@bot.command()
async def ping(ctx):
    await ctx.send("pong!")


load_dotenv()
token = os.getenv("BOT_TOKEN")

if token is None:
    print("bot token not found")
else:
    bot.run(token)
