from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.uix.label import Label
from kivy.adapters.listadapter import ListAdapter
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListItemButton, ListView
from kivy.lang import Builder
import random
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from player import Player
from countdice2 import get_num_from_dice, test_get_num_from_dice
import json
from pprint import pprint
from kivy.core.window import Window

from kivy.config import Config

Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '800')



##Builder.load_string("""
##<ButtonsApp>:
##    orientation: "vertical"
##    Button:
##            id: wpButton
##            Image:
##                source: "./images/weapon.png"
##                center_x: self.parent.center_x
##                center_y: setlf.parent.center_y
##    Label:
##        text: "A label"
##""")

root = Builder.load_string('''
<RootWidget>:
    canvas.before:
##        AsyncImage:
##            source: './images/initiative.png'
##            size_hint: 1, .5
##            pos_hint: {'center_x':.5, 'center_y': .5}
        Rectangle:
            # self here refers to the widget i.e FloatLayout
            pos: self.pos
            size: self.size
            source: "./images/4.png"
''')

currentPlayer = None
currentPage = None ## 1=init , 2=saving throw , 3=weapons , 4=skills , 5=spells , 6=special ability
pageNum = 0

class RootWidget(FloatLayout):


    Window.size = (480, 800)
    def callback2(instance):
        print('The button <%s> is being pressed' % instance.text)



    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        fp_list = list()
        sp_list = list()
        tp_list = list()
        f2p_list = list()
        f3p_list = list()
        zp_list = list()
        playerList = list()
        playerNames = list()
        initData = list()
        dmgData = list()
        saData = list()
        wpData = list()
        skData = list()
        stData = list()
        playerDic = dict()
        initFlag = False


        ##################### Importing Player data Json File ######################
        with open('player.json') as data_file:
            data = json.load(data_file)

        for item in data:
            playerList.append(Player(item))

        for item in playerList:
            playerNames.append(item.playerName)
            initData.append(("%s  =     0" %item.playerName))
            playerDic[item.playerName] = item
            print(item.weapons)


        if len(playerNames) > 1:
            global currentPlayer
            currentPlayer = playerDic[playerNames[0]]


        ############################################################################

        global pageNum
        pageNum = 1
        setting = 0 ## 0 = no preference
                    ## 1 = manual calculation
                    ## 2 = automatic calculation

        KIVY_FONTS = [
                        {
                            "name": "custom",
                            "fn_regular": "data/fonts/RobotoCondensed-Light.ttf",
                            "fn_bold": "data/fonts/RobotoCondensed-Regular.ttf",
                            "fn_italic": "data/fonts/RobotoCondensed-LightItalic.ttf",
                            "fn_bolditalic": "data/fonts/RobotoCondensed-Italic.ttf"
                        }]
        ## init add dex

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
##                "Psionics",
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
##
        skData = ["Acrobatics (Dex)",
                "Animal Handling (Wis)",
                "Arcana (Int)",
                "Athletics (Str)",
                "Deception (Cha)",
                "History (Int)",
                "Insight (Wis)",
                "Intimidation (Cha)",
                "Investigation (Int)",
                "Medicine (Wis)",
                "Nature (Int)",
                "Perception (Wis)",
                "Performance (Cha)",
                "Persuasion (Cha)",
                "Religion (Int)",
                "Sleight of Hand (Dex)",
                "Stealth (Dex)",
                "Survival (Wise)"]
##
        stData = ["Strength",
                "Dexterity",
                "Constitution",
                "Intelligence",
                "Wisdom",
                "Charisma"]

##        initData = ["Tie Roll (1d20)"]

##        initData = playerNames
##        initData.sort()

        numData = ["1", "2", "3", "4", "5", "6"]

        diceData = ["d4", "d6", "d8", "d10", "d12", "d20"]



################################# First page widgets! ##############################################################################

        def backPage(instance):
            global die
            global selected1
            global pageNum
            global currentSetting
            print("clicked")
            if pageNum == 2:
                for item in sp_list:
                    self.remove_widget(item)

                for item2 in fp_list:
                    self.add_widget(item2)

                die = 0
                pageNum = 1
                dLabel.text = ('Select your Die!')
##                changePageNum(1)
##                pageNum = 1
            elif pageNum == 3:
                for item in tp_list:
                    self.remove_widget(item)

                for item2 in sp_list:
                    self.add_widget(item2)
                pageNum = 2
##                changePageNum(2)
##                print("herewego")
##                pageNum = 2
            elif pageNum == 4:
                for item in f2p_list:
                    self.remove_widget(item)
                for item in f3p_list:
                    self.remove_widget(item)

                for item2 in tp_list:
                    self.add_widget(item2)
                pageNum = 3
##                changePageNum(3)

        def diceSelection(instance):
            global die
            global selected1
            global pageNum

            if instance == manualDiceButton:
                print("%d page is selected" % pageNum)
                print("%d option is selected" % die)
                print(selected1)
                for item in tp_list:
                    self.remove_widget(item)

                for item2 in f3p_list:
                    self.add_widget(item2)

                pageNum = 4
##                changePageNum(4)

            elif instance == autoDiceButton:
                print("%d page2 is selected" % pageNum)
                print("%d option is selected" % die)
                totalValLabel.text = ("%s rolled  %s !!!" % (spinner.text, str(sum(test_get_num_from_dice()))))
                print("here")
                print(selected1)
                for item in tp_list:
                    self.remove_widget(item)

                for item2 in f2p_list:
                    self.add_widget(item2)

                pageNum = 4
##                changePageNum(4)

        def changePageNum(num):
            global pageNum
            pageNum = num

##        def autoSelection(instance):
##            global currentPlayer
##            lh = ""
##            rh = ""
##            if instance == oneButton:
##                lh = instance.text
##            elif instance == twoButton:
##                lh = instance.text
##            elif instance == threeButton:
##                lh = instance.text
##            elif instance == fourButton:
##                lh = instance.text
##            elif instance == fiveButton:
##                lh = instance.text
##            elif instance == d4Button:
##                rh = instance.text
##            elif instance == d6Button:
##                rh = instance.text
##            elif instance == d8Button:
##                rh = instance.text
##            elif instance == d10Button:
##                rh = instance.text
##            elif instance == d12Button:
##                rh = instance.text
##            elif instance == d20Button:
##                rh = instance.text
##            elif instance == cal2Button:
##                mylist = totalLabel.text.split(" ")
##                if mylist[0] != "?" and mylist[2] != "?":
####                    totalValLabel.text = str(random.randint(int(mylist[0]), int(mylist[0]) * int(mylist[2])))
####                    print(test_get_num_from_dice())
####                    totalValLabel.text = str(sum(test_get_num_from_dice()))
##                    print("here")
##                    ## call the openCV file
##
##            if lh:
##                lhs, rhs = totalLabel.text.split(" ", 1)
##                totalLabel.text = "%s %s" % (lh, rhs)
##            elif rh:
##                lhs, rhs = totalLabel.text.split(" ", 1)
##                totalLabel.text = "%s %s to Roll" % (lhs, rh)

        def manualSelection(instance):
            if instance == clearButton:
                totalManLabel.text = "The total value = 0"
            else:
                num = int(instance.text)
                mylist = totalManLabel.text.split(" ")
                num2 = int(mylist[len(mylist)-1])
                num2 = num2 + num
                totalManLabel.text = ("The total Value = %d" % num2)




        def dieSelect(instance):
            global die
            global selected1
            global pageNum
            global initFlag
            global currentPage
##            global currentPlayer
            flag = True

            if instance == initButton:
                dLabel.text = ('%s is selected!' % instance.text)
                data = [{'text': i, 'is_selected': False} for i in initData]
                sLabel2.text = '0'
                sLabel.text = '0'
                initFlag = True
                currentPage = 1
                die = 1
            elif instance == stButton:
                dLabel.text = ('%s is selected!' % instance.text)
                
                sLabel2.text = '0'
                sLabel.text = '0'
##                stData = playerDic[currentPlayer.playerName].weapons
##                for  item in stData:
##                    print(item)
                data = [{'text': i, 'is_selected': False} for i in stData]
                initFlag = False
                currentPage = 2
                die = 2
            elif instance == wpButton:
                dLabel.text = ('%s is selected!' % instance.text)
                print(currentPlayer.playerName)
                print(playerDic[currentPlayer.playerName].weapons)
                wpData = []
                for item in playerDic[currentPlayer.playerName].weapons:
                    wpData.append(item[0])
##                wpData = playerDic[currentPlayer.playerName].weapons
                data = [{'text': i, 'is_selected': False} for i in wpData]
                sLabel2.text = '0'
                sLabel.text = '0'
                initFlag = False
                currentPage = 3
                die = 3
            elif instance == skButton:
                dLabel.text = ('%s is selected!' % instance.text)
##                skData = playerDic[currentPlayer.playerName].skills
                data = [{'text': i, 'is_selected': False} for i in skData]
                sLabel2.text = '0'
                sLabel.text = '0'
                initFlag = False
                currentPage = 4
                die = 4
            elif instance == spButton:
                dLabel.text = ('%s is selected!' % instance.text)
                print(currentPlayer.playerName)
                print(playerDic[currentPlayer.playerName].spells)
                spData = playerDic[currentPlayer.playerName].spells
                data = [{'text': i, 'is_selected': False} for i in spData]
                sLabel2.text = '0'
                sLabel.text = '0'
                initFlag = False
                currentPage = 5
                die = 5
            elif instance == saButton:
                dLabel.text = ('%s is selected!' % instance.text)
                saData = playerDic[currentPlayer.playerName].special
                data = [{'text': i, 'is_selected': False} for i in saData]
                sLabel2.text = '0'
                sLabel.text = '0'
                initFlag = False
                currentPage = 6
                die = 6
            elif instance == manualButton:
                flag = False
                selected1 = list_adapter.selection
                if not selected1:
                    sLabel.text = "Select One!"
                    sLabel.color = (1,0,0,1)
                else:
                    if initFlag:
                        selectedItem = list_adapter.selection[0].text
                        sLabel.color = (0,0,0,1)
                        sLabel.text = selectedItem
##                        str(sum(test_get_num_from_dice()))
##                        ran = random.randint(1, 100)
##                        sLabel2.text = ('Value: %d' % ran)

                        print("here %d" % pageNum)
                    else:
                        selectedItem = list_adapter.selection[0].text
                        sLabel.color = (0,0,0,1)
                        sLabel.text = selectedItem
                        ran = random.randint(1, 100)
                        sLabel2.text = ('Value: %d' % ran)

##                        for item in sp_list:
##                            self.remove_widget(item)
##
##                        for item2 in tp_list:
##                            self.add_widget(item2)
##                        changePageNum(3)
                        print("here %d" % pageNum)

            elif instance == autoButton:
                flag = False
                selected1 = list_adapter.selection
                if not selected1:
                    sLabel.text = "Select One!"
                    sLabel.color = (1,0,0,1)
                else:
                    if initFlag:
                        selectedItem = list_adapter.selection[0].text
                        sLabel.color = (0,0,0,1)
                        sLabel.text = selectedItem
##                        str(sum(test_get_num_from_dice()))
##                        ran = random.randint(1, 100)
##                        sLabel2.text = ('Value: %d' % ran)

                        print("here %d" % pageNum)
                    else:
                        selectedItem = list_adapter.selection[0].text
                        sLabel.color = (0,0,0,1)
                        
                        sLabel.text = str(sum(test_get_num_from_dice())+int(sLabel3.text))

                        
                        ran = random.randint(1, 100)
                        sLabel2.text = ('Value: %d' % ran)

                        print("here %d" % pageNum)
            elif instance == autoButton2:
                flag = False
                selected1 = list_adapter.selection
                if not selected1:
                    sLabel.text = "Select One!"
                    sLabel.color = (1,0,0,1)
                else:
                    if initFlag:
                        selectedItem = list_adapter.selection[0].text
                        sLabel.color = (0,0,0,1)
                        sLabel.text = selectedItem
##                        str(sum(test_get_num_from_dice()))
##                        ran = random.randint(1, 100)
##                        sLabel2.text = ('Value: %d' % ran)

                        print("here %d" % pageNum)
                    else:
                        selectedItem = list_adapter.selection[0].text
                        sLabel.color = (0,0,0,1)
                        
                        sLabel.text = str(sum(test_get_num_from_dice())+int(sLabel3.text))

                        
                        ran = random.randint(1, 100)
                        sLabel2.text = ('Value: %d' % ran)



            elif instance == nxtButton:
                print('%d is current die' % die)
            else:
                print('what is this?')

            if flag :
                list_adapter.data = data
                list_view.populate()

                for item in fp_list:
                    self.remove_widget(item)

                for item2 in sp_list:
                    self.add_widget(item2)
                changePageNum(2)

        def show_selected_value(spinner, text):
            global currentPlayer
            currentPlayer = playerDic[text]
            print(pageNum)
            if pageNum == 2:
##                if currentPage == 1:
##                    data = [{'text': i, 'is_selected': False} for i in initData]

##                elif currentPage == 2:
##                    data = [{'text': i, 'is_selected': False} for i in stData]

                if currentPage == 3:
                    wpData = []
                    for item in playerDic[currentPlayer.playerName].weapons:
                        wpData.append(item[0])
                    data = [{'text': i, 'is_selected': False} for i in wpData]

##                elif currentPage == 4:
##                    data = [{'text': i, 'is_selected': False} for i in skData]

                elif currentPage == 5:
                    spData = currentPlayer.spells
                    data = [{'text': i, 'is_selected': False} for i in spData]

                elif currentPage == 6:
                    saData = currentPlayer.special
##                    print(saData)
                    data = [{'text': i, 'is_selected': False} for i in saData]
                print(currentPage)
                list_adapter.data = data
                list_view.populate()

        def listSelected (instance):
            if len(list_adapter.selection) > 0:
                selectedItem = list_adapter.selection[0].text
                if currentPage == 3:
                    for item in currentPlayer.weapons:
                        if item[0] == selectedItem:
                            print(item[1])
                            print(item[2])
                            sLabel3.text = item[1]
                            sLabel4.text = item[2]


##
################################### 0 page widgets! ########################################################################################
##
##        dataPlayer = [{'text': i, 'is_selected': False} for i in wpData]
##
##        args_converter2 = lambda row_index, rec: {'text': rec['text'],
##                                                 'size_hint_x': 10,
##                                                 'size_hint_y': None,
##                                                 'selected_color': (1,0,0,1),
##                                                 'deselected_color': (0,0,0,1),
##                                                 'height': 45}
##
##        list_adapter2 = ListAdapter(data=dataPlayer,
##                                    args_converter=args_converter2,
##                                    cls=ListItemButton,
##                                    selection_mode='single',
##                                    allow_empty_selection=True)
##
##
##        list_view2 = ListView(adapter = list_adapter2,
##                             pos_hint = {'center_x': .3, 'center_y': .43},
##                             size_hint = (0.4, 0.6))
##        list_view2.background_normal = (0,0,0,1)

################################# 0 page widgets! ########################################################################################


        spinner = Spinner(
                        # default value shown
                        text=currentPlayer.playerName,
                        # available values
                        values=playerNames,
                        # just for positioning in our example
                        size_hint=(.1, 0.1),
##                        size=(100, 44),
                        pos_hint={'center_x': .93, 'center_y': .93})
        spinner.bind(text=show_selected_value)
        self.add_widget(spinner)
################################# First page widgets! ####################################################################################
        num = 480/800
        defNum = .3
        num2 = 225/250
        num3 = 250/225
##        wx = 480
##        wy = 800
##        bx = 225
##        by = 250
##        defX = wx *by
##        defY = wy *bx
        
        initButton = Button(
            size_hint=(defNum*num2, defNum*num),
            background_normal="./images/button_init.png",
            pos_hint={'center_x': .20, 'center_y': .6})

        initButton.bind(on_press=dieSelect)

        stButton = Button(
            size_hint=(defNum*num2, defNum*num),
            # height=50, width=50,
            background_normal="./images/button_saving_throw.png",
            pos_hint={'center_x': .5, 'center_y': .6})

        stButton.bind(on_press=dieSelect)

        wpButton = Button(
            size_hint=(defNum*num2, defNum*num),
##            size= (0.1, .1),
            background_normal="./images/button_weapons.png",
            pos_hint={'center_x': .8, 'center_y': .6})

        wpButton.bind(on_press=dieSelect)

        skButton = Button(
            size_hint=(defNum*num2, defNum*num),
            background_normal="./images/button_skills.png",
            pos_hint={'center_x': .2, 'center_y': .30})

        skButton.bind(on_press=dieSelect)

        spButton = Button(
            size_hint=(defNum*num2, defNum*num),
            background_normal="./images/button_spell.png",
            pos_hint={'center_x': .5, 'center_y': .30})

        spButton.bind(on_press=dieSelect)

        saButton = Button(
            size_hint=(defNum*num2, defNum*num),
            background_normal="./images/button_special.png",
            pos_hint={'center_x': .8, 'center_y': .30})

        saButton.bind(on_press=dieSelect)

        tLabel = Label(
            text='DnD Dice Tower!',
            color=(0, 0, 0, 1),
            font_size='75sp',
            font_name='./images/Captain_Redemption.ttf',
            pos_hint={'center_x': .5, 'center_y': .85})
        self.add_widget(tLabel)

        dLabel = Label(
            text='Select your Option!',
            color=(0, 0, 0, 1),
            font_size='45sp',
            font_name='./images/Captain_Redemption.ttf',
            pos_hint={'center_x': .5, 'center_y': .75})


################################# Second page widgets! ##############################################################################

        backButton = Button(
                        text = 'Back',
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .1, 'center_y': .9})
        backButton.bind(on_press=backPage)

        manualButton = Button(
                        text = "Rnadom",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .35, 'center_y': .2})
        manualButton.bind(on_press=dieSelect)

        autoButton = Button(
                        text = "Roll Atk",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .5, 'center_y': .2})
        autoButton.bind(on_press=dieSelect)

        autoButton2 = Button(
                        text = "Roll Dmg",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .65, 'center_y': .2})
        autoButton2.bind(on_press=dieSelect)

        

        sLabel = Label(
                text='0',
                color = (0,0,0,1),
                font_size='40sp',
                font_name= './images/Captain_Redemption.ttf',
                pos_hint = {'center_x': .25, 'center_y': .7})

        sLabel2 = Label(
                text='0',
                color = (0,0,0,1),
                font_size='40sp',
                font_name= './images/Captain_Redemption.ttf',
                pos_hint = {'center_x': .25, 'center_y': .55})

        sLabel3 = Label(
                text='0',
                color = (0,0,0,1),
                font_size='40sp',
                font_name= './images/Captain_Redemption.ttf',
                pos_hint = {'center_x': .45, 'center_y': .7})

        sLabel4 = Label(
                text='0',
                color = (0,0,0,1),
                font_size='40sp',
                font_name= './images/Captain_Redemption.ttf',
                pos_hint = {'center_x': .45, 'center_y': .55})
        

        data = [{'text': i, 'is_selected': False} for i in wpData]

        args_converter = lambda row_index, rec: {'text': rec['text'],
                                                 'size_hint_x': 10,
                                                 'size_hint_y': None,
                                                 'font_size': 15,
                                                 'selected_color': (1,0,0,1),
                                                 'deselected_color': (0,0,0,1),
                                                 'height': 45}

        list_adapter = ListAdapter(data=data,
                                    args_converter=args_converter,
                                    cls=ListItemButton,
                                    selection_mode='single',
                                    allow_empty_selection=True)

        list_adapter.bind(on_selection_change=listSelected)


        list_view = ListView(adapter = list_adapter,
                             pos_hint = {'center_x': .75, 'center_y': .43},
                             size_hint = (0.25, 0.5))
        list_view.background_normal = (0,0,0,1)
        
        
##
####        list_adapter.bind(on_selection_change=self.selection_change)


################################# Third page widgets! ####################################################################################

        optionLabel = Label(
                text='Select your calculation option',
                color = (0,0,0,1),
                font_size='60sp',
                font_name= './images//Captain_Redemption.ttf',
                pos_hint = {'center_x': .5, 'center_y': .7})

##        manualDiceButton = Button(
##                        text = 'Manual',
##                        color = (0,0,0,1),
##                        size_hint = (.25, .25),
##                        font_size='35sp',
##                        pos_hint = {'center_x': .3, 'center_y': .5})
##        manualDiceButton.bind(on_press=diceSelection)
##
##        autoDiceButton = Button(
##                        text = 'AutoCal',
##                        color = (0,0,0,1),
##                        size_hint = (.25, .25),
##                        font_size='35sp',
##                        pos_hint = {'center_x': .7, 'center_y': .5})
##        autoDiceButton.bind(on_press=diceSelection)


################################# Forth page (AUTO) widgets! ##############################################################################

##        diceNumLabel = Label(
##                text='Number of Dice?',
##                color = (0,0,0,1),
##                font_size='50sp',
##                font_name= 'data/fonts/Captain_Redemption.ttf',
##                pos_hint = {'center_x': .25, 'center_y': .7})
##
##        yVal1 = 0.6
##        oneButton = Button(
##                        text = "1",
##                        color = (0,0,0,1),
##                        size_hint = (.1, .1),
##                        pos_hint = {'center_x': .16, 'center_y': yVal1})
##        oneButton.bind(on_press=autoSelection)
##
##        twoButton = Button(
##                        text = "2",
##                        color = (0,0,0,1),
##                        size_hint = (.1, .1),
##                        pos_hint = {'center_x': .32, 'center_y': yVal1})
##        twoButton.bind(on_press=autoSelection)
##
##        threeButton = Button(
##                        text = "3",
##                        color = (0,0,0,1),
##                        size_hint = (.1, .1),
##                        pos_hint = {'center_x': .48, 'center_y': yVal1})
##        threeButton.bind(on_press=autoSelection)
##
##        fourButton = Button(
##                        text = "4",
##                        color = (0,0,0,1),
##                        size_hint = (.1, .1),
##                        pos_hint = {'center_x': .64, 'center_y': yVal1})
##        fourButton.bind(on_press=autoSelection)
##
##        fiveButton = Button(
##                        text = "5",
##                        color = (0,0,0,1),
##                        size_hint = (.1, .1),
##                        pos_hint = {'center_x': .8, 'center_y': yVal1})
##        fiveButton.bind(on_press=autoSelection)
##
##
##        diceTypLabel = Label(
##                text='Type of Dice?',
##                color = (0,0,0,1),
##                font_size='50sp',
##                font_name= 'data/fonts/Captain_Redemption.ttf',
##                pos_hint = {'center_x': .22, 'center_y': .45})
##
####        diceTypLabel
##        yVal2 = 0.35
##        d4Button = Button(
##                        text = "d 4",
##                        color = (0,0,0,1),
##                        size_hint = (.1, .1),
##                        pos_hint = {'center_x': .16, 'center_y': yVal2})
##        d4Button.bind(on_press=autoSelection)
##
##        d6Button = Button(
##                        text = "d 6",
##                        color = (0,0,0,1),
##                        size_hint = (.1, .1),
##                        pos_hint = {'center_x': .288, 'center_y': yVal2})
##        d6Button.bind(on_press=autoSelection)
##
##        d8Button = Button(
##                        text = "d 8",
##                        color = (0,0,0,1),
##                        size_hint = (.1, .1),
##                        pos_hint = {'center_x': .416, 'center_y': yVal2})
##        d8Button.bind(on_press=autoSelection)
##
##        d10Button = Button(
##                        text = "d 10",
##                        color = (0,0,0,1),
##                        size_hint = (.1, .1),
##                        pos_hint = {'center_x': .544, 'center_y': yVal2})
##        d10Button.bind(on_press=autoSelection)
##
##        d12Button = Button(
##                        text = "d 12",
##                        color = (0,0,0,1),
##                        size_hint = (.1, .1),
##                        pos_hint = {'center_x': .672, 'center_y': yVal2})
##        d12Button.bind(on_press=autoSelection)
##
##        d20Button = Button(
##                        text = "d 20",
##                        color = (0,0,0,1),
##                        size_hint = (.1, .1),
##                        pos_hint = {'center_x': .8, 'center_y': yVal2})
##        d20Button.bind(on_press=autoSelection)


####        totalLabel = Label(
####                text='? d ? to Roll',
####                color = (0,0,0,1),
####                font_size='40sp',
####                font_name= 'data/fonts/thecroach.ttf',
####                pos_hint = {'center_x': .3, 'center_y': .2})
##
##        cal2Button = Button(
##                        text = "=",
##                        color = (0,0,0,1),
##                        size_hint = (.1, .1),
##                        pos_hint = {'center_x': .5, 'center_y': .2})
##        cal2Button.bind(on_press=autoSelection)

        totalValLabel = Label(
                text='??',
                color = (0,0,0,1),
                font_size='80sp',
                font_name= './images/Captain_Redemption.ttf',
                pos_hint = {'center_x': .5, 'center_y': .5})


################################# Forth page (MANUAL) widgets! ############################################################################

        yValf = 0.65
        yVals = 0.55
        yValt = 0.45
        yValfr = 0.35
        num1Button = Button(
                        text = "1",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .16, 'center_y': yValf})
        num1Button.bind(on_press=manualSelection)

        num2Button = Button(
                        text = "2",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .32, 'center_y': yValf})
        num2Button.bind(on_press=manualSelection)

        num3Button = Button(
                        text = "3",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .48, 'center_y': yValf})
        num3Button.bind(on_press=manualSelection)

        num4Button = Button(
                        text = "4",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .64, 'center_y': yValf})
        num4Button.bind(on_press=manualSelection)

        num5Button = Button(
                        text = "5",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .8, 'center_y': yValf})
        num5Button.bind(on_press=manualSelection)

        num6Button = Button(
                        text = "6",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .16, 'center_y': yVals})
        num6Button.bind(on_press=manualSelection)

        num7Button = Button(
                        text = "7",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .32, 'center_y': yVals})
        num7Button.bind(on_press=manualSelection)

        num8Button = Button(
                        text = "8",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .48, 'center_y': yVals})
        num8Button.bind(on_press=manualSelection)

        num9Button = Button(
                        text = "9",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .64, 'center_y': yVals})
        num9Button.bind(on_press=manualSelection)

        num10Button = Button(
                        text = "10",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .8, 'center_y': yVals})
        num10Button.bind(on_press=manualSelection)

        num11Button = Button(
                        text = "11",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .16, 'center_y': yValt})
        num11Button.bind(on_press=manualSelection)

        num12Button = Button(
                        text = "12",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .32, 'center_y': yValt})
        num12Button.bind(on_press=manualSelection)

        num13Button = Button(
                        text = "13",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .48, 'center_y': yValt})
        num13Button.bind(on_press=manualSelection)

        num14Button = Button(
                        text = "14",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .64, 'center_y': yValt})
        num14Button.bind(on_press=manualSelection)

        num15Button = Button(
                        text = "15",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .8, 'center_y': yValt})
        num15Button.bind(on_press=manualSelection)

        num16Button = Button(
                        text = "16",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .16, 'center_y': yValfr})
        num16Button.bind(on_press=manualSelection)

        num17Button = Button(
                        text = "17",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .32, 'center_y': yValfr})
        num17Button.bind(on_press=manualSelection)

        num18Button = Button(
                        text = "18",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .48, 'center_y': yValfr})
        num18Button.bind(on_press=manualSelection)

        num19Button = Button(
                        text = "19",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .64, 'center_y': yValfr})
        num19Button.bind(on_press=manualSelection)

        num20Button = Button(
                        text = "20",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .8, 'center_y': yValfr})
        num20Button.bind(on_press=manualSelection)

        clearButton = Button(
                        text = "clear",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .65, 'center_y': .2})
        clearButton.bind(on_press=manualSelection)

        totalManLabel = Label(
                text='The total value = 0',
                color = (0,0,0,1),
                font_size='40sp',
                font_name= './images/Captain_Redemption.ttf',
                pos_hint = {'center_x': .33, 'center_y': .2})




###########################################################################################################################################

##        zp_list.append()
##        zp_list.append()
##        zp_list.append()
##        zp_list.append()
##        zp_list.append()
##        zp_list.append()


        fp_list.append(initButton)
        fp_list.append(stButton)
        fp_list.append(spButton)
        fp_list.append(skButton)
        fp_list.append(saButton)
        fp_list.append(wpButton)
        fp_list.append(dLabel)
        # fp_list.append(initImg)
        # fp_list.append(stImg)
        # fp_list.append(dmgImg)
        # fp_list.append(skImg)
        # fp_list.append(saImg)
        # fp_list.append(wpImg)

##        fp_list.append(initLabel)
##        fp_list.append(stLabel)
##        fp_list.append(dmgLabel)
##        fp_list.append(skLabel)
##        fp_list.append(saLabel)
##        fp_list.append(wpLabel)

        sp_list.append(backButton)
##        sp_list.append(calButton)
        sp_list.append(list_view)
        sp_list.append(sLabel)
        sp_list.append(sLabel2)
        sp_list.append(sLabel3)
        sp_list.append(sLabel4)
        sp_list.append(manualButton)
        sp_list.append(autoButton)
        sp_list.append(autoButton2)

##        tp_list.append(manualDiceButton)
##        tp_list.append(autoDiceButton)
        tp_list.append(backButton)
        tp_list.append(optionLabel)


##        f2p_list.append(diceNumLabel)
##        f2p_list.append(diceTypLabel)
##        f2p_list.append(oneButton)
##        f2p_list.append(twoButton)
##        f2p_list.append(threeButton)
##        f2p_list.append(fourButton)
##        f2p_list.append(fiveButton)
##        f2p_list.append(totalLabel)
##        f2p_list.append(d4Button)
##        f2p_list.append(d6Button)
##        f2p_list.append(d8Button)
##        f2p_list.append(d10Button)
##        f2p_list.append(d12Button)
##        f2p_list.append(d20Button)
        f2p_list.append(backButton)
        f2p_list.append(totalValLabel)
##        f2p_list.append(cal2Button)

##        f3p_list.append(list_view2)
##        f3p_list.append(list_view3)
        f3p_list.append(num1Button)
        f3p_list.append(num2Button)
        f3p_list.append(num3Button)
        f3p_list.append(num4Button)
        f3p_list.append(num5Button)
        f3p_list.append(num6Button)
        f3p_list.append(num7Button)
        f3p_list.append(num8Button)
        f3p_list.append(num9Button)
        f3p_list.append(num10Button)
        f3p_list.append(num11Button)
        f3p_list.append(num12Button)
        f3p_list.append(num13Button)
        f3p_list.append(num14Button)
        f3p_list.append(num15Button)
        f3p_list.append(num16Button)
        f3p_list.append(num17Button)
        f3p_list.append(num18Button)
        f3p_list.append(num19Button)
        f3p_list.append(num20Button)
        f3p_list.append(backButton)
        f3p_list.append(clearButton)
        f3p_list.append(totalManLabel)

##        f2p_list.append(sixButton)



        for item in sp_list:
            self.remove_widget(item)

        for item2 in fp_list:
            self.add_widget(item2)


    def btn_pressed(self, instance, pos):
        print ('pos: printed from widget: {pos}'.format(pos=pos))



class CustomBtn(Widget):

    pressed = ListProperty([0,0])
    text = "hello"

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            return True
        return super(CustomBtn, self).on_touch_down(touch)

    def on_pressed(self, instance, pos):
        print ('pressed at {pos}'.format(pos=pos))

class MainApp(App):

    def build(self):
        self.root = root = RootWidget()
##        root.bind(size=self._update_rect, pos = self._update_rect)

##        with root.canvas.before:
##            Color(1, 1, 1, 1)
##            self.rect = Rectangle(size = root.size,
##                                  pos = root.pos,
##                                  source = "./images/dice.jpeg")
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    MainApp().run()
