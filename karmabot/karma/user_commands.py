
import discord
import discord.ext.commands as commands

import numpy as np
import requests
from .karma_store import KarmaStore
from PIL import Image, ImageDraw, ImageFont

class UserCommands(commands.Cog):
    def __init__(self, bot: commands.Bot, karma_store: KarmaStore):
        self.bot = bot
        self.karma_store = karma_store

    @commands.command()
    async def karma(self, ctx: commands.Context):
        """
        Tells you how much karma you have
        """

        # open main image and drawer
        response = Image.new('RGB',(934,282))
        response_drawer = ImageDraw.Draw(response)
        
        # fill main image with colored background
        response.paste( (0,0,0), (0,0,response.size[0],response.size[1]))

        # write users name and discriminator        
        myFont = ImageFont.truetype(font='arial.ttf',size=54)
        response_drawer.text((320,104), str(ctx.author),font=myFont,fill=(255,255,255))
        
        # write users karma
        myFont = ImageFont.truetype(font='arial.ttf',size=64)
        response_drawer.text((320,response.size[1] -(64+44)), f'karma: {self.karma_store.get(int(ctx.author.id))}',font=myFont,fill=(233,79,55))
        
        # collect users avatar
        avatar = Image.open(requests.get(str(ctx.author.avatar),stream=True).raw).convert('RGB').resize((254,254))
        img_arr = np.array(avatar)

        # crop user avatar into circle
        lum_img = Image.new('L',(avatar.size[0],avatar.size[1]),0)
        ImageDraw.Draw(lum_img).pieslice(((0,0),(lum_img.size[0],lum_img.size[1])),0,360,fill=255, outline='white')
        lum_img_arr = np.array(lum_img)
      

        framed_avatar_arr = np.dstack((img_arr , lum_img_arr))
        
        framed_avatar = Image.fromarray(framed_avatar_arr)

        response.paste(framed_avatar,(14,14),mask=framed_avatar)

        response.save('./Resources/Template.png')
        response.close()

        await ctx.reply(file=discord.File('./Resources/Template.png'))

    @commands.command()
    async def leaderboard(self,ctx:commands.Context):
        pass
    
    @commands.command()
    async def thisdoesntexistyet(self, ctx:commands.Context):
        await ctx.channel.send("huh? well it does now...")