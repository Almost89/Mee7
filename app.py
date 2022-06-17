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
@bot.command(name='pause', help = "it's ~~not~~ in the name")
async def pause(ctx):
    await ctx.send("never!")

@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    await ctx.send("no u")

# Gib command
@bot.command(name = "gib", help = "gib da user what they deverseeey")
async def gib(ctx):
    dm_channel = ctx.anthor.dm_channel
    if not dm_channel:
        dm_channel = ctx.anthor.create_dm()

    for i = 0, range(51):
        await dm_channel.send(content = "eat spam", file = discord.File("https://media0.giphy.com/media/xdnytp8742kg0/giphy.gif?cid=ecf05e47ugoxffbpbfjk9i34t2v9nfmtsfqcvwyn4wh13agj&rid=giphy.gif&ct=g"))


if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)