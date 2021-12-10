# Import Discord Package
import asyncio
from collections import UserDict, UserList, UserString
from types import GenericAlias
from datetime import datetime
import discord
from discord import FFmpegPCMAudio
from discord import player
from discord import voice_client
from discord import guild
from discord import emoji
from discord.channel import VoiceChannel
from discord.enums import VoiceRegion
import json
import os
from discord import user
from discord import message
from discord.ext import commands
from discord import colour
import random
from discord.ext.commands import bot
import youtube_dl
import asyncio
import discord.ext.commands.bot
from discord.ext.commands.converter import MemberConverter, VoiceChannelConverter
from types import GenericAlias
import discord
from discord import colour
from discord.gateway import VoiceKeepAliveHandler
from discord.member import VoiceState
from youtube_dl.utils import url_basename
# Client (our bot)
client = commands.Bot(command_prefix = '!')
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='VERIFY ROLE')
    await client.add_roles(member, role)

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user


        if(UserDict.name, UserList.discriminator) == ("member_name", "member_discriminator"):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbaned {UserString.mention}')
            return
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    reponses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(reponses)}')
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
  await ctx.channel.purge(limit=amount)
  await ctx.send("THE MESSAGES ARE DELETED!", delete_after=3)
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('!help'))
    print  ('bot is ready')
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(
      embed = discord.Embed(
        description = f"User {member} has been kicked",
        timestamp = datetime.now(),
        color = 0x5de622
      )
    )
    # Moderation commands
    # Mute commands
    await member.send(f"You have been kicked from {member.guild.name} | reason: {reason}")
@client.command()
async def invite(ctx):
    await ctx.send(
      embed = discord.Embed(
        description = ("firrd bot invite link = https://discord.com/api/oauth2/authorize?client_id=914018241112842240&permissions=8&scope=bot"),
        color = 0x5de622
      )
    )  
@client.command()
async def ishan(ctx):
    await ctx.send(
      embed = discord.Embed(
        description = ("ishan is a bot coder"),
        color = 0x5de622
      )
    ) 
@client.command()
async def arshit(ctx):
    await ctx.send(
      embed = discord.Embed(
        description = ("arshit has written bot coder but he is't a coder"),
        color = 0x5de622
      )
    )   
@client.command()
async def armaan(ctx):
    await ctx.send(
      embed = discord.Embed(
        description = ("gamer hai"),
        color = 0x5de622
      )
    )  
@client.command()
async def ronak(ctx):
    await ctx.send(
      embed = discord.Embed(
        description = ("gamer he hai but he is noob"),
        color = 0x5de622
      )
    )  
@client.command()
async def pratham(ctx):
    await ctx.send(
      embed = discord.Embed(
        description = ("pratham is very padhaku"),
        color = 0x5de622
      )
    )
@client.command()
async def hi(ctx):
    await ctx.send(
      embed = discord.Embed(
        description = ("hello"),
        color = 0x5de622
      )
    )
@client.command()
async def hello(ctx):
    await ctx.send(
      embed = discord.Embed(
        description = ("how are you"),
        color = 0x5de622
      )
    )
@client.command()
async def fine(ctx):
    await ctx.send(
      embed = discord.Embed(
        description = ("nice"),
        color = 0x5de622
      )
    )
@client.command()
async def sad(ctx):
    await ctx.send(
      embed = discord.Embed(
        description = ("oo shot"),
        color = 0x5de622
      )
    )
@client.command()
async def sharyi1(ctx):
    await ctx.send(
      embed = discord.Embed(
        description = ("Chandni raat sahil ko diwana bana deti hai… shamma parwane ko jala deti hai.. Ishaq aisi chiiz hai…jo achcho achcho ko roola deti hai…!"),
        color = 0x5de622
      )
    )
@client.command()
async def sharyi2(ctx):
    await ctx.send(
      embed = discord.Embed(
        description = ("Aahat si koi aaye to lagta hai ki tum ho Saya sa koi lehraye to lagta hai ki tum ho Ab tumhi batao tum kya kisi bhoot se kam ho?"),
        color = 0x5de622
      )
    )
@client.command()
async def sharyi3(ctx):
    await ctx.send(
      embed = discord.Embed(
        description = ("jailar :- Suna Hai Tum Shayar Ho Kuch Sunao Yaar Qaidi:- Gum-E-Ulfat Mein Jo Zindagi Kati Hai Hamari Jis Din Jamanat Huyi Hamari Us Din Zindagi Khatam Tumhari…."),
        color = 0x5de622
      )
    )
@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('schedulen.wav')
        player - voice.play(source)
    else:
          await ctx.send("you are not in a voice channel, you must be in a voice channel to run this command!")
@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice channel")
    else:
        await ctx.send("I am not in a voice channel")

@client.command(pass_context=True)
async def play(ctx, url : str):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()

        # download the youtube video
        ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          ydl.download([url])
        for file in os.listdir("./"):
          if file .endswidth(".mp3"):
           os.rename(file, "song.mp3")

          source = FFmpegPCMAudio('song.mp3')
          player - voice.play(source)

        else:
            await ctx.send("you are not in a voice channel, you must be in a voice channel to run this command!")

@client.command(pass_context=True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients,guild-ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("at the moment, there is no audio playing in the voice channel!")


@client.command(pass_context=True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients,guild=ctx.guild)
    if voice.is_playing():
        voice.resume()
    else:
        await ctx.send("at the moment, there is no song is paused!")

client.run('OTE0MDE4MjQxMTEyODQyMjQw.YaG70g.XQ8WTW4WtJcOb7iRxJNck_4Ztzk')