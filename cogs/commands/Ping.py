from cogs.commands.AbstractCommandCog import CommandCog
from discord.ext import commands


class Ping(CommandCog):
    name = "ping"
    description = "Check to see if the bot is online."
    usage = "ping"
    aliases = ["pg"]

    def __init__(self):
        super().__init__()

    @commands.command(name=name)
    async def ping(self, ctx: commands.Context):
        await ctx.send("Pong!")


def setup(bot):
    bot.add_cog(Ping())
