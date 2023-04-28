import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}')

@bot.command()
async def number(ctx, *choices: '0, 1, 2, 3, 4, 5, 6, 7, 8, 9'):
    await ctx.send(random.choice(choices))

@bot.command()
async def help(ctx):
    await ctx.send(f'привет всем! если вы напишете: $number -- для генерирования случайного числа от 0 до 9 {bot.user}')

bot.run("") 