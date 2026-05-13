import asyncio
import logging
import discord
import httpx
from discord import app_commands
from yt_dlp.utils import DownloadError
from apikeys import BOT_TOKEN
from fetchers import get_cat, get_dog, get_waifu, get_art
from pokemon import pokemon_get
from downloader import mp4, gif
from logger import setup_logger
from caseSimulator import case_open

class BotClient(discord.Client):
    session: httpx.AsyncClient

intents = discord.Intents.default()
client = BotClient(intents=intents)
tree = app_commands.CommandTree(client)

setup_logger()
logger = logging.getLogger(__name__)

@client.event
async def on_ready():
    logger.info("Online.")
    #session to use with apis
    client.session = httpx.AsyncClient(timeout=httpx.Timeout(10.0))
    try:
        synced = await tree.sync()
        logger.info(f"Synced {len(synced)} command(s)")
    except Exception as e:
        logger.error(f"Error syncing commands: {e}")

#cat images
@tree.command(name="cat", description="cat image")
async def cat_command(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        resp = await get_cat(client.session)
        await interaction.followup.send(resp)
    except (httpx.HTTPError, httpx.HTTPStatusError) as e:
        logger.warning(f"Network error: {e}")
        await interaction.followup.send("Can't reach api")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        await interaction.followup.send("An unknown error occurred.")

#dog images
@tree.command(name="dog", description="dog image")
async def dog_command(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        resp = await get_dog(client.session)
        await interaction.followup.send(resp)
    except (httpx.HTTPError, httpx.HTTPStatusError) as e:
        logger.warning(f"Network error: {e}")
        await interaction.followup.send("Can't reach api")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        await interaction.followup.send("An unknown error occurred.")
#anime images
@tree.command(name="waifu", description="waifu image (NO AI)")
async def waifu_command(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        resp = await get_waifu(client.session)
        await interaction.followup.send(resp)
    except (httpx.HTTPError, httpx.HTTPStatusError) as e:
        logger.warning(f"Network error: {e}")
        await interaction.followup.send("Can't reach api")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        await interaction.followup.send("An unknown error occurred.")

#art images
@tree.command(name="art", description="European art ")
async def art_command(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        resp = await get_art(client.session)
        await interaction.followup.send(resp)
    except (httpx.HTTPError, httpx.HTTPStatusError) as e:
        logger.warning(f"Network error: {e}")
        await interaction.followup.send("Can't reach api")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        await interaction.followup.send("An unknown error occurred.")

#pokemon
@tree.command(name="pokemon", description="get pokemon")
async def poke_command(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        embed, image = await pokemon_get(client.session)
        if embed is None or image is None:
            await interaction.followup.send("Error in building embed")
        else:
            await interaction.followup.send(embed=embed, file=image)
    except (httpx.HTTPError, httpx.HTTPStatusError) as e:
        logger.warning(f"Network error: {e}")
        await interaction.followup.send("Can't reach api")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        await interaction.followup.send("An unknown error occurred.")

#case
@tree.command(name="case", description="weapons case boosted odds")
async def case_command(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        embed, image = await case_open(client.session)
        if embed is None or image is None:
            await interaction.followup.send("Error in building embed")
        else:
            await interaction.followup.send(embed=embed, file=image)
    except (httpx.HTTPError, httpx.HTTPStatusError) as e:
        logger.warning(f"Network error: {e}")
        await interaction.followup.send("Can't reach api")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        await interaction.followup.send("An unknown error occurred.")

#mp4
@tree.command(name="mp4", description="video downloader")
@app_commands.describe(link= "Tested X, Youtube, Reddit- 3 may 26" ,name = "Optional name for file")
async def mp4_command(interaction: discord.Interaction, link: str, name: str = ""):
    await interaction.response.defer()
    try:
        resp = await asyncio.to_thread(mp4, link, name)
        logger.info("returning file for link=%s",link)
        await interaction.followup.send(file=resp)
    except DownloadError as e:
        logger.error(f"User request failed: {e}")
        await interaction.followup.send(f"API failed")
    except Exception as e:
        logger.error(f"Error mp4_command: {e}")
        await interaction.followup.send("Can't download. Cant get below 10MB or Error")

#gif
@tree.command(name="gif", description="gif downloader")
@app_commands.describe(link= "Tested X, pixiv - 3 may" ,name = "Optional name for file")
async def gif_command(interaction: discord.Interaction, link: str, name: str = ""):
    await interaction.response.defer()
    try:
        resp = await asyncio.to_thread(gif, link, name)
        logger.info("returning file for link=%s",link)
        await interaction.followup.send(file=resp)
    except DownloadError as e:
        logger.error(f"User request failed: {e}")
        await interaction.followup.send(f"API failed")
    except Exception as e:
        logger.error(f"Error gif command: {e}")
        await interaction.followup.send("Can't download. Cant get below 10MB or Error")

if __name__ == "__main__":
    client.run(BOT_TOKEN, log_handler=None)
