import yaml
import logging
import re


class Config:

    __slots__ = ["__logger", "__filename", "BOT_TOKEN", "OWNERS", "emoji"]

    def __init__(self, file: str):
        self.__filename = file
        self.__logger = logging.getLogger("karmabot.config")

        with open(file, "r") as f:
            parsed = yaml.safe_load(f)

        self.BOT_TOKEN: str = parsed.get("bot_token")
        self.OWNERS: list[int] = parsed.get("owners")
        self.emoji: dict[str | int, int] = parsed.get("emoji")
        self.check_config()

    def check_config(self):
        if self.BOT_TOKEN is None:
            self.__logger.critical("No bot token defined in config, exiting...")
            exit()

        for id in self.OWNERS:
            if type(id) is not int or not re.match(r"^\d{17,18}$", str(id)):
                self.__logger.warn(f"User ID {id} is not a valid discord user id")

        for (emoji, value) in self.emoji.items():
            if not (isinstance(emoji, str) or isinstance(emoji, int)):
                self.__logger.warn(f"Emoji {emoji} is not a valid discord emoji")
            if type(value) is not int:
                self.__logger.warn(
                    f"Karma value {value} is not a valid value (expected int)"
                )

    def save(self):
        config_map = {
            attr.lower(): self.__getattribute__(attr) for attr in self.__slots__[2:]
        }
        with open(self.__filename, "w") as f:
            yaml.dump(
                config_map, stream=f, default_flow_style=False, allow_unicode=True
            )
        self.__logger.info(f"Saved config to {self.__filename}")
