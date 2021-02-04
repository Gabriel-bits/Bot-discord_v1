import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandInvokeError
from data.arquivos import *
import json, os

cor = int(0xe0d900)
Pref = "?"
client = discord.Client()

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
        embed.add_field(name="Perfil animado para live", value="`?Strean`", inline=True)
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
        embed.add_field(name="* `?fala`", value="ex:( ?falar comida) ele mandara uma mensagem com o que vc escreveu na frente do comando.", inline=False)
        embed.add_field(name="* `?inf`", value="pode ser usado para saber as informaçoes do menbro ex:( ?inf @users).", inline=True)
        embed.set_footer(text="por enquanto e so.\r")
        await ctx.send(embed=embed)

 
    @commands.command()
    async def prefixos(self, ctx):
        embed=discord.Embed(title="Não disponível no momento ", color=cor)
        await ctx.send(embed=embed)
    
    
    @commands.command()
    async def repositorio(self, ctx):
        embed=discord.Embed(title="https://github.com/Gabriel-bits/Bot-discord_v1", color=cor)
        await ctx.send(embed=embed)


    @commands.command()
    async def Strean(self, ctx):
        embed=discord.Embed(title="Perfil animado pra ser usado no obs", description="Seguindo os comandos abaixo vc poderar o codg do seu perfil animado para ser usado no obs se segindo a seguinte instrução( Obs -> add objt na cena -> add browser -> espaço para codg CSS ) para mais imformações {Pref}str_tutorial." , color=cor)
        embed.set_author(name="Straem_perfil",url="https://emoji.gg/assets/emoji/7277_green_flame.gif" , icon_url="https://emoji.gg/assets/emoji/7277_green_flame.gif")
        embed.add_field(name="* `?Str_nome`", value=f"ex:({Pref}Str_nome + @você) vai inicilalizar e salvar um perfil/arquivo para cogs.", inline=False)
        embed.add_field(name="* `?Str_defalt`", value=f"ex:({Pref}Str_defalt + imagem/gif) imagem/gif que ficara visivel quando você parar de falar.", inline=False)
        embed.add_field(name="* `?Str_falando`", value=f"ex:({Pref}Str_falando + imagem/gif) imagem/gif que ficara visivel quando você falar algo.", inline=False)
        embed.add_field(name="* `?Str_codg`", value=f"ex:({Pref}Str_codg) retornara a o codígo em forma de menssage para ser add no espaço para codg CSS.", inline=False)
        embed.add_field(name="* `?Str_tutorial`", value=f"ex:({Pref}Str_codg) endisponivel por em quanto vai tmnc passei tres dia fazendo cada codg dessa aba.", inline=False)
        embed.set_footer(text="por enquanto e so.\r")
        await ctx.send(embed=embed)


    


    '''
    cmds dos bot:
    ==========================================================================]
    '''

    @commands.command()
    async def meu_criador(self, ctx):
        await ctx.send()


    @commands.command()
    async def fala(self, ctx , *, frase= None, frase2= None):
        if frase is None:
            await ctx.send(Pref+"fala + alguma coisa")
            return
        await ctx.message.delete()
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

    """
    Strean:
    ==========================================================================]
    
    @commands.command()
    async def Str_nome(self, ctx, *, id_user:discord.Member= None):
        
        if id_user == None:
            embed=discord.Embed(title=f"Confira, se digitou o comando corretamente.\rexp: ```{Pref}Str_nome``` + @voce", color=cor)
            await ctx.send(embed=embed)
            return
        salvar_profil(id_user.id, ima1= None, ima2= None)

        embed=discord.Embed(title=f"O usuario <@!{id_user.id}> foi iniciado, e sera fechado apos o ultimo comondo ou seja ```{Pref}imag_speck```.", color=cor)
        await ctx.send(embed=embed)


    @commands.command()
    async def Str_defalt(self, ctx, *, not_speck= None):
        if not_speck == None:
            embed=discord.Embed(title=f"Confira, se digitou o comando corretamente.\rexp: ```{Pref}Str_defalt``` + @voce", color=cor)
            await ctx.send(embed=embed)
            return
        salvar_profil(ctx.author.id, not_speck, ima2=None)

        embed=discord.Embed(title=f"O usuario <@!{ctx.author.id}> foi iniciado, e sera fechado apos o ultimo comondo ou seja \r```{Pref}imag_speck```.", color=cor)
        embed.set_thumbnail(url=f"{not_speck}")
        await ctx.send(embed=embed)


    @commands.command()
    async def Str_falando(self, ctx, *, speck=None):
        
        if speck == None:
            embed=discord.Embed(title=f"Confira, se digitou o comando corretamente.\rexp: ```{Pref}Str_falando``` + @voce", color=cor)
            await ctx.send(embed=embed)
            return

        with open(f"{ctx.author.id}.json", "r") as f:
            perfil = json.load(f)
        try:
            salvar_profil(ctx.author.id, ima1=perfil["not_speck"], ima2= speck)
        except Exception as ee:
            print(f"Erro -> {ee}")

        embed=discord.Embed(title="Discord Streamkit", url="https://streamkit.discord.com/overlay", description="Link pra o streamkit ⬆", color=cor)
        embed.set_author(name=f"___________________________________________")
        embed.set_thumbnail(url=f"{ctx.author.avatar_url}")
        embed.add_field(name=f"@{ctx.author.name} Seu codg foi salvo com sucesso !.\rPara acessa seu codg digite o seguinte comando:", value=f"`{Pref}Str_codg`", inline=False)
        embed.set_footer(text=f"by <@!{551436913639292928}>")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('✅')

"""
    @commands.command()
    async def Str_codg(self, ctx):

        with open(f"perfils/{ctx.author.id}.json", "r") as f:
            perfil = json.load(f)

        id_usuar = str(perfil["nome"])
        imag1 = str(perfil["not_speck"])
        imag2 = str(perfil["speck"])

        codg_c = '''```CSS
li.voice-state:not([data-reactid*="'''+id_usuar+'''"]) { display:none;
.avatar {
content:url('''+imag1+''');
height:auto !important;
width:auto !important;
border-radius:0% !important;
filter: opacity(100%);
}

.speaking {
border-color:rgba(0,0,0,0) !important;
position:relative;
animation-name: speak-now;
animation-duration: 1s;
animation-fill-mode:forwards;
filter: brightness(100%);
content:url('''+imag2+''');
}

@keyframes speak-now {
0% { bottom:0px; }
15% { bottom:7px; }
30% { bottom:0px; }
}

li.voice-state{ position: static; }
div.user{ position: absolute; left:40%; bottom:5%; }

body { background-color: rgba(0, 0, 0, 0); margin: 0px auto; overflow: hidden; } ``` '''
        

        await ctx.send(f"@{ctx.author.name}:\r{codg_c}")











    @commands.command()
    async def Str_perfil(self, ctx, args:discord.Member, args2, *, args3):
        '''
        !! cuidado area perigosa !!
        args = id do usuario
        args2 = imagem not_speack
        args3 = imagem speack
        '''

        if args == None is args2 == None is args3 == None:
            embed=discord.Embed(title=f"Confira, se digitou o comando corretamente.\rexp: ```{Pref}Str_perfil``` + @voce + imagem_defalt + imagem_falando", color=cor)
            await ctx.send(embed=embed)
            return

        try:
            salvar_profil(args.id, args2, args3)

        except:
            embed=discord.Embed(title=f"Ocorreu um erro, confira se digitou o comando corretamente.\rexp: ```{Pref}Str_perfil``` + @voce + imagem_defalt + imagem_falando", color=cor)
            await ctx.send(embed=embed)
            return

        with open(f"perfils/{ctx.author.id}.json", "r") as f:
            perfil = json.load(f)

        id_usuario = str(args.id)
        imag1 = str(args2)
        imag2 = str(args3)

        codg_c = '''```CSS
li.voice-state:not([data-reactid*="'''+id_usuario+'''"]) { display:none;
.avatar {
content:url('''+imag1+''');
height:auto !important;
width:auto !important;
border-radius:0% !important;
filter: opacity(100%);
}

.speaking {
border-color:rgba(0,0,0,0) !important;
position:relative;
animation-name: speak-now;
animation-duration: 1s;
animation-fill-mode:forwards;
filter: brightness(100%);
content:url('''+imag2+''');
}

@keyframes speak-now {
0% { bottom:0px; }
15% { bottom:7px; }
30% { bottom:0px; }
}

li.voice-state{ position: static; }
div.user{ position: absolute; left:40%; bottom:5%; }

body { background-color: rgba(0, 0, 0, 0); margin: 0px auto; overflow: hidden; } ``` ''' 

        await ctx.send(f"@{ctx.author.name}:\r{codg_c}")








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
