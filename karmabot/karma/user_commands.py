from cmath import pi
from typing import Optional
import discord
import discord.ext.commands as commands

from karmabot import KarmaBot
from .karma_cards import get_karma_card


class UserCommands(commands.Cog):
    def __init__(self, bot: KarmaBot):
        self.bot = bot

    @commands.command()
    async def karma(
        self, ctx: commands.Context, member: Optional[discord.Member] | str
    ):
        """
        Tells you how much karma a user has
        """
        if member is None:
            await ctx.reply(
                file=await get_karma_card(
                    ctx.author, self.bot.karma_store[ctx.author.id]
                )
            )

        elif isinstance(member, str):
            await ctx.reply(f"User {member} does not exist in this server?")

        elif isinstance(member, discord.Member):
            await ctx.reply(
                file=await get_karma_card(member, self.bot.karma_store[member.id])
            )

    @commands.command()
    async def leaderboard(self, ctx: commands.Context):
        pass
