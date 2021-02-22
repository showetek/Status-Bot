#import
from inspect import getmembers
import discord
from discord.embeds import Embed
from discord.ext import commands

#Create Bot
bot = commands.Bot(command_prefix = ".")

#Var
members =[]

file = open("token","r")
token = file.read()

#Functions
def getmember(user):
    is_inside = False
    for i in range(len(members)):
        if members[i] == user:
            is_inside = True
            members[i] = user
        
    if is_inside == False:
        members.append(user)  
            
#Debug
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message:discord.message.Message):
    if message.author == bot.user:
        return
    else:
        user = message.author
        getmember(user)

    #Clear
    if message.content.startswith('.clear'):
        msg = []
        async for newmessage in message.channel.history(limit=100):
            msg.append(newmessage)
        await message.channel.delete_messages(msg)

    #Help
    if message.content.startswith('.help'):

        helpmessage = Embed(title="Help Information")
        helpmessage.add_field(name="Prefix",value=".",inline=False)
        helpmessage.add_field(name="m",value="Setzt den Status auf ✋",inline=True)
        helpmessage.add_field(name="hoch",value="Setzt den Status auf 👍",inline=True)
        helpmessage.add_field(name="runter",value="Setzt den Status auf 👎",inline=True)
        helpmessage.add_field(name="r",value="Setzt den Status zurück",inline=True)
        helpmessage.add_field(name="allreset",value="Setzt den Status aller zurück",inline=True)
        helpmessage.add_field(name="help",value="Zeigt diesen Helpkontext an",inline=True)
        helpmessage.add_field(name="Beispiel",value=".m : Torben --> ✋ Torben",inline=True)
        await message.channel.send(embed = helpmessage)

    #Status setzen
    if message.content.startswith('.m'):
        user = message.author
        if user.nick != None:
            nick = user.nick
        else:
            nick = user.name

        if nick[1] == ' ':
            nick = nick[2:]
        await user.edit(nick= '{i} {n}'.format(n = nick, i= '✋'))
        print('done')   

    if message.content.startswith('.hoch'):
        user = message.author
        if user.nick != None:
            nick = user.nick
        else:
            nick = user.name

        if nick[1] == ' ':
            nick = nick[2:]
        await user.edit(nick= '{i} {n}'.format(n = nick, i= '👍'))
        print('done')    

    if message.content.startswith('.runter'):
        user = message.author
        if user.nick != None:
            nick = user.nick
        else:
            nick = user.name

        if nick[1] == ' ':
            nick = nick[2:]
        await user.edit(nick= '{i} {n}'.format(n = nick, i= '👎'))
        print('done')    

    if message.content.startswith('.deadinside'):
        user = message.author
        if user.nick != None:
            nick = user.nick
        else:
            nick = user.name

        if nick[1] == ' ':
            nick = nick[2:]
        await user.edit(nick= '{i} {n}'.format(n = nick, i= '🕱'))
        print('done')    
    
    #Status reseten
    if message.content.startswith('.r'):
        user = message.author
        if user.nick != None:
            nick = user.nick
        else:
            nick = user.name

        if nick[1] == ' ':
            await user.edit(nick = nick[2:])
        else:
            print('done')
    
    #Reset all
    if message.content.startswith('.allreset'):
        #print(members)
        for member in members:
            if member.nick != None:
                nick = member.nick
            else:
                nick = member.name
                
            if nick[1] == ' ':
                await member.edit(nick = nick[2:])
            else:
                print('done')
            
#run this shit
bot.run(token)