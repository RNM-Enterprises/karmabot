from urllib import response
import discord
import discord.ext.commands as commands

from .karma_store import KarmaStore
from PIL import Image, ImageDraw, ImageFont

class UserCommands(commands.Cog):
    def __init__(self, bot: commands.Bot, karma_store: KarmaStore):
        self.bot = bot
        self.karma_store = karma_store

    @commands.command()
    async def karma(self, ctx: commands.Context):
        """
        Tells you your fake karma (because real karma doesnt exist yet)
        """
        # self.karma_store[int(ctx.author.id)] += 1
        # await ctx.reply(
        #     f"{ctx.author}'s karma isnt {self.karma_store.get(int(ctx.author.id))}"
        # )

        response = Image.open('./Resources/Template.jpg')
    
        drawer = ImageDraw.Draw(response)
        myFont = ImageFont.truetype(font='arial.ttf',size=65)
        drawer.text((4,4), ctx.author.name,font=myFont,fill=(255,255,255))
        drawer.text((4,69), f'karma:{self.karma_store.get(int(ctx.author.id))}',font=myFont,fill=(255,255,255))


        response.save('./Resources/Template.jpg')

        await ctx.reply(file=discord.File('./Resources/Template.jpg'))

        response.paste( (0,0,0), (0,0,response.size[0],response.size[1]))
        response.save('./Resources/Template.jpg')

        response.close()

    @commands.command()
    async def leaderboard(self,ctx:commands.Context):
        pass

    