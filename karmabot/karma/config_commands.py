import discord.ext.commands as commands
import discord
from karmabot import KarmaBot
from .emoji import UnicodeEmoji, emoji_value
from functools import partial


class ConfigCommands(commands.Cog):
    def __init__(self, bot: KarmaBot):
        self.__bot = bot
        self.__emoji_value = partial(emoji_value, self.__bot.config.emoji)

    @commands.group(invoke_without_command=True)
    async def emoji(self, ctx: commands.Context, emoji: discord.Emoji | UnicodeEmoji):
        value = self.__emoji_value(emoji)

        await ctx.reply(
            f"Emoji {str(emoji)} has value {value if value is not None else 0}"
        )

    @emoji.command()
    async def list(self, ctx: commands.Context):
        """
        Gets the karma values for all emoji
        """
        await ctx.reply(str(self.__bot.config.emoji))

    @emoji.command()
    async def set(
        self, ctx: commands.Context, emoji: discord.Emoji | UnicodeEmoji, value: int
    ):
        if isinstance(emoji, discord.Emoji):
            self.__bot.config.emoji[emoji.name] = value
        elif isinstance(emoji, UnicodeEmoji):
            self.__bot.config.emoji[str(emoji)] = value
        else:  # unreachable
            assert False

        await self.__bot.config.save()
        await ctx.reply(f"Emoji {str(emoji)} has been given a karma value of {value}")

    @emoji.command()
    async def unset(self, ctx: commands.Context, emoji: discord.Emoji | UnicodeEmoji):
        async def try_del(key: str | int) -> bool:
            try:
                del self.__bot.config.emoji[key]
                return True
            except KeyError:
                await ctx.reply(f"Emoji {str(emoji)} is already worth 0 karma!")
                return False

        if isinstance(emoji, discord.Emoji):
            if emoji.id in self.__bot.config.emoji.keys():
                if not await try_del(emoji.id):
                    return
            elif emoji.name in self.__bot.config.emoji.keys():
                if not await try_del(emoji.name):
                    return

        elif isinstance(emoji, UnicodeEmoji):
            if not await try_del(str(emoji)):
                return

        else:  # unreachable
            assert False

        await self.__bot.config.save()
        await ctx.reply(f"Emoji {str(emoji)} has been given a karma value of 0")
