import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time

# Site voor invite https://discordapp.com/oauth2/authorize?client_id=522487838361649152&scope=bot&permissions=8

Token = 'NTIyNDg3ODM4MzYxNjQ5MTUy.DvOjOQ.fS1ib9x8gyQ-4kan_LAZBE-bDgA'

client = discord.Client()   
# client = case_insensitive(True)d
# bot.remove_command('help')

@client.event
async def on_ready():
    print('I {0.user.name}'.format(client) + ' am online and ready to go!')
    game = discord.Game("anime on the background")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Test Crew')
    await client.add_roles(member, role)

# @client.event
# async def clear(ctx, amount=100):
#     if message.content.upper().startswith('CLEAR'):
#         channel = ctx.message.channel
#         message = []
#         async for message in client.logs_from(channel, limit=int(ammount) + 1):
#             message.append(message)
#         await client.delete_messages(messages)
#         await client.say('Messages is goooone')

# @client.event
# async def on_message_delete(message):
#     await message.channel.send("You cant hide anything from me. {0.author.name}".format(message) + "-senpai!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.upper().startswith('HELLO'):
        if message.author.id == "272014773162344449":
            await message.channel.send('Hello {0.author.name}'.format(message) + '-sensei')
        else:    
            await message.channel.send('Hello {0.author.name}'.format(message) + '-senpai')

    if message.content.upper().startswith('GOODNIGHT'):
        if message.author.id == "272014773162344449":
            await message.channel.send('Goodnight {0.author.name}'.format(message) + '-sensei')
        else:    
            await message.channel.send('Goonight {0.author.name}'.format(message) + '-senpai')

    if message.content.upper().startswith('OHAYO'):
        if message.author.id == "272014773162344449":
            await message.channel.send('Ohayo {0.author.name}'.format(message) + '-sensei')
        else:    
            await message.channel.send('Ohayo {0.author.name}'.format(message) + '-senpai')
    
    if message.content.upper().startswith('I LOVE YOU YUUNI'):
        if message.author.id == "272014773162344449":
            await message.channel.send('I love you more then anyone else {0.author.name}'.format(message) + '-sensei :heart_eyes:')
        else:    
            await message.channel.send('I love you too {0.author.name}'.format(message) + '-senpai')

    if message.content.upper().startswith('!PING'):
        userName = message.author.name
        await message.channel.send("%s Pong!" % (userName))
    
    if message.content.upper().startswith('!PONG'):
        userName = message.author.name
        await message.channel.send("%s Ping!" % (userName))

    if message.content.upper().startswith('!SAY'):
        args = message.content.split(" ")
        await message.channel.send("%s" % (" ").join(args[1:]))

# async def help(ctx):
#     author = ctx.message.author
#     embed = discord.Embed(
#         color = discord.Colour.Hotpink()
#     )
#     embed.set_author(name='Help')
#     embed.add_field(name='!Ping', value='Returns Pong!', inline=True)
#     await message.channel.send(author, embed=embed)

    # if message.conctent.upper().startswith('LOOKFORID'):
    #     userID = message.author.id
    #     await message.channel.send("Your id is <%s>" % (userID))


client.run(Token)