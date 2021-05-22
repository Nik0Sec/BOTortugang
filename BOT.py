import datetime
import os
import random
from time import sleep
import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from dotenv import load_dotenv
import youtube_dl
import os
from tqdm import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!') #Prefijo bot



@bot.command()
async def pinga(ctx):
   await ctx.send("pong")

@bot.command()
async def info1(ctx):
    embed = discord.Embed(title="A esta hora me estoy culiando a tu mamita: ", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/9/90/EGG_KING_DIOS.jpg")
    await ctx.send(embed=embed)

@bot.command()
async def ayuda(ctx):
   await ctx.send("""
   LOS COMANDOS MAS LAKRAS DEL UNIVERSO JJJJAAAAAAAA
   
!info1 = La hora exacta que se están culiando a tu mamita jojojojo !info
!esquizo = Dice puras frases pa putiarte aleatoriamente | !esquizo
!agregar = añade una frase al bot (!esquizo) para que te putee aleatoriamente | !añadir FRASE 
!putear = putea a un usuario determinado jojojojojo
!mc = te dice el status del server indicado | !mc NOMBREDELSERVER
   """)

@bot.command()
async def esquizo(ctx):
    archivo = open('insultos', 'r')
    content = archivo.read().splitlines()
    line = random.choice(content)
    await ctx.send(content=line)


@bot.command()
async def agregar(ctx, *, buscar):
    frase = open('insultos', '+a')
    data = frase.write("{} \n".format(buscar))
    await ctx.send('Frase añadida, que sea una wea de vio sipo fracasao y la ctm !!!!')

@bot.command()
async def spam(ctx, *, mensaje):
    for x in range(10):
        await ctx.send('{}'.format(mensaje))

@bot.command()
async def putear(ctx, *, usuario):
    user = "{}".format(usuario)
    if user:
        await esquizo(ctx)


@bot.event
async def on_ready():
    game = discord.Game('WEAR A LONJIS TOA LA NOXE')
    await bot.change_presence(status=discord.Status.online, activity=game)


@bot.command()
async def mc(ctx, arg):
    r = requests.get('https://api.minehut.com/server/' + arg + '?byName=true')
    json_data = r.json()

    description = json_data["server"]["motd"]
    online = str(json_data["server"]["online"])
    playerCount = str(json_data["server"]["playerCount"])

    embed = discord.Embed(
        title="Info de la caga de server:  \n" + arg,
        description='Descripcion del sv: ' + description + '\nTa activo ono: ' + online + '\nWns jugando: ' + playerCount,
        color=discord.Color.dark_green()
    )
    embed.set_thumbnail(url="https://i1.wp.com/www.craftycreations.net/wp-content/uploads/2019/08/Grass-Block-e1566147655539.png?fit=500%2C500&ssl=1")

    await ctx.send(embed=embed)




bot.run(TOKEN)
