import discord
import youtube_dl
from discord.ext import commands

TOKEN = "NDUzNTYyNzc2OTc2MDk3MzAw.DfgtEw.pYtH7BMHMATBjTbz8sY58SWsrWM"

client = commands.Bot(command_prefix = ".")
client.remove_command('help')

players = {}

@client.event
async def on_ready():
    print("bot is ready")

@client.event
async def on_message(message):
    print("A user sent a message go chek it!")
    await client.process_commands(message)

@client.command()
async def ping():
    await client.say('PONG!')

@client.command()
async def echo(*args):
    output = ""
    for word in args:
        output += word
        output += " "
    await client.say(output)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name="test1")
    await client.add_roles(member, role)

@client.command()
async def displayembed():
    embed = discord.Embed(
    title = "Test",
    description = "This is a test",
    colour = 0x1E90FF
    )

    embed.set_footer(text="MadeByTwins")
    embed.set_image(url='https://cdn.discordapp.com/attachments/442755312924098561/449630894039236628/unknown.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/442755312924098561/449630894039236628/unknown.png')
    embed.set_author(name='Twins', icon_url='https://cdn.discordapp.com/attachments/442755312924098561/449630894039236628/unknown.png')
    embed.add_field(name='field name', value='IsOk', inline=False)

    await client.say(embed=embed)

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
    colour = 0x1E90FF
    )

    embed.set_author(name='Help')
    embed.add_field(name='ping', value='returns Pong!', inline=False)
    await client.send_message(author, embed=embed)

@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} Has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.content))

@client.event
async def on_client_remove(recation, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} Has removed {} from the message: {}'.format(user.name, reaction.emoji, reaction.message.content))


@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

@client.command(pass_context=True)
async def play(ctx, url):
    players = {}
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url)
    players [server.id] = player

    player.start()
    await client.say('Here The music')

@client.command(pass_context=True)
async def pause(ctx):
    players = {}
    id = ctx.message.server.id
    players[id].pause()
    await client.say('Paused')

@client.command(pass_context=True)
async def stop(ctx):
    players = {}
    id = ctx.message.server.id
    players[id].stop()
    await client.say('Stoped')

@client.command(pass_context=True)
async def resume(ctx):
    players = {}
    id = ctx.message.server.id
    players[id].resume()
    await client.say('resumed')



client.run(TOKEN)
