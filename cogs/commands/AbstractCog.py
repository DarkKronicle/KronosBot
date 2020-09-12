from abc import ABC, abstractmethod, ABCMeta
from discord.ext import commands

"""
This is a class designed to make my life easier in creating commands.
It starts by creating a parent metaclass CommandMeta so we don't get any type errors.
After that we create AbstractCommand that takes in a couple variables and then form it into CommandCog.
"""

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
