import discord.ext.commands as commands

from karma_store import KarmaStore

class AdminCommands(commands.Cog):
    def __init__(self, bot,karma_store):
        self.bot = bot
        self.karma_store = karma_store
