from karmabot.karma.karma_store import KarmaStore
from .admin_commands import AdminCommands
from .listeners import Listeners
from .user_commands import UserCommands
from discord.ext.commands import Bot


async def setup(bot: Bot):

    karma_store = KarmaStore()

    await bot.add_cog(AdminCommands(bot, karma_store))
    await bot.add_cog(UserCommands(bot, karma_store))
    await bot.add_cog(Listeners(bot, karma_store))
