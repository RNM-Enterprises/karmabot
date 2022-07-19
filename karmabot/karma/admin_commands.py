import discord.ext.commands as commands


class AdminCommands(commands.Cog):
    def __init__(self, bot,karma_store):
        self.bot = bot
        AdminCommands.karma_store = karma_store
