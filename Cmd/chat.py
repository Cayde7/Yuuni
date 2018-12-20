import discord
import re
from discord.ext import commands

class no_erp:
    def __init__(self, client):
        self.client = client

    async def on_message(self, message):
        if message.author == self.client.user:
            return
        text = message.content
        text = re.sub(r'[^\w\s]','', text).lower().split()
        if "no" in text:
            return
        elif "weeaboo" in text or "weeb" in text:
            await message.channel.send("Nobody here is a weeb or a weeaboo.")
        elif "anime" in text:
            await message.channel.send("Anime? Which anime?")
        elif "hello" in text or "hi" in text or "ohayo" in text:
            await message.channel.send("Hello {0.author.name}".format(message) + "-senpai")
        elif "ecchi" in text or "hentai" in text:
            await message.channel.send("Are u a pervert? :persevere: {0.author.name}".format(message) + "-senpai")

def setup(client):
    client.add_cog(no_erp(client))
