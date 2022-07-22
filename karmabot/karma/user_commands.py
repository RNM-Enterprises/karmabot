import discord.ext.commands as commands

from .karma_store import KarmaStore


class UserCommands(commands.Cog):
    def __init__(self, bot: commands.Bot, karma_store: KarmaStore):
        self.bot = bot
        self.karma_store = karma_store

    @commands.command()
    async def karma(self, ctx: commands.Context):
        """
        Tells you your karma
        """
        await ctx.reply(f"{ctx.author}'s karma is {self.karma_store[ctx.author.id]}")
