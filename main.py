import os
from discord import Intents, Client, Message
from replit import db
from responses import get_response

#Discord Intent rules
intents: Intents = Intents.default()
intents.message_content = True #NOQA
client: Client = Client(intents=intents)

#intro message when starting
@client.event
async def on_ready():
  print('you in')

# event handling incoming message
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  try:
    if get_response(message.content) == "delete":
      await message.delete()
      print("Good")
    elif get_response(message.content) == None:
      await message.delete()
      print("ERR")
    elif get_response(message.content) == "list mons":
      keys = db.keys()
      for key in keys:
        print(db[key])
    else:
      await message.channel.send(get_response(message.content))
  except ValueError:
    print("Error")

client.run(os.environ['SECRET_BOT_KEY'])
