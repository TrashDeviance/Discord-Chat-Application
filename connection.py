import discord
import os
import guild as guild  # Used for the get_guild_and_members()
from dotenv import load_dotenv  # used to store sensitive information like an API key

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')  # # Access the Discord token

# Check to see if the TOKEN variable is None or not
if TOKEN is not None:
    print("Discord API TOKEN loaded successfully!")

GUILD_ID = os.getenv('GUILD_ID')

# What actions bot should listen out for
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True


client = discord.Client(command_prefix='$', intents=intents) # Bot will listen for $


# Client Connection to Discord
establish_connection = True


while establish_connection:
    try:
        @client.event
        async def on_ready():
            print(f'{client.user}, has connected to {client.get_guild(int(GUILD_ID))} successfully!')

    except TypeError:
        print('''you have passed a function or an object to a function that expects a coroutine, but the passed function
         or object is not a coroutine.''')
    finally:
        break


# Retrieve the guild and all the users of the guild
def get_guild_and_members():
    current_guild = ''
    for current_guild in client.guilds:
        if current_guild.name == GUILD_ID:
            return guild

    member_dict = {}

    print(f'UserName')
    print(f'-------------------------------------------------------------------------------------------')
    for user in current_guild.members:
        member_dict[user.name] = f"ID: {user.discriminator}"
        print(f'{user.name} -> #{user.discriminator}')
    return member_dict



