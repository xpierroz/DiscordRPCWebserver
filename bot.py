import quart 
from quart import Quart, redirect, render_template, request

import discord 
from discord.ext import commands
from discord.ext import ipc

import os 
import sys 

import requests 
import json

import colorama 
from colorama import init, Fore 
if os.name == 'nt':
    init(convert=True) # Windows users need this option to get their colors working

def get_token():
    with open("Configuration.$", "r") as out:
        for line in out.read().splitlines():
            if line.startswith("TOKEN = "):
                token = line.split("TOKEN = ")[1]
                return token
            
        print(f'    {Fore.YELLOW}.$ {Fore.LIGHTRED_EX}ERROR: You must put your token in Configuration.$')
        time.sleep(3)
        os.system("exit")

class xBot(commands.Bot):

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)

		self.ipc = ipc.Server(self, secret_key = "xStream")

	async def on_ready(self):
		print("Bot is ready.")

	async def on_ipc_ready(self):
		print("Ipc server is ready.")

	async def on_ipc_error(self, endpoint, error):
		print(endpoint, "raised", error)


bot = xBot(command_prefix = ">", self_bot=True)


@bot.ipc.route()
async def stream(data):
    await bot.change_presence(
        activity = discord.Streaming(
            name = data.name,
            url = data.url
        )
    )
    return True

if __name__ == '__main__':
	bot.ipc.start()
	bot.run(get_token(), bot=False)