import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv


# Get bot token from the .env file
# The .env file should look like this: TOKEN=Your Token Here
load_dotenv()
TOKEN = os.getenv('TOKEN')


# Bot setup
intents = discord.Intents.default()
intents.message_content = True


# Bot initialization

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(f"Error syncing commands: {e}")


# Bot slash commands
@bot.tree.command(name="ping", description="Test bot status")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Pong!')


# Start up bot
bot.run(TOKEN)

