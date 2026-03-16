# import discord # bibliothèque discord.py, elle gère toute la communication avec l'API Discord.
# from discord.ext import commands # Importe le système de commandes (!ask, !help...) 
# from dotenv import load_dotenv # Importe la fonction qui va lire le fichier .env pour charger les variables secrètes (token Discord).
# import asyncio # mode asynchrone (plusieurs tâches en parallèle)
# import os # permet de lire les variables d'environnement système.

# load_dotenv() # Lit le fichier .env et charge ses variables en mémoire. Sans cette ligne, os.getenv('TOKEN') retournerait None.

# intents = discord.Intents.default()
# intents.members = True
# intents.message_content = True

# bot = commands.Bot(command_prefix='', intents=intents)

# @bot.event
# async def on_ready():
#     print(f'Bot connecté : {bot.user}')

# async def main():
#     async with bot:
#         # await bot.load_extension('cogs.llm')  # charge le cog LLM
#         await bot.load_extension('cogs.python_commands')
#         await bot.start(os.getenv('TOKEN'))

# asyncio.run(main()) # 

import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
# GUILD_ID = int(os.getenv("GUILD_ID"))


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True

        super().__init__(
            command_prefix=commands.when_mentioned_or("!"),
            intents=intents
        )

    async def setup_hook(self):
        # await self.load_extension("cogs.fun")
        # await self.load_extension("cogs.pause")
        await self.load_extension("cogs.python_commands")
        # guild = discord.Object(id=GUILD_ID)
        # self.tree.copy_global_to(guild=guild)
        # await self.tree.sync(guild=guild)
        

    async def on_ready(self):
        print(f"connected as {self.user}")


async def main():
    bot = Bot()
    await bot.start(TOKEN)


asyncio.run(main())