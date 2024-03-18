import os
import random
import discord 
from discord.ext import commands
import game
import get_quote as q
import gemini as gem
import chatgpt as cht

def runbot():
  intents= discord.Intents.default()
  intents.message_content = True
  command_prefix = '/'
  bot = commands.Bot(command_prefix, intents=intents)
  @bot.event 
  async def on_ready():  
    print(f"{bot.user}has logged in ")

   # await bot.tree.sync()
  
  '''@bot.event 
  async def on_message (message):
    if message.content.startswith (f'{command_prefix}hi '):
      await message.channel.send ('hello there')
'''
  @bot.command()
  async def say(ctx, what="sorry but what the fuck you wanna say? "):
    await ctx.send(what)

  @bot.command(
    aliases = ["quote"],
    description = "This command will give you a quote "
    
  )
  async def inspire():
    quote = q.get_quote()
    await ctx.send(quote)

#what is users context which get stores in :)

  @bot.command()
  async def bolo(ctx,what):  
    await ctx.send(" ".join(what))


  @bot.command()
  async def choice(ctx,what):
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
    enabled= True 
  )
  async def rpc(ctx, user: str ):
    if user.lower() in ['rock', 'paper', 'scissor']:
      comp = random.choice(["rock","paper","scissor"])
      result = game.game(user, comp)
      await ctx.send(result)
    else:
      await ctx.send("please enter valid role")

  @bot.command(
    help = "personal chatting",
    aliases = ['kanojo'],
    description = "with this command you can call me anytime to hangon!! "
    
  )
  async def gemini(ctx,what):
    response = gem.generate_response(what)
    await ctx.send(response)

  @bot.command()
  async def gpt(ctx, what):
    response = cht.gpt(what)
    await ctx.send(response)
    
  bot.run(os.environ.get('TOKEN'))

runbot()