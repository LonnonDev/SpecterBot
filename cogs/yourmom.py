import time
import json
import random
import math
import discord
import os
import sys
import datetime
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
from discord.ext import tasks, commands
from discord.ext.commands.cooldowns import BucketType
try:
	source = 'C:\SpecterBot'
	os.chdir('C:\SpecterBot')
except:
	source = 'C:\SpecterBot'
	os.chdir('C:\SpecterBot')

class yourmom(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
def setup(bot):
	print("your mom")
	bot.add_cog(yourmom(bot))