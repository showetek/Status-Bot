#  * @file
#  * This file is part of the source code of the absolute awesome Status-Bot for Discord.
#  * 
#  * @author      Torben Heine
#  * @copyright   Copyright (c) 2021, Torben Heine
#  * @github      https://github.com/showetek
#  * @version     0.1.4 PRE-RELEASE

#import
import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound
from discord.embeds import Embed

#Create Bot
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = ".", help_command=None, intents=intents)

#Var
file = open("token","r")
token = file.read()
file.close

#Functions
async def changenick(message, icon):
    user = message.author
    if user.nick != None:
        nick = user.nick
    else:
        nick = user.name
    if nick[1] == ' ':
        nick = nick[2:]
    await user.edit(nick= '{0} {1}'.format(icon, nick))
    print('Changed nickname from {0.name}'.format(user))
            
#Debug
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

#Get members and await commands
@bot.event
async def on_message(message:discord.message.Message):
    if message.author == bot.user:
        return
    else:
        await bot.process_commands(message)

#Command not found exception
@bot.event
async def on_command_error(message:discord.message.Message, error):
    if isinstance(error, CommandNotFound):
        await message.channel.send(error)
        print("Catching exception: {0}".format(error))
    else:
        raise error

#Clear
@bot.command()
async def clear(message:discord.message.Message):
    msg = []
    async for newmessage in message.channel.history(limit=100):
        msg.append(newmessage)
    await message.channel.delete_messages(msg)

#Help
@bot.command()
async def help(message:discord.message.Message):
    helpmessage = Embed(title="Help Information")
    helpmessage.add_field(name="Prefix",value=".",inline=True)
    helpmessage.add_field(name="Source",value="Source code located at [GitHub](https://github.com/showetek/Status-Bot)",inline=False)
    helpmessage.add_field(name="melden (m)",value="Setzt den Status auf ✋",inline=True)
    helpmessage.add_field(name="hoch",value="Setzt den Status auf 👍",inline=True)
    helpmessage.add_field(name="runter",value="Setzt den Status auf 👎",inline=True)
    helpmessage.add_field(name="reset (r)",value="Setzt den Status zurück",inline=True)
    helpmessage.add_field(name="resetall",value="Setzt den Status aller zurück",inline=True)
    helpmessage.add_field(name="help",value="Zeigt diesen Helpkontext an",inline=True)
    helpmessage.add_field(name="Beispiel",value=".m : Torben --> ✋ Torben",inline=True)
    await message.channel.send(embed = helpmessage)

#Status setzen
@bot.command(aliases=['m'])
async def melden(message:discord.message.Message):
    await changenick(message, '✋')

@bot.command()
async def hoch(message:discord.message.Message):
    await changenick(message, '👍')

@bot.command()
async def runter(message:discord.message.Message):
    await changenick(message, '👎')

@bot.command()
async def deadinside(message:discord.message.Message):
    await changenick(message, '🕱')

#Status reseten
@bot.command(aliases=['r'])
async def reset(message:discord.message.Message):
    user = message.author
    if user.nick != None:
        nick = user.nick
    else:
        nick = user.name

    if nick[1] == ' ':
        await user.edit(nick = nick[2:])    
    print('Resettet nickname from {0.name}'.format(user))

#Reset all
@bot.command()
async def resetall(message:discord.message.Message):
    user = message.author
    for member in message.guild.members:
        if member.bot != True:
            if member.nick != None:
                nick = member.nick
            else:
                nick = member.name
    
            if nick[1] == ' ':
                await member.edit(nick = nick[2:])        
    print('Resettet all user by {0.name}'.format(user))

#run this shit
bot.run(token)