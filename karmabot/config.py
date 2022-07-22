import yaml
import logging
import re


class Config:
    def __init__(self, file: str):
        with open(file, "r") as f:
            parsed = yaml.safe_load(f)

        self.BOT_TOKEN: str = parsed.get("bot-token")
        self.OWNERS: list[int] = parsed.get("owners")

        self.check_config()

    def check_config(self):
        logger = logging.getLogger("karmabot.config")
        if self.BOT_TOKEN is None:
            logger.critical("No bot token defined in config, exiting...")
            exit()

        for id in self.OWNERS:
            if type(id) is not int or not re.match(r"^\d{17,18}$", str(id)):
                logger.warn(f"User ID {id} is not a valid discord user id")
