import flask 
from flask import Flask, redirect, render_template, request
from flask_socketio import send, SocketIO
import socketio

from pypresence import Presence
import time

import os 
import sys 

import requests 
import json

import colorama 
from colorama import init, Fore 
if os.name == 'nt':
    init(convert=True) # Windows users need this option to get their colors working

sio = socketio.Client()

client_id = open("application_id.txt", "r").read()
RPC = Presence(client_id=client_id)
RPC.connect()

@sio.on('stream')
def ok(data):
    print(f"Now streaming {data[0]} with {data[1]}")
    RPC.update(
        state=data[0], details=data[1],
    )



if __name__ == '__main__':
	sio.connect('http://127.0.0.1:5000')