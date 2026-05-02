import io
import logging
import random
import discord
import httpx

logger = logging.getLogger(__name__)

class Pokemon:
    def __init__(self, pokeapi, id):
        self.id = id
        self.ability = pokemon_ability(pokeapi["abilities"])
        self.cry = pokeapi['cries']['latest']
        self.name = pokeapi["name"].capitalize()
        self.sprite = pokeapi["sprites"]["other"]["official-artwork"]["front_default"]
        self.sprite_shiny = pokeapi["sprites"]["other"]["official-artwork"]["front_shiny"]
        self.types, self.color = pokemon_type(pokeapi["types"])

type_colors = {
    'bug': '#A6B91A',
    'dark': '#705746',
    'dragon': '#6F35FC',
    'electric': '#F7D02C',
    'fairy': '#D685AD',
    'fighting': '#C22E28',
    'fire': '#EE8130',
    'flying': '#A98FF3',
    'ghost': '#735797',
    'grass': '#7AC74C',
    'ground': '#E2BF65',
    'ice': '#96D9D6',
    'normal': '#A8A77A',
    'poison': '#A33EA1',
    'psychic': '#F95587',
    'rock': '#B6A136',
    'steel': '#B7B7CE',
    'water': '#6390F0'
}

def pokemon_ability(abilities):
    arr = []
    for a in abilities:
        arr.append(a["ability"]["name"].capitalize())
    return '/'.join(arr)

def pokemon_type(types):
    arr = []
    for t in types:
        arr.append(t["type"]["name"].capitalize())
    return '/'.join(arr), types[0]["type"]["name"]

async def pokemon_get(session: httpx.AsyncClient):
    n = random.randint(1,1025)
    url = f"https://pokeapi.co/api/v2/pokemon/{n}"
    resp = await session.get(url)
    resp.raise_for_status()
    poke = Pokemon(resp.json(), n)
    return await embed_creator(poke, session)

async def embed_creator(poke: Pokemon, session: httpx.AsyncClient):
    image_url = poke.sprite
    if random.randint(1,10) == 1:
        image_url = poke.sprite_shiny
    try:
        image_resp = await session.get(image_url)
        image_resp.raise_for_status()
        image_buffer = io.BytesIO(image_resp.content)
        image_file = discord.File(image_buffer, filename="poke.png")
    except Exception as e:
        logger.error(f"Error with image {e}")
        raise
    try:
        poke_color = type_colors[poke.color] or "#000000"
        embed = discord.Embed(title=poke.name,color=discord.Color.from_str(poke_color))
        embed.set_footer(text=poke.id)
        des = (f"Type: {poke.types}\n"
                f"Ability: {poke.ability}\n"
               )
        embed.description = des
        embed.set_image(url="attachment://poke.png")

        return embed, image_file
    except Exception as e:
        logger.error(f"Unknown error in building embed")
        raise



