import io
import logging
import random
from random import choice
import cases.weaponsCase1 as CASE
import discord
import httpx
logger = logging.getLogger(__name__)

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
    CAPPED_WEAPONS = {
        "AWP | Lightning Strike": (0.00, 0.08),
        "Desert Eagle | Hypnotic": (0.00, 0.08),
        "Glock-18 | Dragon Tattoo": (0.00, 0.08),
        "M4A1-S | Dark Water": (0.10, 0.26),
        "USP-S | Dark Water": (0.10, 0.26),
        "AUG | Wings": (0.00, 0.14),
        "MP7 | Skulls": (0.10, 0.26),
        "SG 553 | Ultraviolet": (0.06, 0.80),
    }
    KNIFE_CAPS_08 = ["Fade", "Slaughter"]
    KNIFE_CAPS_80 = ["Crimson Web", "Night", "Boreal Forest", "Forest DDPAT", "Safari Mesh", "Urban Masked", "Scorched"]

    if skin_name in CAPPED_WEAPONS:
        return CAPPED_WEAPONS[skin_name]

    if skin_name.startswith("★"):
        if any(finish in skin_name for finish in KNIFE_CAPS_08):
            return (0.00, 0.08)
        if any(finish in skin_name for finish in KNIFE_CAPS_80):
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

# rarity [79.92, 15.98, 3.2, 0.64, 0.26] offical odds
# using boosted odds
def weapon_rarity():
    RARITIES = [
        "Blue",
        "Purple",
        "Pink",
        "Red",
        "Gold",
    ]
    #WEIGHTS = [79.92, 15.98, 3.2, 0.64, 0.26]
    WEIGHTS = [69,20,7.5,2.5,1]
    return random.choices(RARITIES, weights=WEIGHTS, k=1)[0]

#weapons case random weapon from given rarity
def weapons_base_name(rarity):
    if rarity == "Red":
        return random.choice(CASE.RED)

    if rarity == "Pink":
        return random.choice(CASE.PINK)

    if rarity == "Purple":
        return random.choice(CASE.PURPLE)

    if rarity == "Blue":
        return random.choice(CASE.BLUE)

    return random.choice(CASE.GOLD)

# buff api usage basic price and image
# TODO use more data later
async def buff_api(id, session: httpx.AsyncClient):
    url = f"https://buff.163.com/api/market/goods/info?game=csgo&goods_id={id}"
    resp = await session.get(url)
    resp.raise_for_status()
    resp = resp.json()
    url = resp["data"]["goods_info"]["icon_url"]
    price = resp['data']['steam_market_url']
    return url, price

#items colors
# TODO get exact colors valve use
color_rare = {
        "Blue": discord.Color.from_str("#002bff"),
        "Purple": discord.Color.purple(),
        "Pink": discord.Color.pink(),
        "Red": discord.Color.red(),
        "Gold": discord.Color.gold(),
}

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
        image_file = discord.File(image_buffer, filename="wep.png")
    except Exception as e:
        logger.error(f"Error with image {e}")
        raise

    title = weapon
    embed = discord.Embed(title=title, colour=color_rare[rarity])
    des = (
            f"{wfloat[0]:.7f}\n"
            f"{weapon_pattern()}\n"
            f"[Market]({price})"
           )
    embed.description = des
    embed.set_image(url="attachment://wep.png")


    return embed, image_file
