from io import BytesIO
import discord
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import requests
from os import SEEK_SET


async def get_karma_card(user: discord.abc.User, user_karma: int) -> discord.File:
    """
    returns karma card for a user as an Image
    """
    card = Image.new("RGB", (934, 282))
    card_drawer = ImageDraw.Draw(card)
    card.paste((40, 40, 40), (0, 0, card.size[0], card.size[1]))

    font = ImageFont.truetype(font="arial.ttf", size=54)
    card_drawer.text((340, 64), str(user), font=font, fill=(245, 249, 215))

    font = ImageFont.truetype(font="arial.ttf", size=74)
    card_drawer.text(
        (340, card.size[1] - (94 + 44)),
        f"karma: {user_karma}",
        font=font,
        fill=(250, 219, 47),
    )

    avatar = (
        Image.open(BytesIO(requests.get(user.display_avatar.url).content))
        .convert("RGB")
        .resize((234, 234))
    )
    avatar_arr = np.array(avatar)

    lum_img = Image.new("L", (avatar.size[0], avatar.size[1]), 0)
    ImageDraw.Draw(lum_img).pieslice(
        ((0, 0), (lum_img.size[0], lum_img.size[1])), 0, 360, fill=255, outline="white"
    )
    lum_img_arr = np.array(lum_img)

    framed_avatar_arr = np.dstack((avatar_arr, lum_img_arr))
    framed_avatar = Image.fromarray(framed_avatar_arr)

    card.paste(
        framed_avatar, (int((282 - 234) / 2), int((282 - 234) / 2)), mask=framed_avatar
    )

    pic_bytes = BytesIO()
    card.save(pic_bytes, format="PNG")
    pic_bytes.seek(SEEK_SET)
    return discord.File(pic_bytes, filename="karma.png")
