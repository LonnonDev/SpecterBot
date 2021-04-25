import time
import json
import random
import math
import discord
import os
import sys
import sqlite3
# import secrets
import discord
import datetime
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from os import listdir
import datetime
import asyncio
from config import *
try:
	source = 'C:\SpecterBot'
	os.chdir('C:\SpecterBot')
except:
	source = 'C:\SpecterBot'
	os.chdir('C:\SpecterBot')

commandprefix = ["sb!","SB!"]

intents = discord.Intents.all()

bot = commands.AutoShardedBot(case_insensitive=True, command_prefix=commands.when_mentioned_or(*commandprefix), intents=intents)
owner = bot.get_user(835921524309360710)

#stuff	

@bot.command()
async def reload(ctx, cog : str = 'all'):
	if ctx.author.id == 835921524309360710:
		if cog == 'all':
			path = f'{source}/cogs'
			cogs = []
			for f in listdir(path):
				file = f"cogs.{f}".replace('.py', '')
				cogs += [file]
			cogs.remove('cogs.__pycache__')
			for extension in cogs:
				bot.load_extension(extension)
		else:
			initial_extensions = [f'cogs.{cog}']
			for extension in initial_extensions:
				bot.reload_extension(extension)
			await ctx.send(f"Reloaded {cog}.py")

cogs = []
try:
	path = f'{source}/cogs'
	for f in listdir(path):
		file = f"cogs.{f}".replace('.py', '')
		cogs += [file]
	cogs.remove('cogs.__pycache__')
except:
	pass

for extension in cogs:
	bot.load_extension(extension)

print('ready')
bot.run(config)