import discord
import asyncio
import json
from discord.ext import commands

startup_extensions = [
"Cmd.Client",
"Cmd.Waifu",
"Cmd.chat",
]

client = discord.Client()
client = commands.Bot(command_prefix=(""),
                      pm_help=True,
                      case_insensitive=True,
                      owner_id=272014773162344449)

client.remove_command('help')

async def background_loop():
    while True:
        await client.wait_until_ready()
        online = []
        x = client.get_all_members()
        for member in x:
            if member.status == discord.Status.online:
                online.append(member)
            elif member.status == discord.Status.idle:
                online.append(member)
            elif member.status == discord.Status.dnd:
                online.append(member)
        watching = "anime"

        await client.change_presence(activity=discord.Activity(name=watching, type=3))
        await asyncio.sleep(600)
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

client.loop.create_task(background_loop())
client.run("NTIyNDg3ODM4MzYxNjQ5MTUy.DvOjOQ.fS1ib9x8gyQ-4kan_LAZBE-bDgA", bot=True, reconnect=True)
