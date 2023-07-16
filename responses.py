import discord
from connection import client, GUILD_ID
from colorama import *


# Called when a Member joins a Guild.
@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels)  # discord.utils to simplify common tasks
    message = f'Welcome to {member.guild.name}, **{member.name}**! \n\nType in chat with a \'$helpme\' to receive help!'
    await channel.send(message)


# Called when a Member leaves a Guild.
@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels)
    message = f"We lost a member today 😔. RIP, **{member.name}**!"
    await channel.send(message)


# Called when a Member updates their profile.

@client.event
async def on_member_update(before, after):
    # global timeout

    # Used to show when a user has updated their nickname
    async def update_nickname():
        if before.nick != after.nick:
            channel = discord.utils.get(after.guild.text_channels)
            message = f'{after.name}\'s nickname {before.nick}, has been changed to {after.nick}!'
            await channel.send(message)

    await update_nickname()

    # Shows when a user has updated one of their roles
    async def updated_role():
        if before.roles != after.roles:
            channel = discord.utils.get(after.guild.text_channels)

            # Storing the actual names of the roles instead of their ids
            before_role_list = []
            for role in before.roles:
                before_role_list.append(role.name)

            after_role_list = []
            for role in after.roles:
                after_role_list.append(role.name)

            message = f'{after.name}\'s role\'s have been changed from {before_role_list} to {after_role_list}'
            await channel.send(message)

    await updated_role()

    # Sends a message when a user has been put in timeout mode
    # timeout = False
    #
    # async def update_timeout(set_time):
    #     if before.timeout != after.timeout and set_time == False:
    #         channel = discord.utils.get(after.guild.text_channels)
    #         message = f'{after.name}\'s account has been put into timeout mode!'
    #         set_time = True
    #         print(f'if: {set_time}')
    #         await channel.send(message)
    #
    #     elif before.timeout != after.timeout and set_time == True:
    #         channel = discord.utils.get(after.guild.text_channels)
    #         message = f'{after.name}\'s account has been put into timeout mode!'
    #         set_time = False
    #         print(f'elif: {set_time}')
    #         await channel.send(message)
    #
    # await update_timeout(timeout)

    # Sends a message with the updated avatar for the user
    async def update_avatar():
        if before.avatar != after.avatar:
            channel = discord.utils.get(after.guild.text_channels)
            message = f'{after.name}\'s guild avatar {before.avatar}, has been changed to {after.avatar}!'
            await channel.send(message)

    await update_avatar()


@client.event
async def on_member_ban(guild, user):
    pass