import discord.ext.commands as commands

from karmabot import KarmaBot


class UserCommands(commands.Cog):
    def __init__(self, bot: KarmaBot):
        self.bot = bot

    @commands.command()
    async def karma(self, ctx: commands.Context):
        """
        Tells you your karma
        """
        await ctx.reply(
            f"{ctx.author}'s karma is {self.bot.karma_store[ctx.author.id]}"
        )
