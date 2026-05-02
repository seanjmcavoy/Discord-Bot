import asyncio

import discord
import httpx
from discord import app_commands
from apikeys import BOT_TOKEN
from fetchers import get_cat, get_dog
from pokemon import get_pokemon
from downloader import downloader

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("Online.")
    print('-' * 20 )
    #session to use with apis
    client.session = httpx.AsyncClient(timeout=httpx.Timeout(10.0))
    try:
        synced = await tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Error syncing commands: {e}")


#cat images
@tree.command(name="cat", description="cat image")
async def cat_command(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        resp = await get_cat(client.session)
        await interaction.followup.send(resp)
    except httpx.HTTPError as e:
        print(f"Network error in cat_command: {e}")
        await interaction.followup.send("Can't reach api")
    except (KeyError, IndexError) as e:
        print(f"Data error in cat_command: {e}")
        await interaction.followup.send("Error from the API.")
    except Exception as e:
        print(f"Unexpected error in cat_command: {e}")
        await interaction.followup.send("An unknown error occurred.")


#dog images
@tree.command(name="dog", description="dog image")
async def dog_command(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        resp = await get_dog(client.session)
        await interaction.followup.send(resp)
    except httpx.HTTPError as e:
        print(f"Network error in dog_command: {e}")
        await interaction.followup.send("Can't reach api")
    except (KeyError, IndexError) as e:
        print(f"Data error in dog_command: {e}")
        await interaction.followup.send("Error from the API.")
    except Exception as e:
        print(f"Unexpected error in dog_command: {e}")
        await interaction.followup.send("An unknown error occurred.")

#pokemon
@tree.command(name="pokemon", description="get pokemon")
async def poke_command(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        embed, image = await get_pokemon(client.session)
        if embed and image:
            await interaction.followup.send(embed=embed, file=image)
        else:
            await interaction.followup.send("Could not retrieve Pokemon data")
    except Exception as e:
        print(f"Error poke_command: {e}")
        await interaction.followup.send("Error getting pokemon")
         
@tree.command(name="mp4", description="video downloader")
async def mp4_command(interaction: discord.Interaction, link: str, name: str = ""):
    await interaction.response.defer()
    try:
        resp = await asyncio.to_thread(downloader, link, name)
        await interaction.followup.send(files=resp)
    except Exception as e:
        print(f"Error mp4_command: {e}")
        await interaction.followup.send("Error fetching video")

if __name__ == "__main__":
    client.run(BOT_TOKEN)
