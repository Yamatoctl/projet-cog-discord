import discord
from discord.ext import commands
import aiohttp
import json

class LLM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.url = "http://localhost:11434/api/generate"
        self.model = "ministral-3"
        self.generating = {}

    @commands.command()
    async def ask(self, ctx, *, question: str):
        self.generating[ctx.author.id] = True
        msg = await ctx.send("⏳ Je réfléchis...")

        answer = ""
        i = 0

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.url, json={
                    "model": self.model,
                    "prompt": question,
                    "stream": True
                }) as response:

                    async for line in response.content:
                        if not self.generating.get(ctx.author.id):
                            await msg.edit(content=f"🤖 {answer[-1900:]}\n\n⛔ Génération annulée.")
                            return

                        line = line.strip()
                        if line:
                            try:
                                chunk = json.loads(line)
                                answer += chunk.get("response", "")
                                i += 1
                                if i % 10 == 0:
                                    await msg.edit(content=f"🤖 {answer[-1900:]}")
                            except json.JSONDecodeError:
                                continue

            await msg.edit(content=f"🤖 {answer[-1900:]}")

        except aiohttp.ClientConnectorError:
            await msg.edit(content="❌ Impossible de joindre Ollama. Est-il bien démarré sur le port 11434 ?")

        except Exception as e:
            await msg.edit(content=f"❌ Erreur inattendue : `{e}`")

        finally:
            self.generating[ctx.author.id] = False

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if self.generating.get(message.author.id):
            self.generating[message.author.id] = False
        # process_commands retiré — commands.Bot le gère automatiquement

async def setup(bot):
    await bot.add_cog(LLM(bot))