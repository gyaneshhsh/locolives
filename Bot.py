import random
import requests
import asyncio
from discord import Game
from discord.ext.commands import Bot
import discord
from discord.ext import commands
import random
import aiohttp
import csv
from pathlib import Path
import json
import os
import datetime
from datetime import datetime
from os import listdir
from os.path import isfile, join
import string
import time
import threading
import numbers
##import Tools


owner = ["535771434060873729","488569887342723073","532783109935071243","487227923053543447","497047989433663488","538685291469209601"]

global stocksloco
stocksloco = 500
global checkbuycmd
checkbuycmd = "ON"
global dis
dis = 0

client = Bot(command_prefix=".")
client.remove_command('help')

cwd = os.path.dirname(os.path.realpath(__file__))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='with Loco Lives!'))
    print("Logged in as " + client.user.name)
    print("Get Loco Lives!")

@client.command(pass_context=True)
async def clear(ctx, amount = 100):
	msg = await client.say("role...")
	role1 = discord.utils.get(msg.server.roles, name = 'Staff')
	await client.delete_message(msg)
	if ctx.message.author.id in owner:
		pass
	elif role1 in ctx.msg.server.roles:
		pass
	else:
		return
	channel = ctx.message.channel
	messages = []
	async for message in client.logs_from(channel, int(amount)):
		messages.append(message)
	await client.delete_messages(messages)


@client.command(pass_context=True,aliases=['stocks'])
async def stock(ctx):
    embed = discord.Embed(title="Loco Stock", description=str(stocksloco) + " :heart: ", color=0x5761ee, inline=True)
    embed.set_thumbnail(url="http://i.imgur.com/8bNf82p.jpg")
    embed.set_footer(text="Lives Lives")
    await client.say(embed=embed)
    


@client.command(pass_context = True, aliases=['point','credits','credit'])
async def points(ctx):
    author = ctx.message.author
    tapauthor = ctx.message.author.mention
    print(author)
    with open(cwd + '/points.json', 'r') as f:
        users = json.load(f)

        await add_data(users, author)

        await user_points(users, author, tapauthor)
     


        with open(cwd + '/points.json', 'w') as f:
            json.dump(users, f)

async def add_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['points'] = 0   

async def user_points(users, user, tapauthor):
    name = user.name
    points = users[user.id]['points']
    print(points)

    await client.say("You have **{} points**.".format(points))


@client.command(pass_context=True, aliases=['loco'], no_pm=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def life(ctx, lives=None, refercode=None):
    global stocksloco
    if stocksloco == 0:
        await client.say("**Oh no! Looks like the stock is empty** :frowning:")
        return
    elif stocksloco < 0:
        await client.say("**Oh no! Looks like the stock is empty** :frowning:")
        return
    if refercode is None:
        await client.say(" Correct Use:" + "\n" + "`.life amount referral`")
        return
    abcd = lives
    print(abcd)
    if str(abcd).startswith("0"):
        return await client.say("Number of Lives can't begin with `0` lol")
    if lives is None:
        await client.say("Correct use: \n `.life amount referral`")
    else:
        lives = int(lives)
    if stocksloco < lives:
        await client.say("**Low stock**")
        return
    else:
    	pass


    url = "http://sl-api.getloconow.com/v1/search/"
    querystring = {"q":str(refercode)} 
    headers = {
        'x-auth-token': "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNoZXRhbjE3MjgiLCJ1c2VyX3VpZCI6IjhIR1M3TFVJNE0iLCJsYW5ndWFnZSI6MSwicHJvZmlsZV92ZXJzaW9uIjoyLCJpc19mYWtlIjpmYWxzZSwiaXNfc3RhZmYiOmZhbHNlfQ.J2f_4b3v-oYeeNoXLm411rEF3g9D85OaySDjQewpmt8",
        'user-agent': "Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G9350 Build/LMY48Z)"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    try:
        userid = json.loads(response.text)[0]["user_uid"]
        print(userid)
        username = json.loads(response.text)[0]["username"]
        print(username)
        pass
    except:
        await client.say("**wrong ref code**")
        return

    user = ctx.message.author
    with open(cwd + '/points.json', 'r') as f:
        users = json.load(f)
        try:
            points = users[user.id]['points']
            print(points)
        except:
            points = 0
        if points == 0:
            await client.say("**You don't have enough points!**")
            return
        elif points < 0:
            await client.say("** You don't have enough points!**")
            return
        elif points < lives:
            await client.say("**You don't have enough points!**")
            return
        else:
            pass

    
    msg = await client.say("**Starting...**")
                
    with open(cwd + '/points.json', 'r') as f:
        users = json.load(f)
        author = ctx.message.author
                                        
        await took_points(users, author, msg, refercode, lives)
                    
        with open(cwd + '/points.json', 'w') as f:
                        
            json.dump(users, f)
                    
async def took_points(users, user, msg, refercode, lives):
    users[user.id]['points'] -= lives
    points = users[user.id]['points']
    name = user.name
    print(name)
    print(points)
    print(user.id)
    ab = lives*1540

    msg1 = await client.edit_message(msg, "**Sending {} Coins ({} :heart:) to `{}`...**".format(ab, lives, refercode))

    global stocksloco
    stocksloco -= lives
    
    await client.edit_message(msg1, "**Your {} Coins ({} :heart:) have been sent to `{}`!**".format(ab, lives,refercode))
   
@client.command(pass_context = True, no_pm=True)
async def add(ctx, times : int, userName: discord.User):
    if ctx.message.author.id not in owner:
        return
    else:
        pass
    author = ctx.message.author
    print(author)
    
    await client.send_message(userName, "You just got **{} points**!".format(times))
    
    msg = await client.say("**Adding...**")
    await client.delete_message(msg)
    with open(cwd + '/points.json', 'r') as f:
        users = json.load(f)


        await update_data(users, userName)

        await add_points(users, userName, times, author)


        with open(cwd + '/points.json', 'w') as f:
            json.dump(users, f)

async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['points'] = 0

async def add_points(users, user, exp, author):
    users[user.id]['points'] += exp
    points = users[user.id]['points']
    name = user.name
    print(name)
    print(points)
    print(user.id)
    print(exp)
    await client.say("{} gave `{}` points to {}!".format(author, exp, name))


client.run("NTM4NTc2NzI3NzU3MDI5Mzk3.Dy10Rw.qlh7uPc_zfUI2uuq2OXe92PYyYI")
