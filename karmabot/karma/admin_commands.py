import discord.ext.commands as commands

from karmabot import KarmaBot


class AdminCommands(commands.Cog):
    def __init__(self, bot: KarmaBot):
        self.__bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, module: str):
        """Reloads an extension, or the config file"""
        if module == "config":
            await self.__bot.reload_config()

        try:
            await self.__bot.unload_extension(module)
            await self.__bot.load_extension(module)
        except Exception as e:
            await ctx.reply("\N{PISTOL}")
            await ctx.reply("{}: {}".format(type(e).__name__, e))
        else:
            await ctx.reply("\N{OK HAND SIGN}")

    @commands.command(hidden=True)
    @commands.is_owner()
    async def cool(self, ctx: commands.Context):
        await ctx.reply("Yeah youre cool asf")
