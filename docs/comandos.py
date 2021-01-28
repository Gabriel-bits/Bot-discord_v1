import discord
from discord.ext import commands


cor = int(0xe0d900)
Pref = "?"
client = discord.Client()
#classe:
class comandos(commands.Cog):
    def __init__(self, client):
        self.client = client

    '''
    Comandos primarios:
    ==========================================================================]
    '''
    @commands.cooldown(1,2, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def heLp(self, ctx):
        embed=discord.Embed(title="comandos primários do bot", description="temos uma função especial que se você estiver em duvida sobre os prefixos dos outros bots você \rpode usar o comando abaixo (prefixos).", color=cor)
        embed.set_author(name="ZEN Comandos", url="https://discord.com/api/oauth2/authorize?client_id=745030751636029530&permissions=8&scope=bot" , icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQd1yqpOX-OrXQX_95zdGZ8bmBBTZyHQgKzg&usqp=CAU")
        embed.add_field(name="Comandos", value="`?cmds`", inline=True)
        embed.add_field(name="Prefixos", value="`?prefixos`", inline=True)
        embed.add_field(name="Link do bot", value="`?link_bot`", inline=True)
        embed.add_field(name="Repositorio", value="`?repositorio`", inline=True)
        help_eact = await ctx.send(embed=embed)
        await help_eact.add_reaction('👍')


    @commands.command()
    async def LiNk_bot(self, ctx):
        embed=discord.Embed(title="☝ e so clicar para add nosso bot ao seu servem", color=cor)
        embed.set_author(name="Click aqui", url="https://discord.com/api/oauth2/authorize?client_id=745030751636029530&permissions=8&scope=bot")
        embed.set_thumbnail(url="https://www.freeiconspng.com/thumbs/add-icon-png/add-1-icon--flatastic-1-iconset--custom-icon-design-0.png")
        await ctx.send(embed=embed)


    @commands.command()
    async def cmds(self, ctx):
        embed=discord.Embed(title="divirta-se", color=cor)
        embed.set_author(name="Comandos",url="https://emoji.gg/assets/emoji/7277_green_flame.gif" , icon_url="https://emoji.gg/assets/emoji/7277_green_flame.gif")
        embed.add_field(name="* ?fala", value="ex:( ?falar comida) ele mandara uma mensagem com o que vc escreveu na frente do comando.", inline=False)
        embed.add_field(name="* ?inf", value="pode ser usado para saber as informaçoes do menbro ex:( ?inf @users).", inline=True)
        embed.set_footer(text="por enquanto e so.\r")
        await ctx.send(embed=embed)

 
    @commands.command()
    async def prefixos(self, ctx):
        embed=discord.Embed(title="Não disponível no momento ", color=cor)
        await ctx.send(embed=embed)
    
    
    @commands.command()
    async def repositorio(self, ctx):
        embed=discord.Embed(title="Não disponível no momento ", color=cor)
        await ctx.send(embed=embed)

    '''
    cmds dos bot:
    ==========================================================================]
    '''
    

    @commands.command()
    async def meu_criador(self, ctx):
        await ctx.send()

    @commands.command()
    async def fala(self, ctx , *, frase= None):
        if frase is None:
            await ctx.send(Pref+"fala + alguma coisa")
            return
        await ctx.send(f"{frase}")


    @commands.command()
    async def ping(self, ctx, *, usuario):
        
        teta = discord.Client()
        await ctx.send(f'Seu ping e de {teta} ms')
        print(teta.latency(usuario))
        
        
    @commands.command()
    async def inf(self, ctx , *, usuario:discord.Member= None):
        if usuario is None:
            await ctx.send(Pref+"inf + @usuario")
            return
        usuario
        embed=discord.Embed(title="Informaçao do usuário ", color=cor)
        embed.set_thumbnail(url=usuario.avatar_url)
        embed.add_field(name="Nome:", value="`{}`".format(usuario.name), inline=True)
        embed.add_field(name="Apelido:", value="`@{}`".format(usuario.display_name), inline=True)
        embed.add_field(name="Id:", value="`{}`".format(usuario.id), inline=False)
        embed.add_field(name="Conta criada:", value="`{}`".format(usuario.created_at), inline=False)
        embed.add_field(name="Avatar:", value=usuario.avatar_url, inline=True)
        await ctx.send(embed=embed)
'''
    @commands.command()
    async def join(self, ctx):
        if not ctx.message.author.voice:
            await ctx.send("You are not connected to a voice channel")
            return
        else:
            channel = ctx.message.author.voice.channel

        await channel.connect()

    @commands.command()
    async def play(self, ctx):
        global queue

        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            player = await YTDLSource.from_url(queue[0], loop=client.loop)
            voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
'''
    



def setup(client):
    client.add_cog(comandos(client))
