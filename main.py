import discord
from discord.ext.commands import AutoShardedBot, when_mentioned_or
from Secrect import Secret
from docs import comandos
import musi
import os

Pref = "?"
pera = 'discord.ext.commands.errors.CommandNotFound'

client = discord.Client()
client = AutoShardedBot(command_prefix=Pref, case_insensitive=True)
client.remove_command('help')


@client.event
async def on_ready():
    print("Bot on")
    print(client.user.name)
    print(client.user.id)
    game = discord.Game("pica na sua mina")
#    await client.change_presence(status=discord.Status.idle, activity=game)
    await client.change_presence(activity=discord.Streaming(name=Pref+'help', url='https://www.twitch.tv/narutozini'))


@client.event
async def on_ready():
    if not os.path.exists("perfils"):
        os.mkdir("testaNdo")
    else:
        pass



modulos = ["docs.comandos","musi"]

if __name__ == "__main__":
    for modulo in modulos:
        client.load_extension(modulo)


client.run(Secret)
