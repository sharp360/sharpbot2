import asyncio
import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import youtube_dl
from discord.ext import commands, tasks
from discord import Member
from discord import Activity, ActivityType
from discord.ext.commands import has_permissions, MissingPermissions
from itertools import cycle
import time
import random
from discord import Game
import os
import urbandictionary
import ffmpeg
import sys
if not discord.opus.is_loaded():
    discord.opus.load_opus('libopus.so')

#client = commands.Bot(command_prefix = '/')
bot = commands.Bot(command_prefix = '$')
bot.remove_command('help')
initial_extensions = ['cogs.musicbot']
if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    await bot.change_presence(activity=Activity(name=f"{len(bot.guilds)} servers", 
                                                type=ActivityType.watching))
    print('Ебать работаит')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Bot commands", color=0xa640cc)


    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/605243405622181912/673959848219770930/esdsfodifsdpdonpdkee.png")
    
    embed.add_field(name="$clear", value="Clear messages", inline=True)
    embed.add_field(name="$kick", value="Kick", inline=True)
    embed.add_field(name="$ban", value="Ban", inline=True)
    embed.add_field(name="$unban", value="Unban", inline=True)
    embed.add_field(name="$dice", value="Dice", inline=True)
    embed.add_field(name="$coinflip", value="Coinflip", inline=True)
    embed.add_field(name="$invite", value="Bot invite link", inline=True)
    embed.add_field(name="$urbandic", value="Random definition from urbandictionary.com", inline=True)
    embed.add_field(name="$help_music", value="Music bot commands", inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def help_music(ctx):
    embed=discord.Embed(title="Music bot commands", color=0xa640cc)

    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/605243405622181912/673959848219770930/esdsfodifsdpdonpdkee.png")

    embed.add_field(name="$play (url)", value="Play a song(Alias =$p)", inline=True)
    embed.add_field(name="$join", value="Join voice channel(Alias =$connect", inline=True)
    embed.add_field(name="$leave", value="Leave voice channel(Alias =$l)", inline=True)
    embed.add_field(name="$pause", value="Pause a song", inline=True)
    embed.add_field(name="$stop", value="Stop a song(disconnects bot from VC)", inline=True)
    embed.add_field(name="$unpause", value="Unpause(Alias =$resume)", inline=True)
    embed.add_field(name="$skip", value="Skip a song", inline=True)
    embed.add_field(name="$playlist", value="View song playlist", inline=True)
    embed.add_field(name="$currentsong", value="Current playing song(Alias =$np)", inline=True)
    embed.add_field(name="$volume", value="Change volume(Alias =$vol)", inline=True)

    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    print("$invite")
    await ctx.send("https://bit.ly/2K6B5t4")


@bot.command()
async def ping(ctx):
    print("$ping")
    latency = bot.latency
    await ctx.send(latency)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    print("$clear")
    if amount > 50:
            await ctx.send(f'Message ammount should not be more than 50')
    else:
        deleted = await ctx.channel.purge(limit=amount)
        embed = discord.Embed(
            title=(f"Deleted {len(deleted)} messages"),
            colour=discord.Colour.purple()
        )

        embed.set_image(url='https://images-ext-2.discordapp.net/external/iNUSwqRS_5uayhN_Ll-L77uMw3DmfbmxjGiQHW2SPfs/https/images-ext-1.discordapp.net/external/gBJyiZcKW6r9rmZEkB20m-cLOda3C2u1IDGeQ959mwc/https/media.discordapp.net/attachments/296056831514509312/724331512761286677/image0.gif')

        await ctx.send(embed=embed, delete_after=20)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    print("$kick")
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} was kicked')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    print("$ban")
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} was banned')

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    print("$unban")
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} was unbanned')
            return

@bot.command()
async def dice(ctx):
    print("$dice")
    responses = ['1', '2', '3', '4', '5', '6']
    await ctx.send(random.choice(responses))

@bot.command()
async def megadice(ctx):
    print("$megadice")
    responsus = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33',
                 '34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64',
                 '65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95',
                 '96','97','98','99','100']
    await ctx.send(random.choice(responsus))

@bot.command()
async def coinflip(ctx):
    print("$coinflip")
    coin = ['Орел','Решка']
    await ctx.send(random.choice(coin))

@bot.command(aliases=['ud'])
async def urbandic(ctx):
        ran = urbandictionary.random()
        limit = 1
        print("Random definition from urbandictionary.com")
        for r in ran:
            while limit != 0:
                await ctx.send("Слово: " + r.word + " | " + "Значение: " + r.definition)
                limit -= 1

@bot.command(aliases=['s'])
@commands.is_owner()
async def say(ctx, *, arg):
    await ctx.channel.purge(limit=1)
    await ctx.send(arg)


bot.run(os.environ['BOT_TOKEN'])