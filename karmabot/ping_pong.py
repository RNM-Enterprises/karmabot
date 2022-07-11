import discord.ext.commands as commands


class PingPong(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """
        Pings your pong
        """
        await ctx.reply("pong!")


async def setup(bot):
    await bot.add_cog(PingPong(bot))
