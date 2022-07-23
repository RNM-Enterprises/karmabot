import yaml
import logging
import re


class Config:
    def __init__(self, file: str):
        with open(file, "r") as f:
            parsed = yaml.safe_load(f)

        self.BOT_TOKEN: str = parsed.get("bot-token")
        self.OWNERS: list[int] = parsed.get("owners")
        self.EMOJI: dict[str | int, int] = parsed.get("emoji")

        self.check_config()

    def check_config(self):
        logger = logging.getLogger("karmabot.config")
        if self.BOT_TOKEN is None:
            logger.critical("No bot token defined in config, exiting...")
            exit()

        for id in self.OWNERS:
            if type(id) is not int or not re.match(r"^\d{17,18}$", str(id)):
                logger.warn(f"User ID {id} is not a valid discord user id")

        for (emoji, value) in self.EMOJI.items():
            if not (isinstance(emoji, str) or isinstance(emoji, int)):
                logger.warn(f"Emoji {emoji} is not a valid discord emoji")
            if type(value) is not int:
                logger.warn(f"Karma value {value} is not a valid value (expected int)")
