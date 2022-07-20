import discord.ext.commands as commands

from .karma_store import KarmaStore


class Listeners(commands.Cog):
    def __init__(self, bot: commands.Bot, karma_store: KarmaStore):
        self.bot = bot
        self.karma_store = karma_store
