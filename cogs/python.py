import discord # pont entre code python et API discord
from discord.ext import commands # ext. pour extension, importe seulement le sous module commands 
from data.python_commands import PYTHON_COMMANDS # veut dire, va dans dossier data, ouvre python_commands.py et importe seulement la var. PYTHON_COMMAND

# Menu déroulant : liste toutes les fonctions 
class PythonSelect(discord.ui.Select): # une methode est une fonction qui appartient à une classe
    def __init__(self): # methode de construction du menu déroulant avant que l'user clique
        options = [
            discord.SelectOption(label=cmd["name"], value=str(i)) # objet représentant une ligne dans le menu déroulant
            for i, cmd in enumerate(PYTHON_COMMANDS)
        ]
        super().__init__(placeholder="Choisir une fonction...", options=options) # construit le menu déroulant visible à l'écran

    async def callback(self, interaction: discord.Interaction): # 2eme methode, s'exécute après que l'utilisateur a fait son choix. c'est la réaction au clic
        try:
            cmd = PYTHON_COMMANDS[int(self.values[0])]

            embed = discord.Embed(title=f"`{cmd['name']}`", description=cmd["description"], color=0x3498db)
            embed.add_field(name="Description", value=cmd["details"], inline=False)
            embed.add_field(name="Exemple", value=f"```python\n{cmd['example']}\n```", inline=False)
            embed.add_field(name="Documentation officielle", value=f"[docs.python.org]({cmd['doc']})", inline=False)

            await interaction.response.edit_message(embed=embed, view=PythonView())

        except Exception as e:
            await interaction.response.send_message(f"❌ Une erreur est survenue : {e}", ephemeral=True)

#  Vue contenant le menu (timeout 120s) 
class PythonView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=120)
        self.add_item(PythonSelect())

    async def on_timeout(self):
        
        for item in self.children:
            item.disabled = True

# Vue principale : bouton d'entrée (timeout 60s) 
class MainView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)

    async def on_timeout(self):
        # Désactive le bouton quand il expire (après 60s)
        for item in self.children:
            item.disabled = True

    @discord.ui.button(label="Fonctions built-in Python", style=discord.ButtonStyle.primary)
    async def open_menu(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="Fonctions built-in Python",
            description="Sélectionne une fonction dans le menu ci-dessous.",
            color=0x3498db
        )

        await interaction.response.send_message(embed=embed, view=PythonView(), ephemeral=True) # ephemeral=True rend le message visible uniquement par l'utilisateur qui a cliqué

# Cog : regroupe la commande python 
class Python(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def python(self, ctx: commands.Context):
        """Affiche les fiches des fonctions built-in Python."""
        embed = discord.Embed(
            title="Fonctions Built-in Python",
            description=(
                "Explore les fonctions built-in les plus utilisées en Python.\n"
                "Chaque fiche inclut une description, un exemple et la doc officielle.\n\n"
                "Clique sur le bouton ci-dessous pour commencer !"
            ),
            color=0x3498db
        )
        embed.set_image(url="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnFieGRuNWcwbjdkcHluNzJoemNpaWRpcXQ4Y3lrMnVnNDdkYzJvZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/coxQHKASG60HrHtvkt/giphy.gif")
        await ctx.send(embed=embed, view=MainView())

# ── Chargement du Cog par main.py ─────────────────────────────────────────────
async def setup(bot: commands.Bot):
    await bot.add_cog(Python(bot))