# All the necessary imports
import discord
from discord.ext import commands
from googlesearch import search


intents = discord.Intents.default()
intents.message_content = True


client = commands.Bot(command_prefix='/', intents=intents)


# Starting up bot.
@client.event
async def on_ready():
    print("Bot ready!")


# Uses Google search API to look for the top link option for the written String.
@client.command()
async def find_link(ctx, *, query):
    await ctx.channel.send("Here are the links related to your search!")
    async with ctx.typing():
        for i in search(query, tld="co.in", num=1, stop=1, pause=2):
            await ctx.send("Link: " + i)


# The bot is running
client.run('token')
