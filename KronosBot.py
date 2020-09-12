from cogs.commands.Ping import Ping
from Config import Config
import traceback

import discord
from discord.ext.commands import Bot


# Can manage the different Cogs easier this way. All of these below will extend CommandCog
commands = [Ping()]

bot = Bot(command_prefix="!")

# If you're using this, exampleconfig.json has the same values just with placeholders.
config = Config("config.json")
token = config.getvalue("token")


def main():
    for extension in commands:
        try:
            print(f"Loading {extension.name}")
            bot.add_cog(extension)
            print(f"Loaded {extension.name}!")

        except (discord.ClientException, ModuleNotFoundError):
            print(f"Failed to load {extension.name}")
            traceback.print_exc()

    bot.run(token, bot=True, reconnect=True)


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")

if __name__ == '__main__':
    main()
