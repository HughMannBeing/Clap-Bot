import discord
from discord.ext.commands import Bot

my_bot = Bot(command_prefix="!")

@my_bot.event
async def on_read():
    print("Client logged in")

@my_bot.command()
async def test(*args):
    return await my_bot.say("\U0001F44F")

naughtyWords = ["FUCK", "SHIT", "DAMN", "DARN", "DANGIT", "GOSHDARN", "FUCKING", "DANG", "DARNDIDDLEYDOIT", "STUPID", "DUMB", "USESLESS"]

@my_bot.command()
async def clap(sentence):
    didTrigger = False
    didReferenceBot = False
    dent = sentence.split(" ")
    temp = []
    for i in dent:
        if str(i).upper() == "BOT":
            didReferenceBot = True
        if str(i).upper() in naughtyWords:
            if didTrigger == False:
                await my_bot.say("Hey, watch you language there!")
                didTrigger = True
            temp.append("CENSORED")
        else:
            temp.append(i)
        temp.append(" \U0001F44F ")
    if didReferenceBot and didTrigger:
        return await my_bot.say("\U0001F44F fuck \U0001F44F you \U0001F44F")
    else:
        return await my_bot.say(" ".join(temp))

my_bot.run("MzE1NTczOTc3MTM5MzgwMjI0.DAIs0A.Q59gwXvN2jvbGUV0iYmaR-36-_s")
