import io
import logging
import random
from random import choice
import cases.weaponsCase1 as CASE
import discord
import httpx
logger = logging.getLogger(__name__)

color_rarity = {
        "Blue": discord.Color.from_str("#4B69FF"),
        "Purple": discord.Color.from_str("#8847FF"),
        "Pink": discord.Color.from_str("#D32CE6"),
        "Red": discord.Color.from_str("#EB4B4B"),
        "Gold": discord.Color.from_str("#FFD700"),
}

#basic 1/10 chance for statrack
def weapon_stattrack():
    n = random.randint(1,10)
    if n == 1:
        return "StatTrak™ "
    return ""

#weapon pattern
def weapon_pattern():
    return random.randint(0,999)

def get_float_range(skin_name):

    if skin_name in CASE.CAPPED_WEAPONS:
        return CASE.CAPPED_WEAPONS[skin_name]

    if skin_name.startswith("★"):
        if any(finish in skin_name for finish in CASE.KNIFE_CAPS_08):
            return (0.00, 0.08)
        if any(finish in skin_name for finish in CASE.KNIFE_CAPS_80):
            return (0.06, 0.80)

    return (0.00, 1.00)

def weapon_float(s, e):
    f = random.uniform(s, e)
    if f <= 0.07:
        return f, "Factory New"
    elif f <= 0.15:
        return f, "Minimal Wear"
    elif f <= 0.38:
        return f, "Field-Tested"
    elif f <= 0.45:
        return f, "Well-Worn"
    else:
        return f, "Battle-Scarred"

# using boosted odds
def weapon_rarity():
    RARITIES = [
        "Blue",
        "Purple",
        "Pink",
        "Red",
        "Gold",
    ]
    # valve estimate 
    #WEIGHTS = [79.92, 15.98, 3.2, 0.64, 0.26]
    WEIGHTS = [69,20,7.5,2.5,1]
    return random.choices(RARITIES, weights=WEIGHTS, k=1)[0]

#weapons case random weapon from given rarity
def weapons_base_name(rarity):
    if rarity == "Red":
        n = len(CASE.RED)-1
        return CASE.RED[random.randint(0, n)]

    if rarity == "Pink":
        n = len(CASE.PINK)-1
        return CASE.PINK[random.randint(0, n)]

    if rarity == "Purple":
        n = len(CASE.PURPLE)-1
        return CASE.PURPLE[random.randint(0, n)]

    if rarity == "Blue":
        n = len(CASE.BLUE)-1
        return CASE.BLUE[random.randint(0, n)]
    
    n = len(CASE.GOLD)-1
    return CASE.GOLD[random.randint(0, n)]


# buff api usage basic price and image
# TODO use more data later
async def buff_api(id, session: httpx.AsyncClient):
    url = f"https://buff.163.com/api/market/goods/info?game=csgo&goods_id={id}"
    resp = await session.get(url)
    resp.raise_for_status()
    resp = resp.json()
    url = resp["data"]["goods_info"]["icon_url"]
    steam_url = resp['data']['steam_market_url']
    return url, steam_url


#entry function
async def case_open(session: httpx.AsyncClient):
    rarity = weapon_rarity()
    base = weapons_base_name(rarity)
    s,e = get_float_range(str(base))
    wfloat = weapon_float(s,e)
    statrack = weapon_stattrack()
    weapon = f"{statrack}{base} ({wfloat[1]})"

    url, price = await buff_api(CASE.item_ids[weapon], session)
    try:
        image_resp = await session.get(url)
        image_resp.raise_for_status()
        image_buffer = io.BytesIO(image_resp.content)
        image_file = discord.File(image_buffer, filename="skin.png")
    except Exception as e:
        logger.error(f"Error with image {e}")
        raise

    title = weapon
    embed = discord.Embed(title=title, colour=color_rarity[rarity])
    des = (
            f"{wfloat[0]:.7f}\n"
            f"{weapon_pattern()}\n"
            f"[Market]({price})"
           )
    embed.description = des
    embed.set_image(url="attachment://skin.png")

    return embed, image_file
