import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext import commands, tasks
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from itertools import cycle
import time
import random
from discord import Game
import os

client = commands.Bot(command_prefix = '/')
client.remove_command('help')
status = cycle(['Команды /help'])

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    ctx.send('Cog Загружен, а Cat лох')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    ctx.send('Cog Выгружен, а Cat лох')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Для импортарования кога
#class Sharp(commands.Cog):
#
#   def __init__(self, client):
#      self.client = client
#
#def setup(client):
#    client.add_cog(Sharp(client))


@client.event
async def on_ready():
    chang_status.start()
    print('Ебать работает')

@tasks.loop(seconds=0.5)
async def chang_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def sstatus(ctx):
    await ctx.send("1.0")

@client.command()
async def help(ctx):
    await ctx.send("Доступные команды: /clear, /зачистка - Как /clear, только удаляет 100 сообщений, /kick (Ник#0000), /ban (Ник#0000), /unban (Ник#0000) /dice - Рандомное число от 1 до 6, /megadice - Рандомное число от 1 до 100, /coinflip - Орел и решка, /invite - Пригласить бота на сервер, /ping - Пинг бота. Наверное")

@client.command(pass_context=True)
async def say(ctx, *, text: str=None):
    if ctx.message.author.id == 203634439673217024:
        await ctx.message.delete()
        return await ctx.send(text)

@client.command()
async def invite(ctx):
    await ctx.send("https://bit.ly/2K6B5t4")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, ammount=6):
    await ctx.channel.purge(limit=ammount)
    embed = discord.Embed(
        title='Сообщение удалено',
        colour=discord.Colour.green()
    )
    
    embed.set_image(url='https://cdn.discordapp.com/attachments/447540683574738952/588744831539347468/me_irl.gif')

    await ctx.send(embed=embed)

@client.command()
async def ping(ctx):
    latency = client.latency
    await ctx.send(latency)

@client.command()
@commands.has_permissions(manage_messages=True)
async def зачистка(ctx):
    await ctx.channel.purge(limit=100)
    embed = discord.Embed(
        title='Произошла зОчистка',
        colour=discord.Colour.green()
    )
    
    embed.set_image(url='https://cdn.discordapp.com/attachments/447540683574738952/589700786338922509/image0-11-1.jpg')

    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} Подсрачником отправлен в Украину')

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} Отправился на банановые острова')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} Вернулся с банановых островов')

@client.command()
async def dice(ctx):
    responses = ['1', '2', '3', '4', '5', '6', 'пошел нахуй']
    await ctx.send(random.choice(responses))

@client.command()
async def megadice(ctx):
    responsus = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33',
                 '34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64',
                 '65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95',
                 '96','97','98','99','100']
    await ctx.send(random.choice(responsus))

@client.command()
async def coinflip(ctx):
    coin = ['Орел','Решка']
    await ctx.send(random.choice(coin))

@client.command()
async def rhunt(ctx):
    await ctx.send("rpg hunt")

client.run(os.environ['BOT_TOKEN'])

##client.run(os.environ['BOT_TOKEN'])