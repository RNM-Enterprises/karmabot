import imp
from .admin_commands import AdminCommands
from .listeners import Listeners
from .user_commands import UserCommands
from .emoji_commands import EmojiCommands
from karmabot import KarmaBot


async def setup(bot: KarmaBot):
    await bot.add_cog(AdminCommands(bot))
    await bot.add_cog(UserCommands(bot))
    await bot.add_cog(Listeners(bot))
    await bot.add_cog(EmojiCommands(bot))
