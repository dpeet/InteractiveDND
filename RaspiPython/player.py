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
##        self.skills = args[0]["skills"]
