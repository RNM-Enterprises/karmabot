from cmath import pi
from typing import Optional
import discord
import discord.ext.commands as commands
from .karma_store import KarmaStore
from .karma_cards import get_karma_card
from io import BytesIO
from PIL import Image
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
            picture = await get_karma_card(ctx.author,self.karma_store[ctx.author.id])

            pic_bytes = BytesIO()
            picture.show()
            picture.save(pic_bytes,format="PNG")
            await ctx.reply(file=discord.File(pic_bytes))
        elif isinstance(member,discord.Member):
            picture = await get_karma_card(ctx.author,self.karma_store[member.id])
            await ctx.reply(file=discord.File("./resources/template.PNG"))
        else:
           await ctx.reply(f"{member} isnt in this server?")
        
    @commands.command()
    async def leaderboard(self,ctx:commands.Context):
        pass

    
