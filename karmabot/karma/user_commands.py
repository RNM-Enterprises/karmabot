import discord.ext.commands as commands

from karmabot import karma
from karmabot.karma import karma_store


class UserCommands(commands.Cog):
    def __init__(self, bot, karma_store):
        self.bot = bot
        UserCommands.karma_store = karma_store

    @commands.command()
    async def karma(self, ctx: commands.Context):
        """
        Tells you your fake karma (because real karma doesnt exist yet)
        """
        UserCommands.karma_store[int(ctx.author.id)] += 1
        await ctx.reply(
            f"{ctx.author}'s karma isnt {UserCommands.karma_store.get(int(ctx.author.id))}"
        )
