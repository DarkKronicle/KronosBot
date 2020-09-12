from cogs.commands.AbstractCog import CommandCog
from discord.ext import commands

# Base command to test the bot! Uses the fancy AbstractCog.


class Ping(CommandCog):
    name = "ping"
    description = "Check to see if the bot is online."
    usage = "ping"
    aliases = ["pg"]

    def __init__(self):
        super().__init__()

    @commands.command(name=name, aliases=aliases)
    async def ping(self, ctx: commands.Context):
        await ctx.send("Pong!")
