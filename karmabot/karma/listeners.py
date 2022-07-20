from discord.ext import commands
import discord
from .karma_store import KarmaStore

# need to use raw reaction events
# see docs (https://discordpy.readthedocs.io/en/latest/api.html#discord.on_raw_reaction_add)


class Listeners(commands.Cog):
    def __init__(self, bot: commands.Bot, karma_store: KarmaStore):
        self.__bot = bot
        self.__karma_store = karma_store

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, event: discord.RawReactionActionEvent):
        message = await self.get_message(event)

        self.__karma_store[message.author.id] += 1

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, event: discord.RawReactionActionEvent):
        message = await self.get_message(event)
        self.__karma_store[message.author.id] -= 1

    @commands.Cog.listener()
    async def on_raw_reaction_clear(self, event: discord.RawReactionActionEvent):
        pass

    @commands.Cog.listener()
    async def on_raw_reaction_emoji(self, event: discord.RawReactionActionEvent):
        pass

    # helper to get message from raw reaction event
    async def get_message(
        self,
        event: discord.RawReactionActionEvent
        | discord.RawReactionClearEvent
        | discord.RawReactionClearEmojiEvent,
    ) -> discord.Message:
        channel = self.__bot.get_channel(event.channel_id)
        assert isinstance(channel, discord.abc.Messageable)
        message = await channel.fetch_message(event.message_id)
        return message
