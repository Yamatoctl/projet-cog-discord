import discord # bibliothèque discord.py, elle gère toute la communication avec l'API Discord.
from discord.ext import commands # Importe le système de commandes (!ask, !help...) 
from dotenv import load_dotenv # Importe la fonction qui va lire le fichier .env pour charger les variables secrètes (token Discord).
import asyncio # mode asynchrone (plusieurs tâches en parallèle)
import os # permet de lire les variables d'environnement système.

load_dotenv() # Lit le fichier .env et charge ses variables en mémoire. Sans cette ligne, os.getenv('TOKEN') retournerait None.

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connecté : {bot.user}')

async def main():
    async with bot:
        # await bot.load_extension('cogs.llm')  # charge le cog LLM
        await bot.load_extension('cogs.python')
        await bot.start(os.getenv('TOKEN'))

asyncio.run(main()) # 