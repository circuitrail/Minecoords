import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv


# Get bot token from the .env file
# The .env file should look like this: TOKEN=Your Token Here
load_dotenv()
TOKEN = os.getenv('TOKEN')


# Define variables

project_directory = os.getcwd()
data_file_path = project_directory + "/data.csv"


# Define functions

# Returns true if data.csv exists in the same directory as main.py, else returns false.
def data_file_exists():
    if os.path.exists(data_file_path):
        return True
    else:
        return False


# Define bot class
class Client(discord.Client):
    async def on_ready(self):
        print(f'\'sup, I\'m {self.user}!')


# Bot setup
intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)


# Bot slash commands
#@client.tree.command(name="", description="")


# Start up bot
client.run(TOKEN)

