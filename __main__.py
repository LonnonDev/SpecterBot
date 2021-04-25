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
from token import *

commandprefix = ["a!","A!"]

intents = discord.Intents.all()

bot = commands.AutoShardedBot(case_insensitive=True, command_prefix=commands.when_mentioned_or(*commandprefix), intents=intents)

@bot.event
async def on_ready():
	print('ready')
bot.run(token)