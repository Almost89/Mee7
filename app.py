# Modules
import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv

# Init the dotenv module
load_dotenv()

# Vars
DISCORD_TOKEN = os.getenv("discord_token")

intents = discord.Intents().all()
client = discord.Client(intents = intents)
bot = commands.Bot(command_prefix = '!', intents = intents)

# Join command
@bot.command(name = "join", help = "tells da bot to join your ~~text~~ voice channel")
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not conncted to a voice channel!".format(ctx.message.anthor.name))
        return
    else:
        channel = ctx.message.anthor.voice.channel
    await channel.connect()

# Leave command
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

# Play command
@bot.command(name = "play", help = "play an epik song")
async def play(ctx):
    try:
        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop = bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable = "ffmpeg.exe", source = filename))
        await ctx.send('**Now playing:** {}'.format(filename))
    
    except:
        await ctx.send("The bot is not connected to a voice channel.")

# Pause + stop command
@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    await ctx.send("never!")

@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    await ctx.send("no u")

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)