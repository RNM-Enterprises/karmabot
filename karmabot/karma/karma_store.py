import pickle as pkl
from aiofile import async_open
from discord.ext import tasks
from os import path
from collections.abc import MutableMapping


class KarmaStore(MutableMapping[int, int]):
    __store: dict[int, int]

    def __init__(self, filename: str, interval: int = 1):
        self.filename = filename

        # load internal state if file already exists
        if path.exists("filename"):
            self.load()
        # if not, can just start from empty

        self.bgsave.change_interval(minutes=interval)
        self.bgsave.start()

    async def save(self):
        """
        Save internal store to file
        """
        raw_data = pkl.dumps(self.__store)
        async with async_open(self.filename, "wb") as f:
            await f.write(raw_data)

    def load(self):
        """
        Replace current internal store with file contents
        """
        with open(self.filename, "rb") as f:
            raw_data: bytes = f.read()
        loaded_data = pkl.loads(raw_data)

        # we could have loaded literally fucking anything
        # validate it
        if isinstance(loaded_data, dict) and all(
            isinstance(k, int) and isinstance(v, int) for (k, v) in loaded_data.values()
        ):
            self.__store = loaded_data
        else:
            raise TypeError(
                f"Object loaded from {self.filename} is not valid karma data"
            )

    @tasks.loop()
    async def bgsave(self):
        """
        Background loop to periodically save file to disk
        """
        await self.save()
