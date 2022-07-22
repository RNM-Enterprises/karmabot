from typing import Optional
import discord
import discord.ext.commands as commands
from .karma_store import KarmaStore
from .karma_cards import get_karma_card
from io import BytesIO
class UserCommands(commands.Cog):
    def __init__(self, bot: commands.Bot, karma_store: KarmaStore):
        self.bot = bot
        self.karma_store = karma_store

    @commands.command()
    async def karma(self, ctx: commands.Context,member:Optional[discord.Member] | str):
        """
        Tells you how much karma a user has
        """
        if member is None:
            await ctx.reply(file=discord.File(await get_karma_card(ctx.author,self.karma_store[ctx.author.id])))
        elif isinstance(member,discord.Member):
            #get_karma_card(member,self.karma_store[member.id])
            await ctx.reply(file=discord.File('./Resources/Template.png'))
        else:
           await ctx.reply(f"{member} isnt in this server?")

    @commands.command()
    async def leaderboard(self,ctx:commands.Context):
        pass

    
