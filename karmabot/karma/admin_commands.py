import discord.ext.commands as commands

from .karma_store import KarmaStore


class AdminCommands(commands.Cog):
    def __init__(self, bot: commands.Bot, karma_store: KarmaStore):
        self.bot = bot
        self.karma_store = karma_store

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, module: str):
        """Reloads a module."""
        try:
            await self.bot.unload_extension(module)
            await self.bot.load_extension(module)
        except Exception as e:
            await ctx.reply("\N{PISTOL}")
            await ctx.reply("{}: {}".format(type(e).__name__, e))
        else:
            await ctx.reply("\N{OK HAND SIGN}")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def cool(self, ctx: commands.Context):
        await ctx.reply("Yeah youre cool asf")
