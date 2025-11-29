import math

ores = {
    "Stone Ore": {"rarity": "Common", "multiplier": 0.2, "traitType": None, "trait": None},
    "Sand Stone": {"rarity": "Common", "multiplier": 0.25, "traitType": None, "trait": None},
    "Copper Ore": {"rarity": "Common", "multiplier": 0.3, "traitType": None, "trait": None},
    "Iron Ore": {"rarity": "Common", "multiplier": 0.35, "traitType": None, "trait": None},
    "Tin Ore": {"rarity": "Uncommon", "multiplier": 0.425, "traitType": None, "trait": None},
    "Silver Ore": {"rarity": "Uncommon", "multiplier": 0.5, "traitType": None, "trait": None},
    "Gold Ore": {"rarity": "Uncommon", "multiplier": 0.65, "traitType": None, "trait": None},
    "Mushroomite Ore": {"rarity": "Rare", "multiplier": 0.8, "traitType": None, "trait": None},
    "Platinum Ore": {"rarity": "Rare", "multiplier": 0.8, "traitType": None, "trait": None},
    "Bananite Ore": {"rarity": "Uncommon", "multiplier": 0.85, "traitType": None, "trait": None},
    "Cardboardite Ore": {"rarity": "Common", "multiplier": 0.7, "traitType": None, "trait": None},
    "Aite Ore": {"rarity": "Epic", "multiplier": 1.0, "traitType": None, "trait": None},
    "Poopite Ore": {"rarity": "Epic", "multiplier": 1.2, "traitType": None, "trait": None},
    "Cobalt Ore": {"rarity": "Uncommon", "multiplier": 1.0, "traitType": None, "trait": None},
    "Titanium Ore": {"rarity": "Uncommon", "multiplier": 1.15, "traitType": None, "trait": None},
    "Lapis Lazuli Ore": {"rarity": "Uncommon", "multiplier": 1.3, "traitType": None, "trait": None},
    "Volcanic Rock": {"rarity": "Rare", "multiplier": 1.55, "traitType": None, "trait": None},
    "Quartz Ore": {"rarity": "Rare", "multiplier": 1.5, "traitType": None, "trait": None},
    "Amethyst Ore": {"rarity": "Rare", "multiplier": 1.65, "traitType": None, "trait": None},
    "Topaz Ore": {"rarity": "Rare", "multiplier": 1.75, "traitType": None, "trait": None},
    "Diamond Ore": {"rarity": "Rare", "multiplier": 2.0, "traitType": None, "trait": None},
    "Sapphire Ore": {"rarity": "Rare", "multiplier": 2.25, "traitType": None, "trait": None},
    "Cuprite Ore": {"rarity": "Epic", "multiplier": 2.43, "traitType": None, "trait": None},
    "Obsidian Ore": {"rarity": "Epic", "multiplier": 2.35, "traitType": "Armor", "trait": "30% Vitality"},
    "Emerald Ore": {"rarity": "Epic", "multiplier": 2.55, "traitType": None, "trait": None},
    "Ruby Ore": {"rarity": "Epic", "multiplier": 2.95, "traitType": None, "trait": None},
    "Rivalite Ore": {"rarity": "Epic", "multiplier": 3.33, "traitType": "Weapon", "trait": "+20% Critical Strike Chance on Weapons"},
    "Uranium Ore": {"rarity": "Legendary", "multiplier": 3.0, "traitType": "Armor", "trait": "5% Player Max HP as AOE Damage on Armor"},
    "Mythril Ore": {"rarity": "Legendary", "multiplier": 3.5, "traitType": "Armor", "trait": "1.5% > 8.25% > 15% Vtality"},
    "Eye Ore": {"rarity": "Legendary", "multiplier": 4.0, "traitType": "All", "trait": "-10% Health, +15% Damage"},
    "Fireite Ore": {"rarity": "Legendary", "multiplier": 4.5, "traitType": "Weapon", "trait": "20% Burn for 2 Seconds with 30% On-Hit Chance"},
    "Magmaite Ore": {"rarity": "Legendary", "multiplier": 5.0, "traitType": "Weapon", "trait": "50% AOE Explosion Damage with 35% On-Hit Chance"},
    "Lightite Ore": {"rarity": "Legendary", "multiplier": 4.6, "traitType": "Armor", "trait": "1-10% Move Speed Bonus"},
    "Demonite Ore": {"rarity": "Mythical", "multiplier": 5.5, "traitType": "Armor", "trait": "20% Burn for 2 Seconds with 15% On-Ht Chance & Demon's Backfire Passive."},
    "Darkryte Ore": {"rarity": "Mythical", "multiplier": 6.3, "traitType": "Armor", "trait": "Shadow's Phantom Step Passive (15% Chance to Negate Damage)"},
    "Magenta Crystal Ore": {"rarity": "Epic", "multiplier": 3.1, "traitType": None, "trait": None},
    "Crimson Crystal Ore": {"rarity": "Epic", "multiplier": 3.3, "traitType": None, "trait": None},
    "Green Crystal Ore": {"rarity": "Epic", "multiplier": 3.2, "traitType": None, "trait": None},
    "Orange Crystal Ore": {"rarity": "Epic", "multiplier": 3.0, "traitType": None, "trait": None},
    "Blue Crystal Ore": {"rarity": "Epic", "multiplier": 3.4, "traitType": None, "trait": None},
    "Rainbow Crystal Ore": {"rarity": "Legendary", "multiplier": 5.25, "traitType": None, "trait": None},
    "Arcane Crystal Ore": {"rarity": "Epic", "multiplier": 7.5, "traitType": None, "trait": None},
    "Galaxite Ore": {"rarity": "Divine", "multiplier": 11.5, "traitType": None, "trait": None},
    "Vooite Ore": {"rarity": None, "multiplier": 0.0, "traitType": None, "trait": None}
}

#Weapon Types:
    #Dagger
    #Straight Sword
    #Gauntlets
    #Katana
    #Great Sword
    #Great Axe
    #Colossal Sword

    #Beyond 55 Materials Values Skew, every 5 or so makes Colossal a Single % more likely.

weaponOdds = {
    3: {"Dagger": 1.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.00, "Great Axe": 0.00, "Colossal Sword": 0.00},
    4: {"Dagger": 0.86, "Straight Sword": 0.14, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.00, "Great Axe": 0.00, "Colossal Sword": 0.00},
    5: {"Dagger": 0.35, "Straight Sword": 0.65, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.00, "Great Axe": 0.00, "Colossal Sword": 0.00},
    6: {"Dagger": 0.14, "Straight Sword": 0.86, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.00, "Great Axe": 0.00, "Colossal Sword": 0.00},
    7: {"Dagger": 0.06, "Straight Sword": 0.74, "Gauntlet": 0.20, "Katana": 0.00, "Great Sword": 0.00, "Great Axe": 0.00, "Colossal Sword": 0.00},
    8: {"Dagger": 0.02, "Straight Sword": 0.44, "Gauntlet": 0.54, "Katana": 0.00, "Great Sword": 0.00, "Great Axe": 0.00, "Colossal Sword": 0.00},
    9: {"Dagger": 0.01, "Straight Sword": 0.24, "Gauntlet": 0.65, "Katana": 0.00, "Great Sword": 0.00, "Great Axe": 0.00, "Colossal Sword": 0.00},
    10: {"Dagger": 0.00, "Straight Sword": 0.11, "Gauntlet": 0.47, "Katana": 0.42, "Great Sword": 0.00, "Great Axe": 0.00, "Colossal Sword": 0.00},
    11: {"Dagger": 0.00, "Straight Sword": 0.05, "Gauntlet": 0.32, "Katana": 0.63, "Great Sword": 0.00, "Great Axe": 0.00, "Colossal Sword": 0.00},
    12: {"Dagger": 0.00, "Straight Sword": 0.03, "Gauntlet": 0.22, "Katana": 0.72, "Great Sword": 0.00, "Great Axe": 0.00, "Colossal Sword": 0.00},
    13: {"Dagger": 0.00, "Straight Sword": 0.01, "Gauntlet": 0.14, "Katana": 0.62, "Great Sword": 0.22, "Great Axe": 0.00, "Colossal Sword": 0.00},
    14: {"Dagger": 0.00, "Straight Sword": 0.01, "Gauntlet": 0.08, "Katana": 0.46, "Great Sword": 0.45, "Great Axe": 0.00, "Colossal Sword": 0.00},
    15: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.05, "Katana": 0.34, "Great Sword": 0.60, "Great Axe": 0.00, "Colossal Sword": 0.00},
    16: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.03, "Katana": 0.26, "Great Sword": 0.69, "Great Axe": 0.01, "Colossal Sword": 0.00},
    17: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.02, "Katana": 0.19, "Great Sword": 0.68, "Great Axe": 0.11, "Colossal Sword": 0.00},
    18: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.01, "Katana": 0.13, "Great Sword": 0.57, "Great Axe": 0.28, "Colossal Sword": 0.00},
    19: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.01, "Katana": 0.09, "Great Sword": 0.46, "Great Axe": 0.45, "Colossal Sword": 0.00},
    20: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.01, "Katana": 0.06, "Great Sword": 0.36, "Great Axe": 0.57, "Colossal Sword": 0.00},
    21: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.04, "Great Sword": 0.29, "Great Axe": 0.65, "Colossal Sword": 0.02},
    22: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.03, "Great Sword": 0.23, "Great Axe": 0.67, "Colossal Sword": 0.07},
    23: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.02, "Great Sword": 0.18, "Great Axe": 0.66, "Colossal Sword": 0.13},
    24: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.02, "Great Sword": 0.15, "Great Axe": 0.64, "Colossal Sword": 0.20},
    25: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.01, "Great Sword": 0.12, "Great Axe": 0.60, "Colossal Sword": 0.26},
    26: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.01, "Great Sword": 0.10, "Great Axe": 0.56, "Colossal Sword": 0.32},
    27: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.01, "Great Sword": 0.09, "Great Axe": 0.53, "Colossal Sword": 0.37},
    28: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.01, "Great Sword": 0.07, "Great Axe": 0.50, "Colossal Sword": 0.42},
    29: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.01, "Great Sword": 0.07, "Great Axe": 0.47, "Colossal Sword": 0.46},
    30: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.01, "Great Sword": 0.06, "Great Axe": 0.45, "Colossal Sword": 0.49},
    31: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.05, "Great Axe": 0.43, "Colossal Sword": 0.51},
    32: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.05, "Great Axe": 0.41, "Colossal Sword": 0.54},
    33: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.04, "Great Axe": 0.39, "Colossal Sword": 0.56},
    34: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.04, "Great Axe": 0.38, "Colossal Sword": 0.58},
    35: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.04, "Great Axe": 0.37, "Colossal Sword": 0.59},
    36: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.03, "Great Axe": 0.36, "Colossal Sword": 0.61},
    37: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.03, "Great Axe": 0.35, "Colossal Sword": 0.62},
    38: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.03, "Great Axe": 0.34, "Colossal Sword": 0.63},
    39: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.03, "Great Axe": 0.33, "Colossal Sword": 0.64},
    40: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.03, "Great Axe": 0.32, "Colossal Sword": 0.65},
    41: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.03, "Great Axe": 0.32, "Colossal Sword": 0.65},
    42: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.03, "Great Axe": 0.31, "Colossal Sword": 0.66},
    43: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.02, "Great Axe": 0.31, "Colossal Sword": 0.67},
    44: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.02, "Great Axe": 0.30, "Colossal Sword": 0.67},
    45: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.02, "Great Axe": 0.30, "Colossal Sword": 0.68},
    46: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.02, "Great Axe": 0.29, "Colossal Sword": 0.69},
    47: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.02, "Great Axe": 0.29, "Colossal Sword": 0.69},
    48: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.02, "Great Axe": 0.28, "Colossal Sword": 0.69},
    49: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.02, "Great Axe": 0.28, "Colossal Sword": 0.70},
    50: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.02, "Great Axe": 0.28, "Colossal Sword": 0.70},
    51: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.02, "Great Axe": 0.27, "Colossal Sword": 0.71},
    52: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.02, "Great Axe": 0.27, "Colossal Sword": 0.71},
    53: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.02, "Great Axe": 0.27, "Colossal Sword": 0.71},
    54: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.01, "Great Axe": 0.27, "Colossal Sword": 0.72},
    55: {"Dagger": 0.00, "Straight Sword": 0.00, "Gauntlet": 0.00, "Katana": 0.00, "Great Sword": 0.01, "Great Axe": 0.26, "Colossal Sword": 0.73},
}

# Armor Types:
    #Light Helmet
    #Light Chest
    #Light Leggings

    #Medium Helmet
    #Medium Chest
    #Medium Leggings
armorOdds = {
    3: {"Light Helmet": 1.00, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    4: {"Light Helmet": 1.00, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    5: {"Light Helmet": 0.89, "Light Leggings": 0.11, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    6: {"Light Helmet": 0.56, "Light Leggings": 0.44, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    7: {"Light Helmet": 0.32, "Light Leggings": 0.67, "Light Chestplate": 0.01, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    8: {"Light Helmet": 0.17, "Light Leggings": 0.17, "Light Chestplate": 0.17, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    9: {"Light Helmet": 0.08, "Light Leggings": 0.51, "Light Chestplate": 0.41, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    10: {"Light Helmet": 0.04, "Light Leggings": 0.34, "Light Chestplate": 0.53, "Medium Helmet": 0.04, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    11: {"Light Helmet": 0.02, "Light Leggings": 0.20, "Light Chestplate": 0.47, "Medium Helmet": 0.31, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    12: {"Light Helmet": 0.01, "Light Leggings": 0.12, "Light Chestplate": 0.37, "Medium Helmet": 0.50, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    13: {"Light Helmet": 0, "Light Leggings": 0.04, "Light Chestplate": 0.28, "Medium Helmet": 0.60, "Medium Leggings": 0.04, "Medium Chestplate": 0, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    14: {"Light Helmet": 0, "Light Leggings": 0.04, "Light Chestplate": 0.19, "Medium Helmet": 0.55, "Medium Leggings": 0.22, "Medium Chestplate": 0, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    15: {"Light Helmet": 0, "Light Leggings": 0.02, "Light Chestplate": 0.12, "Medium Helmet": 0.43, "Medium Leggings": 0.43, "Medium Chestplate": 0, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    16: {"Light Helmet": 0, "Light Leggings": 0.01, "Light Chestplate": 0.08, "Medium Helmet": 0.32, "Medium Leggings": 0.57, "Medium Chestplate": 0.08, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    17: {"Light Helmet": 0, "Light Leggings": 0.01, "Light Chestplate": 0.05, "Medium Helmet": 0.22, "Medium Leggings": 0.57, "Medium Chestplate": 0.16, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    18: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0.03, "Medium Helmet": 0.14, "Medium Leggings": 0.48, "Medium Chestplate": 0.35, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    19: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0.02, "Medium Helmet": 0.09, "Medium Leggings": 0.39, "Medium Chestplate": 0.50, "Heavy Helmet": 0, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    20: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0.01, "Medium Helmet": 0.06, "Medium Leggings": 0.32, "Medium Chestplate": 0.60, "Heavy Helmet": 0.01, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    21: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0.01, "Medium Helmet": 0.07, "Medium Leggings": 0.25, "Medium Chestplate": 0.63, "Heavy Helmet": 0.07, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    22: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0.03, "Medium Leggings": 0.19, "Medium Chestplate": 0.59, "Heavy Helmet": 0.19, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    23: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0.02, "Medium Leggings": 0.14, "Medium Chestplate": 0.52, "Heavy Helmet": 0.32, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    24: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0.01, "Medium Leggings": 0.10, "Medium Chestplate": 0.44, "Heavy Helmet": 0.44, "Heavy Leggings": 0, "Heavy Chestplate": 0},
    25: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0.07, "Medium Chestplate": 0.36, "Heavy Helmet": 0.51, "Heavy Leggings": 0.05, "Heavy Chestplate": 0},
    26: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0.05, "Medium Chestplate": 0.28, "Heavy Helmet": 0.51, "Heavy Leggings": 0.15, "Heavy Chestplate": 0},
    27: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0.04, "Medium Chestplate": 0.21, "Heavy Helmet": 0.47, "Heavy Leggings": 0.28, "Heavy Chestplate": 0.21},
    28: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0.03, "Medium Chestplate": 0.16, "Heavy Helmet": 0.42, "Heavy Leggings": 0.39, "Heavy Chestplate": 0},
    29: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0.02, "Medium Chestplate": 0.11, "Heavy Helmet": 0.35, "Heavy Leggings": 0.47, "Heavy Chestplate": 0.04},
    30: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0.01, "Medium Chestplate": 0.08, "Heavy Helmet": 0.28, "Heavy Leggings": 0.49, "Heavy Chestplate": 0.13},
    31: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0.01, "Medium Chestplate": 0.06, "Heavy Helmet": 0.22, "Heavy Leggings": 0.46, "Heavy Chestplate": 0.25},
    32: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0.01, "Medium Chestplate": 0.04, "Heavy Helmet": 0.17, "Heavy Leggings": 0.42, "Heavy Chestplate": 0.37},
    33: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0.03, "Heavy Helmet": 0.13, "Heavy Leggings": 0.37, "Heavy Chestplate": 0.47},
    34: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0.02, "Heavy Helmet": 0.10, "Heavy Leggings": 0.33, "Heavy Chestplate": 0.54},
    35: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0.02, "Heavy Helmet": 0.08, "Heavy Leggings": 0.30, "Heavy Chestplate": 0.60},
    36: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0.01, "Heavy Helmet": 0.07, "Heavy Leggings": 0.27, "Heavy Chestplate": 0.64},
    37: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0.01, "Heavy Helmet": 0.06, "Heavy Leggings": 0.25, "Heavy Chestplate": 0.68},
    38: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0.01, "Heavy Helmet": 0.05, "Heavy Leggings": 0.23, "Heavy Chestplate": 0.71},
    39: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0.01, "Heavy Helmet": 0.04, "Heavy Leggings": 0.22, "Heavy Chestplate": 0.73},
    40: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0.01, "Heavy Helmet": 0.04, "Heavy Leggings": 0.20, "Heavy Chestplate": 0.75},
    41: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0.01, "Heavy Helmet": 0.04, "Heavy Leggings": 0.19, "Heavy Chestplate": 0.77},
    42: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0.03, "Heavy Leggings": 0.18, "Heavy Chestplate": 0.78},
    43: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0.03, "Heavy Leggings": 0.17, "Heavy Chestplate": 0.79},
    44: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0.03, "Heavy Leggings": 0.17, "Heavy Chestplate": 0.80},
    45: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0.03, "Heavy Leggings": 0.16, "Heavy Chestplate": 0.81},
    46: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0.02, "Heavy Leggings": 0.16, "Heavy Chestplate": 0.82},
    47: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0.02, "Heavy Leggings": 0.15, "Heavy Chestplate": 0.82},
    48: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0.02, "Heavy Leggings": 0.15, "Heavy Chestplate": 0.83},
    49: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0.02, "Heavy Leggings": 0.14, "Heavy Chestplate": 0.83},
    50: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0.02, "Heavy Leggings": 0.14, "Heavy Chestplate": 0.84},
    51: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0.02, "Heavy Leggings": 0.14, "Heavy Chestplate": 0.84},
    52: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0.02, "Heavy Leggings": 0.13, "Heavy Chestplate": 0.85},
    53: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0.02, "Heavy Leggings": 0.13, "Heavy Chestplate": 0.85},
    54: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0.02, "Heavy Leggings": 0.13, "Heavy Chestplate": 0.85},
    55: {"Light Helmet": 0, "Light Leggings": 0, "Light Chestplate": 0, "Medium Helmet": 0, "Medium Leggings": 0, "Medium Chestplate": 0, "Heavy Helmet": 0.02, "Heavy Leggings": 0.12, "Heavy Chestplate": 0.86},
}

def calculate_combined_multiplier(selected_ores, ores_dict):
    """
    Calculate the combined multiplier of a selection of ores.

    Parameters:
    - selected_ores: dict of ore_name -> count
        Example: {"Eye Ore": 2, "Lightite Ore": 1}
    - ores_dict: dictionary of ores with multiplier info

    Returns:
    - float: combined multiplier
    """
    total_multiplier = 0
    total_count = 0

    for ore_name, count in selected_ores.items():
        if ore_name not in ores_dict:
            print(f"Warning: {ore_name} not found in ores dictionary.")
            continue
        multiplier = ores_dict[ore_name]["multiplier"]
        total_multiplier += multiplier * count
        total_count += count

    if total_count == 0:
        return 0  # avoid division by zero

    return total_multiplier / total_count


def get_item_chances_with_traits(selected_ores, ores_dict, craft_type="Weapon"):
    """
    Calculate combined multiplier, total count, composition, odds, traits, and rarity.
    Automatically selects weaponOdds or armorOdds based on craft_type.
    """

    # Auto-select correct odds table
    if craft_type == "Weapon":
        odds_dict = weaponOdds
    else:
        odds_dict = armorOdds

    # Step 1: Combined multiplier
    combined_multiplier = calculate_combined_multiplier(selected_ores, ores_dict)

    # Step 2: Total ore count
    total_count = sum(selected_ores.values())

    MAX_ODDS_ORE_COUNT = 55

    # Cap odds at 55
    if total_count > MAX_ODDS_ORE_COUNT:
        print("This is not recommended, 55 Ores should be the most you add.")
        odds_key = MAX_ODDS_ORE_COUNT
    else:
        odds_key = total_count

    # Step 3: Composition %
    composition = {ore: (count / total_count * 100) for ore, count in selected_ores.items()}

    # Step 4: Trait transfer rules
    traits = []
    for ore, pct in composition.items():
        ore_data = ores_dict.get(ore, {})
        trait = ore_data.get("trait", None)
        trait_type = ore_data.get("traitType", "All")

        if pct >= 10 and trait and (trait_type == craft_type or trait_type == "All"):
            traits.append(trait)

    # Step 5: Get correct odds for armor or weapon
    if odds_key not in odds_dict:
        odds_key = max(odds_dict.keys())

    odds = odds_dict[odds_key]

    # Step 6: Sort filtered odds
    filtered_odds = {k: v for k, v in odds.items() if v > 0}
    sorted_odds = dict(sorted(filtered_odds.items(), key=lambda x: x[1], reverse=True))

    # Step 7: Craft rarity
    if composition:
        highest = max(composition.items(), key=lambda x: x[1])[0]
        rarity = ores_dict.get(highest, {}).get("rarity", "Unknown")
    else:
        rarity = "Unknown"

    return {
        "combined_multiplier": combined_multiplier,
        "total_count": total_count,
        "composition": composition,
        "odds": sorted_odds,
        "traits": traits if traits else ["No traits transfer"],
        "rarity": rarity
    }


selected = {
    "Eye Ore" : 7,
    "Mythril Ore" : 6,
    "Obsidian Ore" : 6,
    "Uranium Ore" : 6
}  

# Choose craft type here:
craft_type = "Weapon"  # or "Armor"

result = get_item_chances_with_traits(selected, ores, craft_type)


print("Craft Results:")
print(f"Rarity: {result['rarity']}") 
print(f"Combined multiplier: {result['combined_multiplier']:.2f}")
print("Composition of selected ores:")
for ore, pct in result['composition'].items():
    print(f"  {ore}: {pct:.1f}%")
print("Chances by type:")
for key, chance in result["odds"].items():
    print(f"  {key}: {chance*100:.1f}%")
print("Traits triggered:")
for trait in result["traits"]:
    print(f"  {trait}")

