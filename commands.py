from connection import *
import discord
import datetime
import time
import random

# from responses import play


# Parent class that all other command child classes will inherit from
class Commands:
    def __init__(self, client):
        self.client = client  # attribute that will be used in every unique command subclass

    @client.event
    async def on_message(self, message):  # grab this variable and pass it into the Commands class constructor
        # Prevent the message from a bot being saved
        if message.author == client.user:
            return


# Command will show additional information to the user to help them
class HelpMe(Commands):
    # Here is an example if I wanted to define a constructor to potentially add more attributes to this specific object
    # def __init__(self, client):
    #     super().__init__(client)
    async def on_message(self, message):
        if message.content.startswith("$helpme"):
            await message.channel.send(f'Hello {message.author}, type \'$commands\' to receive a list of all commands.')


# Command will show the user all the available commands
class CommandList(Commands):
    def __init__(self, client):
        super().__init__(client)
        self.list_commands = ['$helpme', '$commands', '$time', '$random#', '$joke', '$members', '$#members', '$showguild']  # store all commands in list and send to user upon request

    async def on_message(self, message):
        if message.content.startswith("$commands"):
            result = ''
            for commands in self.list_commands:
                result += f'{commands}\n'
            await message.author.send(f'Hello {message.author}, here is a list of available commands? \n{result}')


# Command will return the current time
class Time(Commands):
    async def on_message(self, message):
        if message.content.startswith('$time'):
            current_time = datetime.datetime.now()
            date_time = current_time.strftime("%A, %B %d %Y - %I:%M")
            await message.channel.send(f"The current time is {date_time}")


# Command will return a random number from 0-1000
class RandomNum(Commands):
    async def on_message(self, message):
        if message.content.startswith('$random#'):
            random_num = random.randint(0, 1000)
            await message.channel.send(f'Your random number is: {random_num}')


# Command will tell a random joke from the dictionary of jokes
class Joke(Commands):
    def __init__(self, client):
        super().__init__(client)
        self.dict_jokes = {
            'What animal loves a baseball game?': 'A bat.',
            'What is black and white and red all over?': 'An embarrassed zebra.',
            'Where is a cow\'s favorite place to go?': 'The mooooovies.',
            'What do you call an alligator that solves mysteries?': 'An investi-gator.',
            'What is an astronaut\'s favorite button on a keyboard?': 'The spacebar.',
            'Why did the alien go to the doctor?': 'He was looking a little green.',
            'What did Venus say to Saturn?': 'Give me a ring.'
        }

    async def on_message(self, message):
        if message.content.startswith('$joke'):
            random_joke_key = random.choice(list(self.dict_jokes.keys()))
            random_joke_value = self.dict_jokes[random_joke_key]
            await message.channel.send(random_joke_key)
            time.sleep(2)
            await message.channel.send(random_joke_value)
            await message.channel.send("Ha ha ha ha!")


# Command will show all users in guild and their names
class ShowMembers(Commands):
    def __init__(self, client):
        super().__init__(client)
        self.dict_users = {}

    async def on_message(self, message):

        if message.content.startswith('$members'):
            # Returns all the members of that guild
            my_guild = message.guild
            await message.channel.send(self.get_list_of_members(my_guild))

        elif message.content.startswith("$#members"):
            # Will return the number of users in the guild
            num_members = self.number_of_members(message.guild.members)
            await message.channel.send(num_members)

    # Returns all the members of that guild
    def get_list_of_members(self, my_guild):
        self.dict_users = {}  # Store the key, value of users and their corresponding discriminator

        # Add the unique users and their discriminator to the dict_users
        members = my_guild.members
        for member in members:
            if member.name not in self.dict_users:
                self.dict_users[member.name] = member.discriminator

        # Format the users to make it look more organized
        member_list = ""
        for name, discriminator in self.dict_users.items():
            member_list += f"Username: {name} | Discriminator: {discriminator}\n"

        return member_list

    # Will return the number of users in the guild
    def number_of_members(self, guild_members) -> str:
        num_members = len(guild_members)
        message = f'Number of members: {num_members}'
        return message


# Command will show the current name of the guild
class ShowGuild(Commands):
    def __init__(self, client):
        super().__init__(client)

    async def on_message(self, message):
        if message.content.startswith('$showguild'):
            # Returns only the guild
            def get_guild():
                guild_name = client.get_guild(int(GUILD_ID))
                # print(dir(guild_name))
                if guild_name:
                    return guild_name
                else:
                    return None

            await message.channel.send(f"Current Guild: {get_guild()}")

# class PlaySong(Commands):
#     def __init__(self, client):
#         super().__init__(client)
#
#     async def on_message(self, message):
#         await super().on_message(message)
#         if message.content.startswith("$playsong"):
#             channel = discord.utils.get(client.guild.voice_channel, name="General")
#             voice_channel = await channel.connect()


# Stored all messages send by all members into a dictionary
class StoreMessageFromUserDict(Commands):
    def __init__(self, client):
        super().__init__(client)

        # Storing messages into a dictionary
        self.dict_store_messages = {}
        self.list_testing = []

    async def on_message(self, message):

        # Prevent the message from a bot being saved
        if message.author == client.user:
            return

        # Name of the individual who sent message
        author_name = message.author.name

        # If author is not in the dictionary, add them with an empty list
        if author_name not in self.dict_store_messages:
            self.dict_store_messages[author_name] = []

        # Append the message content to the list for this author
        self.dict_store_messages[author_name].append(message.content)

        if message.content.startswith("$all_messages"):
            await message.channel.send(self.dict_store_messages)


# Creating objects for each command
help_me = HelpMe(client)
command_list = CommandList(client)
display_time = Time(client)
random_num = RandomNum(client)
jokes = Joke(client)
show_guild = ShowGuild(client)
show_members = ShowMembers(client)
stored_messages_dict = StoreMessageFromUserDict(client)
# play_song = PlaySong(client)


# Objects will be waiting for user to type in a message
@client.event
async def on_message(message):
    await help_me.on_message(message)
    await command_list.on_message(message)
    await display_time.on_message(message)
    await random_num.on_message(message)
    await jokes.on_message(message)
    await show_guild.on_message(message)
    await show_members.on_message(message)
    await stored_messages_dict.on_message(message)
    # await play_song.on_message(message)


