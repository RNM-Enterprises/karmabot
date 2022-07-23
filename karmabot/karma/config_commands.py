import discord.ext.commands as commands
import discord
from karmabot import KarmaBot


class ConfigCommands(commands.Cog):
    def __init__(self, bot: KarmaBot):
        self.bot = bot

    @commands.group()
    async def emoji(self, ctx: commands.Context):
        pass

    @emoji.command()
    async def get(self, ctx: commands.Context):
        """
        Gets the karma values for all emoji, or a specific emoji
        """
        await ctx.reply(f"{self.bot.config.emoji}")

    @emoji.command()
    async def set(self, ctx: commands.Context, emoji: discord.PartialEmoji, value: int):
        if emoji.is_custom_emoji():
            pass

        elif emoji.is_unicode_emoji():
            pass

    @emoji.command()
    async def unset(self, ctx: commands.Context, emoji: discord.PartialEmoji):
        pass
