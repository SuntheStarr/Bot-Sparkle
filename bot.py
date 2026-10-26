import os
import discord
from discord.ext import commands

# Configuração das intenções do bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Criação da instância do bot
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}!')

@bot.command()
async def ola(ctx):
    await ctx.send(f'Olá, {ctx.author.name}! Bem-vindo ao canal de Desenhos e OCs! ✨')

# Pega o token de forma segura do servidor do Render
TOKEN = os.environ.get('DISCORD_TOKEN')

bot.run(TOKEN)
