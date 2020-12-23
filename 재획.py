import discord
import asyncio
import youtube_dl
import re
import sys
import os
from discord.ext import commands
import urllib
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import warnings
import requests
import time

client = discord.Client()

@client.event # Use these decorator to register an event.
async def on_ready(): # on_ready() event : when the bot has finised logging in and setting things up
    await client.change_presence(status=discord.Status.online, activity=discord.Game("숫자 세기"))
    print("New log in as {0.user}".format(client))

@client.event

async def on_message(message):

    id = message.author.id

    mchannel = message.channel

    if message.content.startswith('!재획'):

        sec = 7200

        if (id == 289974891975802880):
            id = '이냐'
        if (id == 275507005916053504):
            id = '천준'
        if (id == 277449752398790657):
            id = '루얀'
        if (id == 482927663644934154):
            id = '룬찌'
        if (id == 283846760919597057):
            id = '박진수'
        if (id == 320143261203169280):
            id = '민준'
        if (id == 264980104675852291):
            id = '유화'
        if (id == 585466210607562774):
            id = '매히'

        for i in range(sec, 0, -1):
            time.sleep(1)
            if (i % 180 == 0):
                 await message.channel.send(str(id)+" 쓸심 써")
            if (i % 1800 == 0):
                 await message.channel.send(str(id)+" 경험치 도핑 다시해")
        else:
            await message.channel.send(str(id)+" 재획 끝났어 수고했어~")

client.run('NzkxMjQyMDU2OTk1MzA3NTMx.X-MTlg.GiA4k2K1KXrrYI_BDxyuljusXCQ')