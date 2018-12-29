import discord
from discord.ext import commands

class help:

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def help(ctx):
        author = ctx.message.author
        if not userName:
            embed=discord.Embed(color="#FA0293")
            embed.add_field(name="Random word. The random words are:", inline=True)
            embed.add_field(name="Weeb/Weeabop: ", value="Yuuni will react on you.", inline=False)
            embed.add_field(name="Hello/hey: ", value="Yuuni will react on you.", inline=False)
            embed.add_field(name="Ohayo/ohayōgozaimasu/ohayō: ", value="Yuuni will react on you.", inline=False)
            embed.add_field(name="ecchi/hentai: ", value="Yuuni will react on you.", inline=False)
            embed.add_field(name="nani: ", value="Yuuni will react on you.", inline=False)
            embed.add_field(name="oh my: ", value="Yuuni will react on you.", inline=True)
            embed.add_field(name="!waifu: ", value="Yuuni will pick a random person in the discord server and call it best waifu.", inline=False)
            embed.add_field(name="!husbando ", value="Yuuni will pick a random person in the discord server and call it best husbando.", inline=False)
            embed.add_field(name="!userinfo: ", value="Yuuni will give info about the user or someone that he/she calld.", inline=False)
            await ctx.send_message(author, embed=embed)
        else:
            embed=discord.Embed(color="#FA0293")
            embed.add_field(name="Random word. The random words are:", inline=True)
            embed.add_field(name="Weeb/Weeabop: ", value="Yuuni will react on you.", inline=False)
            embed.add_field(name="Hello/hey: ", value="Yuuni will react on you.", inline=False)
            embed.add_field(name="Ohayo/ohayōgozaimasu/ohayō: ", value="Yuuni will react on you.", inline=False)
            embed.add_field(name="ecchi/hentai: ", value="Yuuni will react on you.", inline=False)
            embed.add_field(name="nani: ", value="Yuuni will react on you.", inline=False)
            embed.add_field(name="oh my: ", value="Yuuni will react on you.", inline=True)
            embed.add_field(name="!waifu: ", value="Yuuni will pick a random person in the discord server and call it best waifu.", inline=False)
            embed.add_field(name="!husbando ", value="Yuuni will pick a random person in the discord server and call it best husbando.", inline=False)
            embed.add_field(name="!userinfo: ", value="Yuuni will give info about the user or someone that he/she calld.", inline=False)
            await ctx.send_message(author, embed=embed)

def setup(client):
    client.add_cog(help(client))
