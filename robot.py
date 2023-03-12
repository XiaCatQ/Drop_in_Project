# bot.py
import search_dropin

# instantiate BadmintonWeb class from search_dropin.py
badminton_web = search_dropin.BadmintonWeb()

# no result message 
no_result_message = '''Sorry, we can\'t find what you are searching for. We will check again next hour.'''



import os
import random
import time

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# intents = discord.Intents.default()
# intents.message_content = True
intents = discord.Intents().all()

client = discord.Client(command_prefix=',', intents=intents)
                        
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    print(message.content)
    if message.author == client.user:
        return  
  # lower case message
    message_content = message.content.lower()  

  
    if message.content.startswith(f'$hello'):
        await message.channel.send('Hello there! I\'m the badminton assistant.')
    
    if f'$start' in message_content:
        while True:
            await message.channel.send('$search 中上')
            key_words, search_words = badminton_web.key_words_search_words(message_content)
            day_link = badminton_web.search(key_words)
            links = badminton_web.send_link(day_link, search_words)
            
            link_str = ""
            if len(links) > 0:
                for link in links:
                    link_str = link_str + link +"\n"
                await message.channel.send(link_str)
            else:
                await message.channel.send(no_result_message)
            
            time.sleep(30)
    
    if f'$search' in message_content:

        key_words, search_words = badminton_web.key_words_search_words(message_content)
        day_link = badminton_web.search(key_words)
        links = badminton_web.send_link(day_link, search_words)
        
        link_str = ""
        if len(links) > 0:
            for link in links:
                for link in links:
                    link_str = link_str + link +"\n"
                await message.channel.send(link_str)
        else:
            await message.channel.send(no_result_message)

client.run(TOKEN)