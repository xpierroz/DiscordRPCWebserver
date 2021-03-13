import quart 
from quart import Quart, redirect, render_template, request, flash

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

                    
app = Quart('Discord Streaming Status')
ipc_client = ipc.Client(secret_key = "xStream")

@app.route("/", methods=["GET", "POST"])
async def home():
    succes = None
    if request.method == "POST":
        data = await request.form
        name = data["sname"]
        url = data["surl"]
        try:
            r = requests.get(url)
        except:
            return await render_template("error.html", name=name)
        if r.status_code == 404:
            return await render_template("error.html", name=name)
        await ipc_client.request("stream", name=name, url=url)
        return await render_template("succes.html", name=name)
    if request.method == "GET":
        return await render_template("index.html")

if __name__ == '__main__':
    app.run()
