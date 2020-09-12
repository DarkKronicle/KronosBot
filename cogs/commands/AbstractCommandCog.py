from abc import ABC, abstractmethod, ABCMeta
from discord.ext import commands


class CommandMeta(commands.CogMeta, ABCMeta):
    pass


class AbstractCommand(ABC, metaclass=CommandMeta):

    def __init__(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def description(self):
        pass

    @property
    @abstractmethod
    def usage(self):
        pass

    @property
    @abstractmethod
    def aliases(self):
        return


class CommandCog(commands.Cog, AbstractCommand, ABC, metaclass=CommandMeta):
    pass
