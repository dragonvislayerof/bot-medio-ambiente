import discord
import random
import os
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Nos hemos logeado como {bot.user}')

@bot.command()
async def mem(ctx):
    try:
        images = os.listdir('images')
        if images:
            img_name = random.choice(images)
            with open(f'images/{img_name}', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(file=picture)
        else:
            await ctx.send("¡No se encontraron memes en la carpeta 'imagenes'!")
    except FileNotFoundError:
        await ctx.send("¡No se encontró la carpeta 'imagenes'!")

@bot.command()
async def ma(ctx):
    await ctx.send("¡Hola! Veo que estás interesado en el medio ambiente. ¡Aquí tienes 5 consejos!")
    await ctx.send("1. Recicla la basura.")
    await ctx.send("2. Usa productos que puedan reutilizarse.")
    await ctx.send("3. Apaga las luces.")
    await ctx.send("4. Consume productos ecológicos y locales.")
    await ctx.send("5. Evita dejar los aparatos enchufados.")

@bot.command()
async def video(ctx):
    video_path = r"C:/Users/juan miguel domingue/Documents/proyectos python/cloase 6/mav.mp4"
    if os.path.isfile(video_path):
        await ctx.send(file=discord.File(video_path))
    else:
        await ctx.send("No se encontró el archivo de video.")

@bot.command()
async def mar(ctx):
    await ctx.send("¡Hola! Veo que quieres un resumen de cómo cuidar el medio ambiente:")
    await ctx.send("Evita quemar basura, hojas y otros objetos, así como hacer fogatas en bosques o en plena ciudad.")
    await ctx.send("Riega las plantas durante la noche o muy temprano, cuando el Sol tarda más en evaporar el agua.")
    await ctx.send("Reutiliza el agua que juntaste de la regadera y de lavar las verduras para regar las plantas o el jardín.")

@bot.command()
async def reci(ctx):
    await ctx.send("La Cometa. Para este proyecto tan solo necesitaremos unas pajitas de plástico como las que utilizamos para beber, una bolsa de plástico, cinta aislante e hilo.")
    await ctx.send("Envasador de bolsas.")
    await ctx.send("Portabolsas de la compra.")
    await ctx.send("Cocina al vapor desde el mismo plato.")
    await ctx.send("Alfombrilla para el baño.")

bot.run("")
