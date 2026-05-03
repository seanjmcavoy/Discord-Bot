import io
import logging
import random
import discord
import httpx
logger = logging.getLogger(__name__)

#basic 1/10 chance for statrack
def weapon_stattrack():
    n = random.randint(1,10)
    if n == 1:
        return True
    return False
# basic float return
# TODO add input range for floats generation for different skins

def weapon_float():
    f = random.random()

    if f <= 0.07:
        return f, "Factory New"
    elif f <= 0.15:
        return f, "Minimal Wear",
    elif f <= 0.38:
        return f, "Well-Worn",
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
    WEIGHTS = [55,25,10,7.5,2.5]
    return random.choices(RARITIES, weights=WEIGHTS, k=1)[0]

#weapons case random weapon from given rarity
def weapon_case1_weapons(rarity):
    if rarity == "Red":
        return "AWP | Lightning Strike"
    PINK = [
        "AK-47 | Case Hardened",
        "Desert Eagle | Hypnotic"
    ]
    if rarity == "Pink":
        return random.choice(PINK)

    PURPLE = [
        "M4A1-S | Dark Water",
        "Glock-18 | Dragon Tattoo",
        "USP-S | Dark Water"
    ]

    if rarity == "Purple":
        return random.choice(PURPLE)

    BLUE = [
        "MP7 | Skulls",
        "AUG | Wings",
        "SG 553 | Ultraviolet"
    ]

    if rarity == "Blue":
        return random.choice(BLUE)

    GOLD = [
        "★ Bayonet | Forest DDPAT", "★ Bayonet | Scorched ",
        "★ Bayonet | Safari Mesh ", "★ Bayonet | Urban Masked ",
        "★ Bayonet | Night ", "★ Bayonet | Blue Steel ", "★ Bayonet | Stained ",
        "★ Bayonet | Case Hardened ",
        "★ Bayonet | Slaughter ", "★ Bayonet | Crimson Web ",
        "★ Bayonet | Fade ", "★ Bayonet | Boreal Forest ",
        "★ Bayonet",
        "★ Flip Knife | Forest DDPAT ", "★ Flip Knife | Scorched ",
        "★ Flip Knife | Safari Mesh ", "★ Flip Knife | Urban Masked ",
        "★ Flip Knife | Night ", "★ Flip Knife | Blue Steel ",
        "★ Flip Knife | Stained ", "★ Flip Knife | Case Hardened ",
        "★ Flip Knife | Slaughter ", "★ Flip Knife | Crimson Web ",
        "★ Flip Knife | Fade ", "★ Flip Knife | Boreal Forest ",
        "★ Flip Knife",
        "★ Gut Knife | Forest DDPAT ", "★ Gut Knife | Scorched ",
        "★ Gut Knife | Safari Mesh ", "★ Gut Knife | Urban Masked ",
        "★ Gut Knife | Night ", "★ Gut Knife | Blue Steel ",
        "★ Gut Knife | Stained ", "★ Gut Knife | Case Hardened ",
        "★ Gut Knife | Slaughter ", "★ Gut Knife | Crimson Web ",
        "★ Gut Knife | Fade ", "★ Gut Knife | Boreal Forest ",
        "★ Gut Knife",
        "★ Karambit | Forest DDPAT ", "★ Karambit | Scorched",
        "★ Karambit | Safari Mesh ", "★ Karambit | Urban Masked",
        "★ Karambit | Night ", "★ Karambit | Blue Steel",
        "★ Karambit | Stained ", "★ Karambit | Case Hardened",
        "★ Karambit | Slaughter ", "★ Karambit | Crimson Web",
        "★ Karambit | Fade ", "★ Karambit | Boreal Forest",
        "★ Karambit",
        "★ M9 Bayonet | Forest DDPAT ", "★ M9 Bayonet | Scorched",
        "★ M9 Bayonet | Safari Mesh ", "★ M9 Bayonet | Urban Masked",
        "★ M9 Bayonet | Night ", "★ M9 Bayonet | Blue Steel",
        "★ M9 Bayonet | Stained ", "★ M9 Bayonet | Case Hardened",
        "★ M9 Bayonet | Slaughter ", "★ M9 Bayonet | Crimson Web",
        "★ M9 Bayonet | Fade", "★ M9 Bayonet | Boreal Forest",
        "★ M9 Bayonet"
    ]

    return random.choice(GOLD)
# item ids with buff167 ids
# TODO add ids for each wear
item_ids = {
    "SG 553 | Ultraviolet": 36507,
    "AUG | Wings": 34063,
    "MP7 | Skulls": 35611,
    "USP-S | Dark Water": 42171,
    "Glock-18 | Dragon Tattoo": 35018,
    "M4A1-S | Dark Water": 35195,
    "Desert Eagle | Hypnotic": 34428,
    "AK-47 | Case Hardened": 33881,
    "AWP | Lightning Strike": 34099,
    "★ Bayonet | Forest DDPAT": 45654,
    "★ Bayonet | Scorched": 755936,
    "★ Bayonet | Safari Mesh": 42418,
    "★ Bayonet | Urban Masked": 42442,
    "★ Bayonet | Night": 44000,
    "★ Bayonet | Blue Steel": 42361,
    "★ Bayonet | Stained": 42430,
    "★ Bayonet | Case Hardened": 42376,
    "★ Bayonet | Slaughter": 42426,
    "★ Bayonet | Crimson Web": 45460,
    "★ Bayonet | Fade": 42391,
    "★ Bayonet | Boreal Forest": 42366,
    "★ Bayonet": 42349,
    "★ Flip Knife | Forest DDPAT": 42725,
    "★ Flip Knife | Scorched": 42756,
    "★ Flip Knife | Safari Mesh": 42751,
    "★ Flip Knife | Urban Masked": 755739,
    "★ Flip Knife | Night": 42744,
    "★ Flip Knife | Blue Steel": 42694,
    "★ Flip Knife | Stained": 42764,
    "★ Flip Knife | Case Hardened": 42707,
    "★ Flip Knife | Slaughter": 42760,
    "★ Flip Knife | Crimson Web": 45455,
    "★ Flip Knife | Fade": 42722,
    "★ Flip Knife | Boreal Forest": 756236,
    "★ Flip Knife": 42682,
    "★ Gut Knife | Forest DDPAT": 42823,
    "★ Gut Knife | Scorched": 44239,
    "★ Gut Knife | Safari Mesh": 42848,
    "★ Gut Knife | Urban Masked": 764072,
    "★ Gut Knife | Night": 755720,
    "★ Gut Knife | Blue Steel": 42791,
    "★ Gut Knife | Stained": 42860,
    "★ Gut Knife | Case Hardened": 42804,
    "★ Gut Knife | Slaughter": 42856,
    "★ Gut Knife | Crimson Web": 42809,
    "★ Gut Knife | Fade": 42820,
    "★ Gut Knife | Boreal Forest": 757222,
    "★ Gut Knife": 42779,
    "★ Karambit | Forest DDPAT": 44049,
    "★ Karambit | Scorched": 755926,
    "★ Karambit | Safari Mesh": 756412,
    "★ Karambit | Urban Masked": 756409,
    "★ Karambit | Night": 45649,
    "★ Karambit | Blue Steel": 44245,
    "★ Karambit | Stained": 43037,
    "★ Karambit | Case Hardened": 42985,
    "★ Karambit | Slaughter": 43033,
    "★ Karambit | Crimson Web": 45417,
    "★ Karambit | Fade": 43000,
    "★ Karambit | Boreal Forest": 42976,
    "★ Karambit": 42961,
    "★ M9 Bayonet | Forest DDPAT": 43095,
    "★ M9 Bayonet | Scorched": 43124,
    "★ M9 Bayonet | Safari Mesh": 45183,
    "★ M9 Bayonet | Urban Masked": 43962,
    "★ M9 Bayonet | Night": 43113,
    "★ M9 Bayonet | Blue Steel": 43064,
    "★ M9 Bayonet | Stained": 43132,
    "★ M9 Bayonet | Case Hardened": 43078,
    "★ M9 Bayonet | Slaughter": 43128,
    "★ M9 Bayonet | Crimson Web": 45454,
    "★ M9 Bayonet | Fade": 33812,
    "★ M9 Bayonet | Boreal Forest": 45224,
    "★ M9 Bayonet": 43052,
}
# buff api usage basic price and image
# TODO use more data later
async def buff_api(id, session: httpx.AsyncClient):
    url = f"https://buff.163.com/api/market/goods/info?game=csgo&goods_id={id}"
    resp = await session.get(url)
    resp.raise_for_status()
    resp = resp.json()
    url = resp["data"]["goods_info"]["icon_url"]
    price = float(resp["data"]["goods_info"]["steam_price_cny"])
    return url, f"${price*0.15:.2f} USD"
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
    wfloat = weapon_float()
    wstat = weapon_stattrack()
    wrare = weapon_rarity()
    wwep = weapon_case1_weapons(wrare)
    url, price = await buff_api(item_ids[wwep], session)

    try:
        image_resp = await session.get(url)
        image_resp.raise_for_status()
        image_buffer = io.BytesIO(image_resp.content)
        image_file = discord.File(image_buffer, filename="wep.png")
    except Exception as e:
        logger.error(f"Error with image {e}")
        raise

    if wstat:
        title = "StatTrak™ " + wwep
    else:
        title = wwep
    embed = discord.Embed(title=title, colour=color_rare[wrare])
    des = (f"Float: {wfloat}\n"
           f"Rarity: {wrare}")
    #embed.description = des
    #embed.set_footer(text=f"{price}")
    embed.set_image(url="attachment://wep.png")

    return embed, image_file
