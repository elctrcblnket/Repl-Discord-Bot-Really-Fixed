import os #is this from replit?
from discord import Intents, Client, Message #what are these discord library functions?
from replit import db #this gets us the database functions
from responses import get_response #this is an OC header/import

#i guess this is some default settings that were copied over
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
  #why ends message function?
  # "That’s why it’s important to compare the message.author to the client.user (your bot user), and ignore any of its own messages."
  if message.author == client.user:
    return
  #what is try?
  # what is causing the 4x responses
  try:
    # these ifs check special messages but... (line 38)
    if get_response(message.content) == "delete":
      #why is this needed?
      await message.delete()
      print("Good")
    elif get_response(message.content) == None:
      await message.delete()
      print("ERR")
    elif get_response(message.content) == "list mons":
      #bot posts all values from which database? is db the main database?
      keys = db.keys()
      for key in keys:
        print(db[key])
    # ...print eveything else otherwise
    else:
      await message.channel.send(get_response(message.content))
  except ValueError:
    print("Error")

#this is to connect to replit?
client.run(os.environ['SECRET_BOT_KEY'])

"""
1/29/24


"""
