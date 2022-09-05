from typing import Sized, SupportsIndex

import discord 
import time
import random
from datetime import datetime
import asyncio

from PIL import Image 
from io import BytesIO
from discord.abc import User
from discord.client import Client
from discord.member import Member
 
import requests

from discord import asset
from discord import activity
from discord.activity import Activity, BaseActivity, CustomActivity, Game, Spotify, create_activity
from discord.enums import ActivityType
from discord.ext import commands

client = commands.Bot(command_prefix=commands.when_mentioned_or('*'))

@client.event
async def on_ready():
    print(">>Bot is online<<")
    print(client.user.name)
    print(client.user.id)

@client.command()
async def view_emojis(ctx):
    emo = ctx.guild.emojis
    print(type(emo))
    for i in emo:
        print(i)

@client.command()
async def pornhub(ctx):
 a = random.randrange(1, 1000)
 a = format('{0:04d}'.format(a))
 await ctx.send(f"http://porngif.cz/gif/ze%20predu/{a}.gif")  

@client.command()
async def wallpaper(ctx):
 a =random.randrange(1,600000)
 a=format('{0:06d}'.format(a))
 await ctx.send(f"https://wall.alphacoders.com/big.php?i={a}")

@client.command()
async def hi(ctx):
 t1 = '12:00'
 t2 = '18:00'
 t3 = '06:00'
 t4 = '00:00'
 
 now = datetime.now().hour
 
 if now >= 18:
     testt = "早上好 現在時間" + t2
 elif now >= 12:
     testt = "午安 現在時間" + t1
 elif now >= 6:
     testt = "早上好 現在時間" + t3
 else:
     testt = "凌晨了 現在時間" + t4
     
 await ctx.send(testt) 
 
 

@client.command()
async def avatar(ctx, *, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url
    await ctx.send(userAvatar)

@client.command()
async def 角色卡(ctx, *, member:discord.Member=None):
 author = ctx.author
 usr=ctx.author.created_at
 grp=ctx.guild.created_at
 pfp = author.avatar_url
 ur1=ctx.author
 sta=ctx.author.stats
 t1 = '12:00'
 t2 = '18:00'
 t3 = '06:00'
 t4 = '00:00'
 now = datetime.now().strftime("%H:%M")
 testt="123123"
 if t3 <= now < t1:
     testt="早上好 現在時間:"+now
 if t1 <= now < t2:
     testt="午安 現在時間:"+now
 if t2 <= now:
     testt="晚安 現在時間:"+now
 if t4 <= now < t3:
     testt="凌晨了 現在時間:"+now    
 embed=discord.Embed(title="角色卡", color=0xffadca)
 embed.add_field(name="姓名", value=ur1, inline=False)
 embed.set_thumbnail(url=pfp)
 embed.add_field(name="您的帳號創建日期", value=usr, inline=True)
 embed.add_field(name="伺服器創建日期", value=grp, inline=True)
 embed.add_field(name="溫馨問候", value=testt, inline=False)
 embed.add_field(name=":butterfly:您的資訊如上:butterfly:", value=sta, inline=False)
 await ctx.send(embed=embed)


@client.command()
async def wanted(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author
    wanted = Image.open("wanted.jpg")
    asset = member.avatar_url_as(format="jpg",size = 128)
    data = BytesIO(await asset.read())
    profilepic = Image.open(data)
    profilepic = profilepic.resize((306,306))
    wanted.paste(profilepic,(68,143))
    wanted.save("wantedpic.jpg")
    await ctx.send(file = discord.File("wantedpic.jpg"))

@client.command()
async def RIP(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author
    RIP = Image.open("RIP.jpg")
    asset = member.avatar_url_as(format="jpg",size = 128)
    data = BytesIO(await asset.read())
    profilepic = Image.open(data)
    profilepic = profilepic.resize((422,491))
    RIP.paste(profilepic,(531,1230))
    RIP.save("RIPIC.jpg")
    await ctx.send(file = discord.File("RIPIC.jpg"))

@client.command()
async def 燒(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author
    RIP = Image.open("spog.jpg")
    asset = member.avatar_url_as(format="jpg",size = 128)
    data = BytesIO(await asset.read())
    profilepic = Image.open(data)
    profilepic = profilepic.resize((188,233))
    RIP.paste(profilepic,(53,87))
    RIP.save("spog1.jpg")
    await ctx.send(file = discord.File("spog1.jpg"))

    
client.run('')
