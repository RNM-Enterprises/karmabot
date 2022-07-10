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


@bot.command
async def ping(ctx):
    await ctx.send("pong!")


@bot.event
async def on_message(msg: discord.Message):
    content = msg.content.lower()
    if (
        content.startswith("i am")
        or content.startswith("i'm")
        or content.startswith("im")
    ):
        msg.reply(f"hello, {msg.author}, I'm a bot!")


load_dotenv()
bot.run(os.getenv("BOT_TOKEN"))
