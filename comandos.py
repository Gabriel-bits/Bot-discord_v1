import discord
from discord.ext import commands

cor = int(0xe0d900)

#classe:
class comandos(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.cooldown(1,2, commands.BucketType.user)
    @commands.guild_only()
    @commands.command()
    async def heLp(self, ctx):
        embed=discord.Embed(title="comandos primários do bot", description="temos uma função especial que se você estiver em \rduvida sobre os prefixos dos outros bots você \rpode usar o comando abaixo (prefixos).", color=cor)
        embed.set_author(name="ZEN Comandos", url="https://discord.com/api/oauth2/authorize?client_id=745030751636029530&permissions=8&scope=bot" , icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQd1yqpOX-OrXQX_95zdGZ8bmBBTZyHQgKzg&usqp=CAU")
        embed.add_field(name="Comandos", value="`?cmds`", inline=True)
        embed.add_field(name="Prefixos", value="`?prefixos`", inline=True)
        embed.add_field(name="Link do bot", value="`?link_bot`", inline=True)
        help_eact = await ctx.send(embed=embed)
        await help_eact.add_reaction('😀')


    @commands.command()
    async def LiNk_bot(self, ctx):
        embed=discord.Embed(
            title="☝ e so clicar para add nosso bot ao seu servem", color=cor)
        embed.set_author(name="Click aqui", url="https://discord.com/api/oauth2/authorize?client_id=745030751636029530&permissions=8&scope=bot")
        embed.set_thumbnail(url="https://www.freeiconspng.com/thumbs/add-icon-png/add-1-icon--flatastic-1-iconset--custom-icon-design-0.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def cmds(self, ctx):
        embed=discord.Embed(title="Não disponível no momento", color=cor)
        await ctx.send(embed=embed)


    @commands.command()
    async def prefixos(self, ctx):
        embed=discord.Embed(title="Não disponível no momento ", color=cor)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(comandos(client))
