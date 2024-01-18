import os
import random
import discord 
from discord.ext import commands
import game

def runbot():
  intents= discord.Intents.default()
  intents.message_content = True
  bot = commands.Bot(command_prefix='/', intents=intents)
  @bot.event 
  async def on_ready(): 
    
    print(f"{bot.user}has logged in ")
  
  @bot.event 
  async def message ():
    if message.content.startswith (f'{command_prefix}hi '):
      await message.channel.send ('hello there')

  @bot.command (
    help ="This is a testing commands",
    aliases = ['p'],
    description = "This command is just answer pong ",
    enable = False
  )
  async def ping(ctx):
    '''.Answer as pong to ping.'''
    await ctx.send ('pong! ')

  @bot.command()
  async def say(ctx, what="sorry but what the fuck you wanna say? "):
    await ctx.send(what)
  
  @bot.command()
  async def bolo(ctx,*what):
    await ctx.send(" ".join(what))
  @bot.command()
  async def choice(ctx,*what):
    await ctx.send(random.choice(what))

  @bot.command(
    aliases = ['r.num'],
    description="This command will give you an random number between 1 to 100"
  )
  async def giveanumber(ctx, what:int=range(0, 100)):
    await ctx.send(f"How about 😉  {random.choice(what)}")

  @bot.command(
    help = "Game command",
    aliases =["play"],
    description="This command will play the rock paper scissors game",
    enable= False 
  )
  async def rpc(ctx, user: str ):
    if user.lower() in ['rock', 'paper', 'scissor']:
      comp = random.choice(["rock","paper","scissor"])
      result = game.game(user, comp)
      if result:
        await ctx.send(result)

      else:
        await ctx.send("Error occur")
    else:
      await ctx.send("please enter valid role")
    
  bot.run(os.environ.get('TOKEN'))


runbot()