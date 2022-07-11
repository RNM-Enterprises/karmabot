from .admin_commands import AdminCommands
from .listeners import Listeners
from .user_commands import UserCommands
from discord.ext.commands import Bot


async def setup(bot: Bot):

    await bot.add_cog(AdminCommands(bot))
    await bot.add_cog(UserCommands(bot))
    await bot.add_cog(Listeners(bot))
