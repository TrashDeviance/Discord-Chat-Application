from connection import client
import discord
import datetime
import time
import random


class Commands:
    def __init__(self):
        self.none = None

    @client.event
    async def on_message(self, message):
        if message.author == client.user:
            return


class HelpMe(Commands):
    async def on_message(self, message):
        await super().on_message(message)
        if message.content.startswith("$helpme"):
            await message.channel.send(f'Hello {message.author}, type \'$commands\' to receive a list of all commands.')


class CommandList(Commands):
    def __init__(self):
        super().__init__()
        self.list_commands = ['$helpme', '$commands', '$time', '$random#']

    async def on_message(self, message):
        await super().on_message(message)
        if message.content.startswith("$commands"):
            result = ''
            for commands in self.list_commands:
                result += f'{commands}\n'
            await message.author.send(f'Hello {message.author}, here is a list of available commands? \n{result}')


class Time(Commands):
    async def on_message(self, message):
        await super().on_message(message)
        if message.content.startswith('$time'):
            current_time = datetime.datetime.now()
            date_time = current_time.strftime("%A, %B %d %Y - %I:%M")
            await message.channel.send(f"The current time is {date_time}")


class Random_Number(Commands):
    async def on_message(self, message):
        await super().on_message(message)
        if message.content.startswith('$random#'):
            random_num = random.randint(0, 1000)
            await message.channel.send(f'Your random number is: {random_num}')


class Joke(Commands):
    def __init__(self):
        super().__init__()
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
        await super().on_message(message)
        if message.content.startswith('$joke'):
            random_joke_key = random.choice(list(self.dict_jokes.keys()))
            random_joke_value = self.dict_jokes[random_joke_key]
            await message.channel.send(random_joke_key)
            time.sleep(2)
            await message.channel.send(random_joke_value)
            await message.channel.send("Ha ha ha ha!")


help_me = HelpMe()
command_list = CommandList()
display_time = Time()
random_num = Random_Number()
jokes = Joke()

client.event(help_me.on_message)
client.event(command_list.on_message)
client.event(display_time.on_message)
client.event(random_num.on_message)
client.event(jokes.on_message)
