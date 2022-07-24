from typing import Optional
import discord
from emoji import is_emoji

EmojiType = discord.Emoji | discord.PartialEmoji | str


def emoji_value(
    map: dict[str | int, int], emoji: discord.Emoji | discord.PartialEmoji | str
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

    elif isinstance(emoji, str) and is_emoji(emoji):
        return map.get(emoji)
    else:
        raise ValueError(f"Argument {emoji} is not an emoji")
