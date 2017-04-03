class Player:
    def __init__(self, *args, **kwargs):
        ##    def __init__(self, name):
        ##        print(kwargs)
        ##        print(args[0])
        self.name = args[0]["name"]
        self.clss = args[0]["class"]
        self.background = args[0]["background"]
        self.race = args[0]["race"]
        self.alignment = args[0]["alignment"]
        self.playerName = args[0]["playername"]
        self.expPoints = args[0]["exp"]

        self.prof = args[0]["prof"]
        self.profStats = args[0]["prof_stats"]

        ## stats
        self.str = args[0]["str"]
        self.dex = args[0]["dex"]
        self.con = args[0]["con"]
        self.int = args[0]["int"]
        self.wis = args[0]["wis"]
        self.cha = args[0]["cha"]

        ## Equipments
        self.armorclass = args[0]["armor_class"]
        self.speed = args[0]["speed"]

        ##
        self.weapons = args[0]["weapons"]
        self.spells = args[0]["spells"]
        self.special = args[0]["special"]
        self.skills = args[0]["skills"]






##        dmgData = ["Slashing (cut)",
##                "Bludgeoning (smash)",
##                "Piercing (pierce)",
##                "Fire (burn)",
##                "Cold (Freeze)",
##                "Poison (Toxin)",
##                "Acid (Corrosion)",
##                "Psychic (Mental Durability)",
##                "Necrotic (Decay)",
##                "Lightning (Electrical)",
##                "Thunder (Sound)",
##                "Force (Force)"]
##
##        saData = ["Ability Score Loss",
##                "Alternate Form",
##                "Antimagic",
##                "Blindsight And Blindsense",
##                "Breath Weapon",
##                "Change Shape",
##                "Charm and Compulsion",
##                "Cold Immunity",
##                "Constrict",
##                "Damage Reduction",
##                "Darkvision",
##                "Death Attacks",
##                "Disease",
##                "Energy Drain And Negative Levels",
##                "Etherealness",
##                "Evasion And Improved Evasion",
##                "Fast Healing",
##                "Fear",
##                "Fire Immunity",
##                "Gaseous Form",
##                "Gaze Attacks",
##                "Improved Grab",
##                "Incorporeality",
##                "Invisibility",
##                "Level Loss",
##                "Low-Light Vision",
##                "Manufactured Weapons",
##                "Movement Modes",
##                "Natural Weapons",
##                "Nonabilities",
##                "Paralysis",
##                "Poison",
##                "Polymorph",
##                "Pounce",
##                "Powerful Charge",
##                "Psionics",5
##                "Rake",
##                "Rays",
##                "Regeneration",
##                "Resistance To Energy",
##                "Scent",
##                "Sonic Attacks",
##                "Spell Immunity",
##                "Spell Resistance",
##                "Spells",
##                "Summon",
##                "Swallow Whole",
##                "Telepathy",
##                "Trample",
##                "Tremorsense",
##                "Turn Resistance",
##                "Vulnerability to Energy"]
##
##        wpData = ["Club (B 1d4)",
##                "Dagger (P 1d4)",
##                "Greatclub (B 1d8)",
##                "Handaxe (S 1d6)",
##                "Javelin (P 1d6)",
##                "Light hammer (B 1d4)",
##                "Mace (B 1d6)",
##                "Quarterstaff (B 1d6)",
##                "Sickle (S 1d4)",
##                "Spear (P 1d6)",
##                "Unarmed strike (B 1)",
##                "Crossbow, light (P 1d8)",
##                "Dart (P 1d4)",
##                "Shortbow (P 1d6)",
##                "Sling (B 1d4)",
##                "Battleaxe (S 1d8)",
##                "Flail (B 1d8)",
##                "Glaive (S 1d10)",
##                "Greataxe (S 1d12)",
##                "Greatsword (S 2d6)",
##                "Halberd (S 1d10)",
##                "Lance (P 1d12)",
##                "Longsword (S 1d8)",
##                "Maul (B 2d6)",
##                "Morningstar (P 1d8)",
##                "Pike (P 1d10)",
##                "Rapier (P 1d8)",
##                "Scimitar (S 1d6)",
##                "Shortsword (P 1d6)",
##                "Trident (P 1d6)",
##                "War pick (P 1d8)",
##                "Warhammer (B 1d8)",
##                "Whip (S 1d4)",
##                "Blowgun (P 1)",
##                "Crossbow, hand (P 1d6)",
##                "Crossbow, heavy (P 1d10)",
##                "Longbow (P 1d8)",
##                "Net"]
##
##
##        wpData.sort()
