import io
import logging
import random
import discord
import httpx
logger = logging.getLogger(__name__)
def weapon_stattrack():
    n = random.randint(1,10)
    if n == 1:
        return True
    return False

def weapon_float():
    tiers_floats = {
        0.07 : "Factory New",
        0.15 : "Minimal Wear",
        0.38 : "Well-Worn",
        1.0  : "Battle-Scarred"
    }
    f = random.random()

    if f <= 0.07:
        return f, "Factory New"
    elif f <= 0.15:
        return f, "Minimal Wear",
    elif f <= 0.38:
        return f, "Well-Worn",
    else:
        return f, "Battle-Scarred"

def weapon_rarity():
    RARITIES = [
        "Blue",
        "Purple",
        "Pink",
        "Red",
        "Gold",
    ]
    #WEIGHTS = [79.92, 15.98, 3.2, 0.64, 0.26]
    WEIGHTS = [45,25,15,10,5]
    return random.choices(RARITIES, weights=WEIGHTS, k=1)[0]

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
        "★ Bayonet | Forest DDPAT (Factory New)", "★ Bayonet | Scorched (Factory New)",
        "★ Bayonet | Safari Mesh (Factory New)", "★ Bayonet | Urban Masked (Factory New)",
        "★ Bayonet | Night (Factory New)", "★ Bayonet | Blue Steel (Factory New)", "★ Bayonet | Stained (Factory New)",
        "★ Bayonet | Case Hardened (Factory New)",
        "★ Bayonet | Slaughter (Factory New)", "★ Bayonet | Crimson Web (Factory New)",
        "★ Bayonet | Fade (Factory New)", "★ Bayonet | Boreal Forest (Factory New)",
        "★ Bayonet",
        "★ Flip Knife | Forest DDPAT (Factory New)", "★ Flip Knife | Scorched (Factory New)",
        "★ Flip Knife | Safari Mesh (Factory New)", "★ Flip Knife | Urban Masked (Factory New)",
        "★ Flip Knife | Night (Factory New)", "★ Flip Knife | Blue Steel (Factory New)",
        "★ Flip Knife | Stained (Factory New)", "★ Flip Knife | Case Hardened (Factory New)",
        "★ Flip Knife | Slaughter (Factory New)", "★ Flip Knife | Crimson Web (Factory New)",
        "★ Flip Knife | Fade (Factory New)", "★ Flip Knife | Boreal Forest (Factory New)",
        "★ Flip Knife",
        "★ Gut Knife | Forest DDPAT (Factory New)", "★ Gut Knife | Scorched (Factory New)",
        "★ Gut Knife | Safari Mesh (Factory New)", "★ Gut Knife | Urban Masked (Factory New)",
        "★ Gut Knife | Night (Factory New)", "★ Gut Knife | Blue Steel (Factory New)",
        "★ Gut Knife | Stained (Factory New)", "★ Gut Knife | Case Hardened (Factory New)",
        "★ Gut Knife | Slaughter (Factory New)", "★ Gut Knife | Crimson Web (Factory New)",
        "★ Gut Knife | Fade (Factory New)", "★ Gut Knife | Boreal Forest (Factory New)",
        "★ Gut Knife",
        "★ Karambit | Forest DDPAT (Factory New)", "★ Karambit | Scorched (Factory New)",
        "★ Karambit | Safari Mesh (Factory New)", "★ Karambit | Urban Masked (Factory New)",
        "★ Karambit | Night (Factory New)", "★ Karambit | Blue Steel (Factory New)",
        "★ Karambit | Stained (Factory New)", "★ Karambit | Case Hardened (Factory New)",
        "★ Karambit | Slaughter (Factory New)", "★ Karambit | Crimson Web (Factory New)",
        "★ Karambit | Fade (Factory New)", "★ Karambit | Boreal Forest (Factory New)",
        "★ Karambit",
        "★ M9 Bayonet | Forest DDPAT (Factory New)", "★ M9 Bayonet | Scorched (Factory New)",
        "★ M9 Bayonet | Safari Mesh (Factory New)", "★ M9 Bayonet | Urban Masked (Factory New)",
        "★ M9 Bayonet | Night (Factory New)", "★ M9 Bayonet | Blue Steel (Factory New)",
        "★ M9 Bayonet | Stained (Factory New)", "★ M9 Bayonet | Case Hardened (Factory New)",
        "★ M9 Bayonet | Slaughter (Factory New)", "★ M9 Bayonet | Crimson Web (Factory New)",
        "★ M9 Bayonet | Fade (Factory New)", "★ M9 Bayonet | Boreal Forest (Factory New)",
        "★ M9 Bayonet"
    ]

    return random.choice(GOLD)

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
    "★ Bayonet | Forest DDPAT (Factory New)": 45654,
    "★ Bayonet | Scorched (Factory New)": 755936,
    "★ Bayonet | Safari Mesh (Factory New)": 42418,
    "★ Bayonet | Urban Masked (Factory New)": 42442,
    "★ Bayonet | Night (Factory New)": 44000,
    "★ Bayonet | Blue Steel (Factory New)": 42361,
    "★ Bayonet | Stained (Factory New)": 42430,
    "★ Bayonet | Case Hardened (Factory New)": 42376,
    "★ Bayonet | Slaughter (Factory New)": 42426,
    "★ Bayonet | Crimson Web (Factory New)": 45460,
    "★ Bayonet | Fade (Factory New)": 42391,
    "★ Bayonet | Boreal Forest (Factory New)": 42366,
    "★ Bayonet": 42349,
    "★ Flip Knife | Forest DDPAT (Factory New)": 42725,
    "★ Flip Knife | Scorched (Factory New)": 42756,
    "★ Flip Knife | Safari Mesh (Factory New)": 42751,
    "★ Flip Knife | Urban Masked (Factory New)": 755739,
    "★ Flip Knife | Night (Factory New)": 42744,
    "★ Flip Knife | Blue Steel (Factory New)": 42694,
    "★ Flip Knife | Stained (Factory New)": 42764,
    "★ Flip Knife | Case Hardened (Factory New)": 42707,
    "★ Flip Knife | Slaughter (Factory New)": 42760,
    "★ Flip Knife | Crimson Web (Factory New)": 45455,
    "★ Flip Knife | Fade (Factory New)": 42722,
    "★ Flip Knife | Boreal Forest (Factory New)": 756236,
    "★ Flip Knife": 42682,
    "★ Gut Knife | Forest DDPAT (Factory New)": 42823,
    "★ Gut Knife | Scorched (Factory New)": 44239,
    "★ Gut Knife | Safari Mesh (Factory New)": 42848,
    "★ Gut Knife | Urban Masked (Factory New)": 764072,
    "★ Gut Knife | Night (Factory New)": 755720,
    "★ Gut Knife | Blue Steel (Factory New)": 42791,
    "★ Gut Knife | Stained (Factory New)": 42860,
    "★ Gut Knife | Case Hardened (Factory New)": 42804,
    "★ Gut Knife | Slaughter (Factory New)": 42856,
    "★ Gut Knife | Crimson Web (Factory New)": 42809,
    "★ Gut Knife | Fade (Factory New)": 42820,
    "★ Gut Knife | Boreal Forest (Factory New)": 757222,
    "★ Gut Knife": 42779,
    "★ Karambit | Forest DDPAT (Factory New)": 44049,
    "★ Karambit | Scorched (Factory New)": 755926,
    "★ Karambit | Safari Mesh (Factory New)": 756412,
    "★ Karambit | Urban Masked (Factory New)": 756409,
    "★ Karambit | Night (Factory New)": 45649,
    "★ Karambit | Blue Steel (Factory New)": 44245,
    "★ Karambit | Stained (Factory New)": 43037,
    "★ Karambit | Case Hardened (Factory New)": 42985,
    "★ Karambit | Slaughter (Factory New)": 43033,
    "★ Karambit | Crimson Web (Factory New)": 45417,
    "★ Karambit | Fade (Factory New)": 43000,
    "★ Karambit | Boreal Forest (Factory New)": 42976,
    "★ Karambit": 42961,
    "★ M9 Bayonet | Forest DDPAT (Factory New)": 43095,
    "★ M9 Bayonet | Scorched (Factory New)": 43124,
    "★ M9 Bayonet | Safari Mesh (Factory New)": 45183,
    "★ M9 Bayonet | Urban Masked (Factory New)": 43962,
    "★ M9 Bayonet | Night (Factory New)": 43113,
    "★ M9 Bayonet | Blue Steel (Factory New)": 43064,
    "★ M9 Bayonet | Stained (Factory New)": 43132,
    "★ M9 Bayonet | Case Hardened (Factory New)": 43078,
    "★ M9 Bayonet | Slaughter (Factory New)": 43128,
    "★ M9 Bayonet | Crimson Web (Factory New)": 45454,
    "★ M9 Bayonet | Fade (Factory New)": 33812,
    "★ M9 Bayonet | Boreal Forest (Factory New)": 45224,
    "★ M9 Bayonet": 43052,
}

async def buff_api(id, session: httpx.AsyncClient):
    url = f"https://buff.163.com/api/market/goods/info?game=csgo&goods_id={id}"
    resp = await session.get(url)
    resp.raise_for_status()
    resp = resp.json()
    url = resp["data"]["goods_info"]["icon_url"]
    price = float(resp["data"]["goods_info"]["steam_price_cny"])
    return url, f"${price*0.15:.2f} USD"

color_rare = {
        "Blue": discord.Color.blue(),
        "Purple": discord.Color.purple(),
        "Pink": discord.Color.pink(),
        "Red": discord.Color.red(),
        "Gold": discord.Color.gold(),
}


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
