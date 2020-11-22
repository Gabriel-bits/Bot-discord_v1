import discord
from discord.ext.commands import AutoShardedBot, when_mentioned_or
from Secrect import Secret

Pref = "?"

client = discord.Client()
client = AutoShardedBot(command_prefix=Pref, case_insensitive=True)
client.remove_command('help')


@client.event
async def on_ready():
    print("Bot on")
    print(client.user.name)
    print(client.user.id)
    await client.change_presence(activity=discord.Streaming(name=Pref+'help', url='https://www.twitch.tv/narutozini'))


#modolos:
modulos = ["comandos"]


#test:(
#@client.event
#async def on_message(message):

#o que o bot esta asistindo / mensagem explicativa dele :
#@client.event
#async def on_ready():
#    print(f'{client.user.name} online')
#    await client.change_presence(activity=discord.Streaming(name='?help', url='https://www.twitch.tv/narutozini'))
#carregar os modulos:

if __name__ == "__main__":
    for modulo in modulos:
        client.load_extension(modulo)


client.run(Secret)
