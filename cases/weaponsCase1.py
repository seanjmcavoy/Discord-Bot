GOLD = [
    "★ Bayonet | Forest DDPAT", "★ Bayonet | Scorched",
    "★ Bayonet | Safari Mesh", "★ Bayonet | Urban Masked",
    "★ Bayonet | Night", "★ Bayonet | Blue Steel", "★ Bayonet | Stained",
    "★ Bayonet | Case Hardened ",
    "★ Bayonet | Slaughter", "★ Bayonet | Crimson Web",
    "★ Bayonet | Fade", "★ Bayonet | Boreal Forest",
    "★ Bayonet",
    "★ Flip Knife | Forest DDPAT", "★ Flip Knife | Scorched",
    "★ Flip Knife | Safari Mesh", "★ Flip Knife | Urban Masked",
    "★ Flip Knife | Night", "★ Flip Knife | Blue Steel",
    "★ Flip Knife | Stained", "★ Flip Knife | Case Hardened",
    "★ Flip Knife | Slaughter", "★ Flip Knife | Crimson Web",
    "★ Flip Knife | Fade", "★ Flip Knife | Boreal Forest",
    "★ Flip Knife",
    "★ Gut Knife | Forest DDPAT", "★ Gut Knife | Scorched",
    "★ Gut Knife | Safari Mesh", "★ Gut Knife | Urban Masked",
    "★ Gut Knife | Night", "★ Gut Knife | Blue Steel",
    "★ Gut Knife | Stained", "★ Gut Knife | Case Hardened",
    "★ Gut Knife | Slaughter", "★ Gut Knife | Crimson Web",
    "★ Gut Knife | Fade", "★ Gut Knife | Boreal Forest",
    "★ Gut Knife",
    "★ Karambit | Forest DDPAT", "★ Karambit | Scorched",
    "★ Karambit | Safari Mesh", "★ Karambit | Urban Masked",
    "★ Karambit | Night", "★ Karambit | Blue Steel",
    "★ Karambit | Stained", "★ Karambit | Case Hardened",
    "★ Karambit | Slaughter", "★ Karambit | Crimson Web",
    "★ Karambit | Fade", "★ Karambit | Boreal Forest",
    "★ Karambit",
    "★ M9 Bayonet | Forest DDPAT", "★ M9 Bayonet | Scorched",
    "★ M9 Bayonet | Safari Mesh", "★ M9 Bayonet | Urban Masked",
    "★ M9 Bayonet | Night", "★ M9 Bayonet | Blue Steel",
    "★ M9 Bayonet | Stained", "★ M9 Bayonet | Case Hardened",
    "★ M9 Bayonet | Slaughter", "★ M9 Bayonet | Crimson Web",
    "★ M9 Bayonet | Fade", "★ M9 Bayonet | Boreal Forest",
    "★ M9 Bayonet"
]

BLUE = [
    "MP7 | Skulls",
    "AUG | Wings",
    "SG 553 | Ultraviolet"
]

PURPLE = [
    "M4A1-S | Dark Water",
    "Glock-18 | Dragon Tattoo",
    "USP-S | Dark Water"
]

PINK = [
    "AK-47 | Case Hardened",
    "Desert Eagle | Hypnotic"
]

RED = [
    "AWP | Lightning Strike",
    "AWP | Lightning Strike"
]

# item ids with buff167 ids
# TODO add ids for each wear
item_ids = {
    #default ultra
    "SG 553 | Ultraviolet": 36507,
    "SG 553 | Ultraviolet (Battle-Scarred)":36506,
    "SG 553 | Ultraviolet (Well-Worn)": 36510,
    "SG 553 | Ultraviolet (Field-Tested)": 36508,
    "SG 553 | Ultraviolet (Minimal Wear)": 36509,
    "SG 553 | Ultraviolet (Factory New)": 36507,
    "StatTrak™ SG 553 | Ultraviolet (Battle-Scarred)":39526,
    "StatTrak™ SG 553 | Ultraviolet (Factory New)": 39527,
    "StatTrak™ SG 553 | Ultraviolet (Field-Tested)": 39528,
    "StatTrak™ SG 553 | Ultraviolet (Minimal Wear)":39529,
    "StatTrak™ SG 553 | Ultraviolet (Well-Worn)":39530,

    #default wings
    "AUG | Wings": 34063,
    "AUG | Wings (Factory New)":34063,
    "AUG | Wings (Minimal Wear)":34064,
    "StatTrak™ AUG | Wings (Factory New)":38278,
    "StatTrak™ AUG | Wings (Minimal Wear)":38279,

    #default skulls
    "MP7 | Skulls": 35611,
    "MP7 | Skulls (Field-Tested)":35610,
    "MP7 | Skulls (Minimal Wear)":35611,
    "StatTrak™ MP7 | Skulls (Field-Tested)":39032,
    "StatTrak™ MP7 | Skulls (Minimal Wear)":39033,

    #default dark
    "USP-S | Dark Water": 42171,
    "USP-S | Dark Water (Field-Tested)":42170,
    "USP-S | Dark Water (Minimal Wear)":42171,
    "StatTrak™ USP-S | Dark Water (Field-Tested)":39733,
    "StatTrak™ USP-S | Dark Water (Minimal Wear)":39734,

    #glock 18
    "Glock-18 | Dragon Tattoo": 35018,
    "Glock-18 | Dragon Tattoo (Factory New)":35018,
    "Glock-18 | Dragon Tattoo (Minimal Wear)":35019,
    "StatTrak™ Glock-18 | Dragon Tattoo (Factory New)":38713,
    "StatTrak™ Glock-18 | Dragon Tattoo (Minimal Wear)":38714,

    #dark water
    "M4A1-S | Dark Water": 35195,
    "M4A1-S | Dark Water (Field-Tested)":35194,
    "M4A1-S | Dark Water (Minimal Wear)":35195,
    "StatTrak™ M4A1-S | Dark Water (Field-Tested)":38807,
    "StatTrak™ M4A1-S | Dark Water (Minimal Wear)":38808,

    #hypnotic
    "Desert Eagle | Hypnotic": 34428,
    "Desert Eagle | Hypnotic (Factory New)":34428,
    "Desert Eagle | Hypnotic (Minimal Wear)":34429,
    "StatTrak™ Desert Eagle | Hypnotic (Factory New)":38429,
    "StatTrak™ Desert Eagle | Hypnotic (Minimal Wear)":38430,

    #case harden
    "AK-47 | Case Hardened": 33881,
    "AK-47 | Case Hardened (Battle-Scarred)":33880,
    "AK-47 | Case Hardened (Factory New)":33881,
    "AK-47 | Case Hardened (Field-Tested)":33882,
    "AK-47 | Case Hardened (Minimal Wear)":33883,
    "AK-47 | Case Hardened (Well-Worn)":33884,
    "StatTrak™ AK-47 | Case Hardened (Factory New)":38171,
    "StatTrak™ AK-47 | Case Hardened (Field-Tested)":38172,
    "StatTrak™ AK-47 | Case Hardened (Minimal Wear)":38173,
    "StatTrak™ AK-47 | Case Hardened (Well-Worn)":38174,

    #awp
    "AWP | Lightning Strike": 34099,
    "AWP | Lightning Strike (Factory New)":34099,
    "AWP | Lightning Strike (Minimal Wear)":34100,
    "StatTrak™ AWP | Lightning Strike (Factory New)":38310,
    "StatTrak™ AWP | Lightning Strike (Minimal Wear)":38311,

    #TODO find automation for knifes
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