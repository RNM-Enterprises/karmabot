from discord.ext import commands
import discord
from karmabot import KarmaBot
from typing import Optional
import logging
from .emoji import emoji_value

# need to use raw reaction events
# see docs (https://discordpy.readthedocs.io/en/latest/api.html#discord.on_raw_reaction_add)

RawReact = (
    discord.RawReactionActionEvent
    | discord.RawReactionClearEvent
    | discord.RawReactionClearEmojiEvent
)


class Listeners(commands.Cog):
    def __init__(self, bot: KarmaBot):
        self.__bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, event: discord.RawReactionActionEvent):
        message = await self.__get_message(event)

        if value := self.__emoji_value(event.emoji):
            self.__bot.karma_store[message.author.id] += value

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, event: discord.RawReactionActionEvent):
        message = await self.__get_message(event)
        if value := self.__emoji_value(event.emoji):
            self.__bot.karma_store[message.author.id] -= value

    @commands.Cog.listener()
    async def on_raw_reaction_clear(self, event: discord.RawReactionClearEvent):
        message = await self.__get_message(event)
        logging.info(
            f"Reactions cleared for message {message.jump_url}. Karma has not been affected"
        )

    @commands.Cog.listener()
    async def on_raw_reaction_clear_emoji(
        self, event: discord.RawReactionClearEmojiEvent
    ):
        message = await self.__get_message(event)
        logging.info(
            f"Reactions for emoji '{event.emoji.name}' cleared for message {message.jump_url}. Karma has not been affected"
        )

    # helper to get message from raw reaction event
    async def __get_message(
        self,
        event: RawReact,
    ) -> discord.Message:
        channel = self.__bot.get_channel(event.channel_id)
        assert isinstance(channel, discord.abc.Messageable)
        message = await channel.fetch_message(event.message_id)
        return message

    def __emoji_value(self, emoji: discord.PartialEmoji) -> Optional[int]:
        karma_map = self.__bot.config.emoji
        return emoji_value(karma_map, emoji)
