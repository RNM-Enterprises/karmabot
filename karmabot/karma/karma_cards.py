import io
import discord
import discord.ext.commands as commands
import numpy as np
from .karma_store import KarmaStore
from PIL import Image, ImageDraw, ImageFont

async def get_karma_card(user: discord.abc.User,user_karma:int ):
        '''
        returns karma card for a user as an Image
        '''
        card = Image.new('RGB',(934,282))
        card_drawer = ImageDraw.Draw(card)
        card.paste( (40,40,40), (0,0,card.size[0],card.size[1]))
        
        font = ImageFont.truetype(font='arial.ttf',size=54)
        card_drawer.text((320,84), str(user),font=font,fill=(245,249,215))
        
        font = ImageFont.truetype(font='arial.ttf',size=74)
        card_drawer.text((320,card.size[1] -(74+44)), f'Karma: {user_karma}',font=font,fill=(250,219,47))
        
        avatar = Image.open(await user.display_avatar.read()).convert('RGB').resize((234,234))
        avatar_arr = np.array(avatar)
        
        lum_img = Image.new('L',(avatar.size[0],avatar.size[1]),0)
        ImageDraw.Draw(lum_img).pieslice(((0,0),(lum_img.size[0],lum_img.size[1])),0,360,fill=255, outline='white')
        lum_img_arr = np.array(lum_img)
        
        framed_avatar_arr = np.dstack((avatar_arr , lum_img_arr))
        framed_avatar = Image.fromarray(framed_avatar_arr)
        
        card.paste(framed_avatar,(int((282-234)/2),int((282-234)/2)),mask=framed_avatar)

        bytes_array = io.BytesIO()

        card.save(bytes_array,format='PNG')
        return bytes_array