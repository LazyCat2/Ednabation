import \
	discord, \
	json, \
	asyncio, \
	random, \
	threading as th, \
	requests

from datetime import datetime as time
from discord.ext import commands
from generator import generate

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="sudo ")
config = json.load(open('config.json'))

INFO = "INFO"
WARN = "WARN"

@bot.event
async def on_ready():
	print('Connected')

@bot.event
async def on_disconnect():
	print("Disconnected")

@bot.command(name="t9")
async def t9_(ctx, start=None):
	await ctx.reply(generate(start)[0:2000], allowed_mentions=discord.AllowedMentions(users=[], roles=[], everyone=False))

bot.run(config['token'])