import discord.ext.commands as commands

from karmabot.karma import karma_store


class Listeners(commands.Cog):
    def __init__(self, bot,karma_store):
        self.bot = bot
        Listeners.karma_store = karma_store