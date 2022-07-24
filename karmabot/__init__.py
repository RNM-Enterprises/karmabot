from sys import stdout
import discord
from discord.ext import commands
import logging
from karmabot.config import Config
from karma_store import KarmaStore


class KarmaBot(commands.Bot):
    def __init__(
        self,
        *args,
        extensions: list[str] = ["karma"],
        config: str = "config.yaml",
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.__init_extensions = extensions
        self.__config_filename = config
        self.config = Config(config)
        self.owner_ids = self.config.OWNERS
        self.karma_store = KarmaStore("karmastore.pkl")
        self.add_check(lambda ctx: ctx.guild is not None)

    # do anything we need to prior to startup
    async def setup_hook(self) -> None:

        for e in self.__init_extensions:
            await self.load_extension(e)

    async def reload_config(self):
        self.config = Config(self.__config_filename)


async def main():
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    bot = KarmaBot(command_prefix=">", intents=intents)
    logger = logging.getLogger("discord")
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler(stream=stdout))

    # TODO: initialise these in the bot class

    @bot.event
    async def on_ready():
        assert bot.user is not None
        logger.info(f"Logged in as {bot.user} (ID: {bot.user.id})")

    await bot.start(bot.config.BOT_TOKEN)
