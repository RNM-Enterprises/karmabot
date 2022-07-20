import discord.ext.commands as commands

from .karma_store import KarmaStore


class UserCommands(commands.Cog):
    def __init__(self, bot: commands.Bot, karma_store: KarmaStore):
        self.bot = bot
        self.karma_store = karma_store

    @commands.command()
    async def karma(self, ctx: commands.Context):
        """
        Tells you your fake karma (because real karma doesnt exist yet)
        """
        self.karma_store[int(ctx.author.id)] += 1
        await ctx.reply(
            f"{ctx.author}'s karma isnt {self.karma_store.get(int(ctx.author.id))}"
        )

    @commands.command()
    async def leaderboard(self,ctx:commands.Context):
        pass

    