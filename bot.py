import asyncio
import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import youtube_dl
from discord.ext import commands, tasks
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from itertools import cycle
import time
import random
from discord import Game
import os
import urbandictionary

#client = commands.Bot(command_prefix = '/')
bot = commands.Bot(command_prefix = '/')
#client.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status, activity=discord.Game('Команды /help'))
    print('Ебать работает')
    
#@client.command()
async def help(ctx):
    await ctx.send("Доступные команды: /clear, /зачистка - Как /clear, только удаляет 100 сообщений, /kick (Ник#0000), /ban (Ник#0000), /unban (Ник#0000) /dice - Рандомное число от 1 до 6, /megadice - Рандомное число от 1 до 100, /coinflip - Орел и решка, /invite - Пригласить бота на сервер, /ping - Пинг бота. Наверное")

@bot.command()
async def invite(ctx):
    await ctx.send("https://bit.ly/2K6B5t4")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount: int):
    deleted = await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
        title=(f"Удалено {len(deleted)} сообщений"),
        colour=discord.Colour.purple()
    )
  
    embed.set_image(url='https://cdn.discordapp.com/attachments/624937083605352469/635196301780320271/Dz-A-4aQgiY.jpg')

    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(latency)

@bot.command()
@commands.has_permissions(manage_messages=True)
async def зачистка(ctx):
    await ctx.channel.purge(limit=100)
    embed = discord.Embed(
        title='Произошла зОчистка',
        colour=discord.Colour.purple()
    )
    
    embed.set_image(url='https://cdn.discordapp.com/attachments/447540683574738952/589700786338922509/image0-11-1.jpg')

    await ctx.send(embed=embed)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} Подсрачником отправлен в Украину')

@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} Отправился на банановые острова')

@bot.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} Был разбанен')
            return

@bot.command()
async def dice(ctx):
    responses = ['1', '2', '3', '4', '5', '6', 'пошел нахуй']
    await ctx.send(random.choice(responses))

@bot.command()
async def megadice(ctx):
    responsus = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33',
                 '34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64',
                 '65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95',
                 '96','97','98','99','100']
    await ctx.send(random.choice(responsus))

@bot.command()
async def coinflip(ctx):
    coin = ['Орел','Решка']
    await ctx.send(random.choice(coin))

@bot.command(brief="Random Urban Dictionary word '/ud'", aliases=['ud'])
async def urbandic(ctx):
        ran = urbandictionary.random()
        limit = 1
        print("Asking urbandictionary.com for a word and def.")
        for r in ran:
            while limit != 0:
                await ctx.send("Word: " + r.word + " | " + "Def: " + r.definition)
                limit -= 1

@bot.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        await channel.connect()
        
    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"Бот присоединился {channel}\n")

    await ctx.send(f"Бот присоединился в {channel}")

@bot.command(pass_context=True, aliases=['l', 'lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    
    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f"Бот вышел из {channel}")
    else:
        await ctx.send(f"Бот не находиться в голосовом канале")



bot.run(os.environ['BOT_TOKEN'])