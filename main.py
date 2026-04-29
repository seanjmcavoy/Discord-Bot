
import discord
import httpx
from discord import app_commands
from apikeys import BOT_TOKEN
from fetchers import get_cat, get_dog
from pokemon import get_pokemon

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    print("Online.")
    print('-' * 20 )
    client.session = httpx.AsyncClient()
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
    except Exception as e:
        print(f"Error cat_command: {e}")
        await interaction.followup.send("Error fetching image.")

#dog images
@tree.command(name="dog", description="dog image")
async def dog_command(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        resp = await get_dog(client.session)
        await interaction.followup.send(resp)
    except Exception as e:
        print(f"Error dog_command: {e}")
        await interaction.followup.send("Error fetching image.")

#pokemon
@tree.command(name="pokemon", description="get pokemon")
async def poke_command(interaction: discord.Interaction):
    await interaction.response.defer()
    embed, image = await get_pokemon(client.session)
    await interaction.followup.send(embed=embed, file=image)




if __name__ == "__main__":
    client.run(BOT_TOKEN)
