from ast import Str
from multiprocessing.sharedctypes import Value
from typing import Optional
import discord
from emoji import is_emoji
from discord.ext import commands


class UnicodeEmoji:
    def __init__(self, emoji: str):
        if not is_emoji(emoji):
            raise ValueError(f"{emoji} is not a value unicode emoji!")
        self.__emoji = emoji

    @classmethod
    async def convert(cls, ctx: commands.Context, arg: str):
        if is_emoji(arg):
            return cls(arg)
        else:
            raise commands.BadArgument()

    def __str__(self):
        return self.__emoji

    def __repr__(self):
        return f"UnicodeEmoji({self.__str__()}"


def emoji_value(
    map: dict[str | int, int],
    emoji: discord.Emoji | discord.PartialEmoji | UnicodeEmoji,
) -> Optional[int]:
    if isinstance(emoji, discord.PartialEmoji):
        if emoji.is_custom_emoji():
            id = emoji.id
            assert id is not None
            name = emoji.name
            if value := map.get(id):
                return value
            elif value := map.get(name):
                return value
            else:
                return None
        elif emoji.is_unicode_emoji():
            return map.get(emoji.name)

    elif isinstance(emoji, discord.Emoji):
        if value := map.get(emoji.id):
            return value
        elif value := map.get(emoji.name):
            return value
        else:
            return None

    elif isinstance(emoji, UnicodeEmoji):
        return map.get(str(emoji))

    else:
        raise ValueError(f"Argument {emoji} is not an emoji")
