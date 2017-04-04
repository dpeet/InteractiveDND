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
import operator
from random import shuffle

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
##            source: "./images/4.png"
''')

currentPlayer = None
currentPage = None ## 1=init , 2=saving throw , 3=weapons , 4=skills , 5=spells , 6=special ability
pageNum = 0
sortedPlayerNames = None
unsortedPalyerNames = None
playerDic = None

class RootWidget(FloatLayout):


    Window.size = (480, 800)
    def callback2(instance):
        print('The button <%s> is being pressed' % instance.text)



    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        global unsortedPlayerNames
        global sortedPlayerNames
        fp_list = list()
        sp_list = list()
        tp_list = list()
        f2p_list = list()
        initp_list = list()
        wpp_list = list()
        initp_list = list()
        spp_list = list()
        stp_list = list()
        skp_list = list()
        
        f3p_list = list()
        zp_list = list()
        playerList = list()
        playerNames = list()
        unsortedPlayerNames = list()
        sortedPlayerNames = list()
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

##        skData = ["Acrobatics (Dex)",
##                "Animal Handling (Wis)",
##                "Arcana (Int)",
##                "Athletics (Str)",
##                "Deception (Cha)",
##                "History (Int)",
##                "Insight (Wis)",
##                "Intimidation (Cha)",
##                "Investigation (Int)",
##                "Medicine (Wis)",
##                "Nature (Int)",
##                "Perception (Wis)",
##                "Performance (Cha)",
##                "Persuasion (Cha)",
##                "Religion (Int)",
##                "Sleight of Hand (Dex)",
##                "Stealth (Dex)",
##                "Survival (Wise)"]

        skData = ["Acrobatics",
                "Animal Handling",
                "Arcana",
                "Athletics",
                "Deception",
                "History",
                "Insight",
                "Intimidation",
                "Investigation",
                "Medicine",
                "Nature",
                "Perception",
                "Performance",
                "Persuasion",
                "Religion",
                "Sleight of Hand",
                "Stealth",
                "Survival"]
        skDataS = ["dex","wis", "int", "str", "cha", "int", "wis", "cha", "int",
                "wis", "int", "wis", "cha", "cha", "int", "dex", "dex", "wis"]
##
        stData = ["Strength",
                "Dexterity",
                "Constitution",
                "Intelligence",
                "Wisdom",
                "Charisma"]

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
                if currentPage == 3:
                    for item in wpp_list:
                        self.remove_widget(item)
                elif currentPage == 1:
                    for item2 in initp_list:
                        self.remove_widget(item2)
                elif currentPage == 5:
                    for item2 in spp_list:
                        self.remove_widget(item2)
                elif currentPage == 2:
                    for item2 in stp_list:
                        self.remove_widget(item2)
                elif currentPage == 4:
                    for item2 in skp_list:
                        self.remove_widget(item2)
                else:
                    for item in sp_list:
                        self.remove_widget(item)

                for item2 in fp_list:
                    self.add_widget(item2)

                die = 0
                pageNum = 1
                dLabel.text = ('Select your Die!')

            elif pageNum == 3:
                for item in tp_list:
                    self.remove_widget(item)

                for item2 in sp_list:
                    self.add_widget(item2)
                pageNum = 2

            elif pageNum == 4:
                for item in f2p_list:
                    self.remove_widget(item)
                for item in f3p_list:
                    self.remove_widget(item)

                for item2 in tp_list:
                    self.add_widget(item2)
                pageNum = 3

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
                totalValLabel.text = ("%s rolled  %s !!!" % (spinner.text, str(sum(get_num_from_dice()))))
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


        def manualSelection(instance):
            if instance == clearButton:
                totalManLabel.text = "The total value = 0"
            else:
                num = int(instance.text)
                mylist = totalManLabel.text.split(" ")
                num2 = int(mylist[len(mylist)-1])
                num2 = num2 + num
                totalManLabel.text = ("The total Value = %d" % num2)

        def exitB(instance):
            App.get_running_app().stop()




        def dieSelect(instance):
            global die
            global selected1
            global pageNum
            global initFlag
            global currentPage
##            global currentPlayer
            flag = True
            data = None

            if instance == initButton:
                dLabel.text = ('%s is selected!' % instance.text)
                sLabel5.text = "Initiative"
                data = [{'text': i, 'is_selected': False} for i in playerNames]
                list_adapter2.data = data
                list_view2.populate()
                data = [{'text': i, 'is_selected': False} for i in []]
                list_adapter3.data = data
                list_view3.populate()
                sLabel3.text = '0'
                sLabel2.text = '0'
                sLabel.text = '0'
                initFlag = True
                currentPage = 1
                die = 1
            elif instance == stButton:
                dLabel.text = ('%s is selected!' % instance.text)
                sLabel5.text = "Saving Throw"
                sLabel2.text = '0'
                sLabel3.text = '0'
                sLabel.text = '0'
                attack.source = "./images/Field_Save.png"
##                attack.source = "./images/Field_Attack.png"
                data = [{'text': i, 'is_selected': False} for i in stData]
                initFlag = False
                currentPage = 2
                die = 2
            elif instance == wpButton:
                dLabel.text = ('%s is selected!' % instance.text)
                sLabel5.text = "Weapons"
                wpData = []
                for item in playerDic[currentPlayer.playerName].weapons:
                    wpData.append(item[0])
##                wpData = playerDic[currentPlayer.playerName].weapons
                attack.source = "./images/Field_Attack.png"
                data = [{'text': i, 'is_selected': False} for i in wpData]
                sLabel2.text = '0'
                sLabel3.text = '0'
                sLabel.text = '0'
                sLabel4.text = '0'
                initFlag = False
                currentPage = 3
                die = 3
            elif instance == skButton:
                dLabel.text = ('%s is selected!' % instance.text)
                sLabel5.text = "Skills"
##                skData = playerDic[currentPlayer.playerName].skills
                skData = []
                for item in playerDic[currentPlayer.playerName].skills:
                    skData.append(item)
                print(skData)
                attack.source = "./images/Field_Attack.png"
                data = [{'text': i, 'is_selected': False} for i in skData]
                sLabel2.text = '0'
                sLabel3.text = '0'
                sLabel.text = '0'
                skStatLabel.text = '--'
                initFlag = False
                currentPage = 4
                die = 4
            elif instance == spButton:
                dLabel.text = ('%s is selected!' % instance.text)
                print(currentPlayer.playerName)
                print(playerDic[currentPlayer.playerName].spells)
                spData = playerDic[currentPlayer.playerName].spells
                data = [{'text': i, 'is_selected': False} for i in spData]
                attack.source = "./images/Field_Attack.png"
                sLabel5.text = "Spells"
                
                sLabel2.text = '0'
                sLabel3.text = '0'
                sLabel.text = '0'
                initFlag = False
                currentPage = 5
                die = 5
            elif instance == saButton:
                dLabel.text = ('%s is selected!' % instance.text)
                sLabel5.text = "Special Ability"
##                attack.source = "./images/Button.png"
                attack.source = "./images/Field_Attack.png"
                saData = playerDic[currentPlayer.playerName].special
                data = [{'text': i, 'is_selected': False} for i in saData]
                sLabel2.text = '0'
                sLabel3.text = '0'
                sLabel.text = '0'
                initFlag = False
                currentPage = 6
                die = 6
            elif instance == manualButton:
                flag = False
                selected1 = list_adapter.selection
                if not selected1:
                    sLabel.text = "Select!"
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
                        if currentPage == 3:
                            selectedItem = list_adapter.selection[0].text
                            sLabel.color = (0,0,0,1)

    ##                        selectedItem = list_adpater.selection[0].text
                            txt = sLabel4.text
                            myList = txt.split("d")
                            myList2 = myList[1].split("+")
                            
                            ran = random.randint(1, 20)
                            sLabel.text = str(ran +int(sLabel3.text))
                            sLabel2.text = str(ran +int(myList2[1]))
                            print("here %d" % pageNum)
                        else:
                            ran = random.randint(1, 20)
                            selectedItem = list_adapter.selection[0].text
                            sLabel.color = (0,0,0,1)
                            sLabel.text = str(ran +int(sLabel3.text))

            elif instance == autoButton:
                flag = False
                selected1 = list_adapter.selection
                if not selected1:
                    sLabel.text = "Select!"
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
                        
                        sLabel.text = str(sum(get_num_from_dice())+int(sLabel3.text))
                        
##                        ran = random.randint(1, 100)
##                        sLabel2.text = ('Value: %d' % ran)

                        print("here %d" % pageNum)
            elif instance == autoButton2:
                flag = False
                selected1 = list_adapter.selection
                if not selected1:
                    sLabel2.text = "Select!"
                    sLabel2.color = (1,0,0,1)
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
##                        sLabel.color = (0,0,0,1)
                        txt = sLabel4.text
                        myList = txt.split("d")
                        myList2 = myList[1].split("+")
                        sLabel2.text = str(sum(get_num_from_dice())+int(myList2[1]))


            elif instance == tieButton:
                flag = False
                if len(list_adapter3.data) > 0:
                    if len(list_adapter3.data) == len(playerNames):
                        previous = -1
                        prevItem = None
                        probList = list()
                        finalList = list()

                        
                        index = 0
                        minI = -1
                        maxI = len(list_adapter3.data)
                        flg = False
                        
                        for item in list_adapter3.data:
                            if previous == -1:
                                prevItem = item
                                previous = int(item['text'].split(' ')[0])
                            else:
                                if previous == int(item['text'].split(' ')[0]):
                                    if len(probList) == 0:
                                        probList.append(prevItem['text'])
                                        probList.append(item['text'])
                                    else:
                                        probList.append(item['text'])
                                    if (minI < 0 and not flg):
                                        flg = True
                                        minI = index - 2
                                    prevItem = item
                                    previous = int(item['text'].split(' ')[0])
                                    maxI = index
                                else:
                                    prevItem = item
                                    previous = int(item['text'].split(' ')[0])
                            index = index + 1

                        shuffle(probList)
                        if len(probList) != 0:
                            
                            index = 0
                            once = 0
                            finalList.append("!!Final Order!!")
                            for item in list_adapter3.data:
                                if index <= minI:
                                    finalList.append("%s. %s" % (str(index + 1), item['text'].split(' ')[2]))
                                elif (index > minI and once == 0):
                                    num = index
                                    for item2 in probList:
                                        finalList.append("%s. %s" % (str(num + 1), item2.split(' ')[2]))
                                        num = num+1
                                    once = 1

                                elif index > maxI:
                                    finalList.append("%s. %s" % (str(index+1), item['text'].split(' ')[2]))
                                print(index)
                                index = index + 1
                            data = [{'text': i, 'is_selected': False} for i in finalList]
                            list_adapter3.data = data
                            list_view3.populate()

            elif instance == rollButton:
                flag = False
                selected1 = list_adapter.selection
                if not selected1:
                    sLabel.text = "Select!"
                    sLabel.color = (1,0,0,1)
                else:
                    if initFlag:
                        selectedItem = list_adapter.selection[0].text
                        sLabel.color = (0,0,0,1)
                        sLabel.text = selectedItem
                    else:
                        selectedItem = list_adapter.selection[0].text
                        sLabel.color = (0,0,0,1)
                        sLabel.text = str(sum(get_num_from_dice())+int(sLabel3.text))
                      
            else:
                print('what is this?')

            if flag:
                list_adapter.data = data
                list_view.populate()
                for item in fp_list:
                    self.remove_widget(item)
                    
                if currentPage == 3:
                    for item2 in wpp_list:
                        self.add_widget(item2)
                elif currentPage == 1:
                    for item2 in initp_list:
                        self.add_widget(item2)
                elif currentPage == 5:
                    for item2 in spp_list:
                        self.add_widget(item2)
                elif currentPage == 2:
                    for item2 in stp_list:
                        self.add_widget(item2)
                elif currentPage == 4:
                    for item2 in skp_list:
                        self.add_widget(item2)
                else:
                    for item2 in sp_list:
                        self.add_widget(item2)
            
            pageNum = 2

        def show_selected_value(spinner, text):
            global currentPlayer
            currentPlayer = playerDic[text]
##            print("here")
            if pageNum == 2:
                if currentPage == 1:
                    data = [{'text': i, 'is_selected': False} for i in initData]

                elif currentPage == 2:
                    data = [{'text': i, 'is_selected': False} for i in stData]
##                    print("Saving")

                if currentPage == 3:
                    wpData = []
                    for item in playerDic[currentPlayer.playerName].weapons:
                        wpData.append(item[0])
                    data = [{'text': i, 'is_selected': False} for i in wpData]

                elif currentPage == 4:
                    skData = []
                    for item in playerDic[currentPlayer.playerName].skills:
                        skData.append(item)
                    data = [{'text': i, 'is_selected': False} for i in skData]

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
##            global unsortedPlayerNames
##            global sortedPlayerNames
##            print("here")
##            print(selectedItem = list_adapter.selection[0].text)
            if len(list_adapter.selection) > 0:
                selectedItem = list_adapter.selection[0].text
                if currentPage == 3:
                    for item in currentPlayer.weapons:
                        if item[0] == selectedItem:
                            sLabel3.text = item[1]
                            sLabel4.text = item[2]
                elif currentPage == 2:
                    profstat = currentPlayer.profStats
                    stat = selectedItem[:3].lower()
                    if stat in profstat:
                        sLabel3.text = str(currentPlayer.prof)
                    else:
                        sLabel3.text = "0"
                elif currentPage == 4:
                    ind = skData.index(str(selectedItem))
                    skStatLabel.text = skDataS[ind].upper()
                    
                    stat = ""
                    if skDataS[ind] == "str":
                        stat = currentPlayer.str
                    elif skDataS[ind] == "dex":
                        stat =  currentPlayer.dex
                    elif skDataS[ind] == "con":
                        stat =  currentPlayer.con
                    elif skDataS[ind] == "int":
                        stat =  currentPlayer.int
                    elif skDataS[ind] == "wis":
                        stat =  currentPlayer.wis
                    elif skDataS[ind] == "cha":
                        stat =  currentPlayer.cha
                    sLabel3.text = str(stat)

                elif currentPage == 5:
                    sLabel3.text = str(currentPlayer.int)
                    
            elif len(list_adapter2.selection) > 0:
                if currentPage == 1:
                    selectedItem = list_adapter2.selection[0].text
####                    print("here")
##                    print(list_adapter2.data)
##                    print(unsortedPlayerNames)
##                    print(sortedPlayerNames)
                    newList = list()
                    newList2 = list()
                    newList2Names = list()
                    if len(list_adapter2.data) > 0:
                        for item in list_adapter2.data:
##                            print(item)
                            if item['text'] != list_adapter2.selection[0].text:
                                newList.append(item['text'])
                    data = [{'text': i, 'is_selected': False} for i in newList]
                    list_adapter2.data = data
                    list_view2.populate()
                    tempDic = list()
                    ran = random.randint(1,20)
                    if len(list_adapter3.data) > 0:
                        for item in list_adapter3.data:
                            if item['text'] != selectedItem:
                                newList2.append(item['text'])
                                tempDic.append((item['text'], int(item['text'].split(' ')[0])))
                    dexx = playerDic[selectedItem].dex
                    ran = ran + dexx

                    tempDic.append((("%d - %s" % (ran, selectedItem)), ran))
                    newList2.append("%d - %s" % (ran, selectedItem))
                    newList2.sort()

##                    sList = [('10 - Devon', 10), ('10 - Todd', 10), ('10 - Ginger', 10), ('3 - Devon3', 3), ('2 - Devon2', 2), ('14 - Devon', 14)]
                    
                    sList = sorted(tempDic, key=lambda dic: dic[1], reverse=True)
##                    sList = [ ('14 - Devon', 14), ('10 - Devon5', 10), ('10 - Todd', 10), ('10 - Ginger', 10), ('3 - Devon3', 3), ('2 - Devon2', 2)]
##                    sList = [ ('10 - Devon', 10), ('10 - Todd', 10), ('10 - Ginger', 10), ('3 - Devon3', 3), ('2 - Devon2', 2)]
##                    sList = [ ('14 - Devon', 14), ('11 - Devon', 11), ('10 - Devon', 10), ('10 - Todd', 10), ('10 - Ginger', 10), ('3 - Devon3', 3), ('2 - Devon2', 2)]
##                    print(sList)
                    fList = list()
                    for item in sList:
                        fList.append(item[0])

                    print(fList)
##                    fList = ['10 - Devon', '10 - Todd', '10 - Ginger', ']
                    data = [{'text': i, 'is_selected': False} for i in fList]
                    list_adapter3.data = data
                    list_view3.populate()
                    

################################# 0 page widgets! ########################################################################################


        spinner = Spinner(
                        # default value shown
                        text=currentPlayer.playerName,
                        # available values
                        values=playerNames,
                        # just for positioning in our example
                        size_hint=(0.175, 0.05),
##                        size=(100, 44),
                        pos_hint={'center_x': .9, 'center_y': .95})
        spinner.bind(text=show_selected_value)
        self.add_widget(spinner)
################################# First page widgets! ####################################################################################
        exitButton = Button(
            text = 'Exit',
            size_hint=(0.175, 0.05),
##                        size=(100, 44),
            pos_hint={'center_x': .5, 'center_y': .95})

        exitButton.bind(on_press=exitB)

        self.add_widget(exitButton)

        def get_scalex_and_y(target_width, width, height):
            screen_width = 480.0
            screen_height = 800.0
            x_s = target_width/screen_width
            y_s = (target_width*height/width)/screen_height
            # print(target_width, height, width, screen_height)
            # print (x_s, y_s, x_s/y_s)
            return x_s, y_s

        get_scalex_and_y(50, 5, 10)

        
        dImg1 = Image(source='./images/box.png',
                        pos_hint = {'center_x': .5, 'center_y': .35},
                        size_hint = (.9,.7))

        initButton = Button(
            size_hint=(get_scalex_and_y(125,125,125)[0], get_scalex_and_y(125,125,125)[1]),
            background_normal="./images/button_init.png",
            pos_hint={'center_x': .20, 'center_y': .4})

        initButton.bind(on_press=dieSelect)

        stButton = Button(
            size_hint=(get_scalex_and_y(125,125,125)[0], get_scalex_and_y(125,125,125)[1]),
            background_normal="./images/button_saving_throw.png",
            pos_hint={'center_x': .5, 'center_y': .4})

        stButton.bind(on_press=dieSelect)

        wpButton = Button(
            size_hint=(get_scalex_and_y(125,125,125)[0], get_scalex_and_y(125,125,125)[1]),
##            size= (0.1, .1),
            background_normal="./images/button_weapons.png",
            pos_hint={'center_x': .8, 'center_y': .4})

        wpButton.bind(on_press=dieSelect)

        skButton = Button(
            size_hint=(get_scalex_and_y(125,125,125)[0], get_scalex_and_y(125,125,125)[1]),
            background_normal="./images/button_skills.png",
            pos_hint={'center_x': .2, 'center_y': .2})

        skButton.bind(on_press=dieSelect)

        spButton = Button(
            size_hint=(get_scalex_and_y(125,125,125)[0], get_scalex_and_y(125,125,125)[1]),
            background_normal="./images/button_spell.png",
            pos_hint={'center_x': .5, 'center_y': .2})

        spButton.bind(on_press=dieSelect)

        saButton = Button(
            size_hint=(get_scalex_and_y(125,125,125)[0], get_scalex_and_y(125,125,125)[1]),
            background_normal="./images/button_special.png",
            pos_hint={'center_x': .8, 'center_y': .20})

        saButton.bind(on_press=dieSelect)

        tLabel = Label(
            text='DnD Dice Tower!',
            color=(0, 0, 0, 1),
            font_size='75sp',
            font_name='./images/Captain_Redemption.ttf',
            pos_hint={'center_x': .5, 'center_y': .765}
        )
        self.add_widget(tLabel)

        dragon = Image(
            source="./images/Dragon_Title.png",
            pos_hint = {'center_x': .5, 'center_y': .78}
        )


        self.add_widget(dragon)

        dLabel = Label(
            text='Select your Option!',
            color=(0, 0, 0, 1),
            font_size='45sp',
            font_name='./images/Captain_Redemption.ttf',
            pos_hint={'center_x': .5, 'center_y': .6})


################################# Second page widgets! ##############################################################################
        
        
        dImg2 = Image(source='./images/box2.png',
                        pos_hint = {'center_x': .48, 'center_y': .45},
                        size_hint = (.16,.16))

        dImg3 = Image(source='./images/box2.png',
                        pos_hint = {'center_x': .48, 'center_y': .25},
                        size_hint = (.16,.16))
        dImg4 = Image(source='./images/DiceRoll.png',
                        pos_hint = {'center_x': .5, 'center_y': .35},
                        size_hint = (.9,.7))

        
        
        backButton = Button(
            text='Back',
            color=(1, 1, 1, 1),
            size_hint=(0.175, 0.05),
            pos_hint={'center_x': .1, 'center_y': .95})
        backButton.bind(on_press=backPage)

        manualButton = Button(
            text="Random",
            color=(255, 255, 255, 1),
            size_hint=(0.175, 0.05),
            pos_hint={'center_x': .25, 'center_y': .1})
        manualButton.bind(on_press=dieSelect)

        autoButton = Button(
            text="Roll Atk",
            color=(255, 255, 255, 1),
            size_hint=(0.175, 0.05),
            pos_hint={'center_x': .5, 'center_y': .1})
        autoButton.bind(on_press=dieSelect)

        autoButton2 = Button(
            text="Roll Dmg",
            color=(255, 255, 255, 1),
            size_hint=(0.175, 0.05),
            pos_hint={'center_x': .75, 'center_y': .1})
        autoButton2.bind(on_press=dieSelect)

        attack = Image(
            source="./images/Field_Attack.png",
            pos_hint={'center_x': .25, 'center_y': .43}
        )

        Damage = Image(
            source="./images/Field_Damage.png",
            pos_hint={'center_x': .25, 'center_y': .23}
        )

        sLabel = Label(
                text='0',
                color = (0,0,0,1),
                font_size='40sp',
                font_name= './images/Captain_Redemption.ttf',
                pos_hint = {'center_x': .25, 'center_y': .45})

        sLabel2 = Label(
                text='0',
                color = (0,0,0,1),
                font_size='40sp',
                font_name= './images/Captain_Redemption.ttf',
                pos_hint = {'center_x': .25, 'center_y': .25})

        sLabel3 = Label(
                text='0',
                color = (0,0,0,1),
                font_size='25sp',
                font_name= './images/Captain_Redemption.ttf',
                pos_hint = {'center_x': .48, 'center_y': .45})

        sLabel4 = Label(
                text='0',
                color = (0,0,0,1),
                font_size='25sp',
                font_name= './images/Captain_Redemption.ttf',
                pos_hint = {'center_x': .48, 'center_y': .25})
        sLabel5 = Label(
                text='Yes',
                color = (0,0,0,1),
                font_size='25sp',
                font_name= './images/Captain_Redemption.ttf',
                pos_hint = {'center_x': .23, 'center_y': .6})

        data = [{'text': i, 'is_selected': False} for i in wpData]

        args_converter = lambda row_index, rec: {'text': rec['text'],
                                                 'size_hint_x': 10,
                                                 'size_hint_y': None,
                                                 'font_size': 15,
                                                 'selected_color': (.5,.5,.5,.25),
                                                 'deselected_color': (50,50,50,1),
                                                 'color': (0, 0, 0, 1),
                                                 'height': 45}

        list_adapter = ListAdapter(data=data,
                                    args_converter=args_converter,
                                    cls=ListItemButton,
                                    selection_mode='single',
                                    allow_empty_selection=True)

        list_adapter.bind(on_selection_change=listSelected)


        list_view = ListView(adapter = list_adapter,
                             pos_hint = {'center_x': .75, 'center_y': .37},
                             size_hint = (0.25, 0.35))
        list_view.background_normal = (0,0,0,0)
        
        
##
####        list_adapter.bind(on_selection_change=self.selection_change)


################################# Init page widgets! ####################################################################################

##        optionLabel = Label(
##                text='Select your calculation option',
##                color = (0,0,0,1),
##                font_size='60sp',
##                font_name= './images//Captain_Redemption.ttf',
##                pos_hint = {'center_x': .5, 'center_y': .7})
        unsortedPalyerNames = playerNames
        
        data = [{'text': i, 'is_selected': False} for i in playerNames]

        args_converter = lambda row_index, rec: {'text': rec['text'],
                                                 'size_hint_x': 10,
                                                 'size_hint_y': None,
                                                 'font_size': 15,
                                                 'selected_color': (.5,.5,.5,.25),
                                                 'deselected_color': (50,50,50,1),
                                                 'color': (0, 0, 0, 1),
                                                 'height': 45}

        list_adapter2 = ListAdapter(data=data,
                                    args_converter=args_converter,
                                    cls=ListItemButton,
                                    selection_mode='single',
                                    allow_empty_selection=True)

        list_adapter2.bind(on_selection_change=listSelected)


        list_view2 = ListView(adapter = list_adapter2,
                             pos_hint = {'center_x': .25, 'center_y': .28},
                             size_hint = (0.25, 0.5))
        list_view2.background_normal = (0,0,0,0)

        sortedPlayerList = []

        data3 = [{'text': i, 'is_selected': False} for i in sortedPlayerList]

        args_converter3 = lambda row_index, rec: {'text': rec['text'],
                                                 'size_hint_x': 10,
                                                 'size_hint_y': None,
                                                 'font_size': 15,
                                                 'selected_color': (.5,.5,.5,.25),
                                                 'deselected_color': (50,50,50,1),
                                                 'color': (0, 0, 0, 1),
                                                 'height': 45}

        list_adapter3 = ListAdapter(data=data3,
                                    args_converter=args_converter3,
                                    cls=ListItemButton,
                                    selection_mode='single',
                                    allow_empty_selection=True)

        list_adapter3.bind(on_selection_change=listSelected)


        list_view3 = ListView(adapter = list_adapter3,
                             pos_hint = {'center_x': .75, 'center_y': .28},
                             size_hint = (0.25, 0.5))
        list_view3.background_normal = (0,0,0,0)


        tieButton = Button(
            text="Tie Breaker",
            color=(255, 255, 255, 1),
            size_hint=(0.175, 0.05),
            pos_hint={'center_x': .5, 'center_y': .1})
        tieButton.bind(on_press=dieSelect)

        totalValLabel = Label(
                text='??',
                color = (0,0,0,1),
                font_size='80sp',
                font_name= './images/Captain_Redemption.ttf',
                pos_hint = {'center_x': .5, 'center_y': .5})

        rollButton = Button(
            text="Roll",
            color=(255, 255, 255, 1),
            size_hint=(0.175, 0.05),
            pos_hint={'center_x': .75, 'center_y': .1})
        rollButton.bind(on_press=dieSelect)

        skStatLabel = Label(
                text='--',
                color = (0,0,0,1),
                font_size='33sp',
                font_name= './images/Captain_Redemption.ttf',
                pos_hint = {'center_x': .48, 'center_y': .37})

#################################################################################################################################

        fp_list.append(dImg1)
        fp_list.append(initButton)
        fp_list.append(stButton)
        fp_list.append(spButton)
        fp_list.append(skButton)
        fp_list.append(saButton)
        fp_list.append(wpButton)
        fp_list.append(dLabel)
        
        sp_list.append(backButton)
        sp_list.append(list_view)
        sp_list.append(attack)
        sp_list.append(Damage)
        sp_list.append(sLabel)
        sp_list.append(sLabel2)
        sp_list.append(sLabel3)
        sp_list.append(sLabel4)
        sp_list.append(manualButton)
        sp_list.append(autoButton)
        sp_list.append(autoButton2)
        sp_list.append(dImg4)
        sp_list.append(sLabel5)
        

        wpp_list.append(dImg2)
        wpp_list.append(dImg3)
        wpp_list.append(dImg4)
        wpp_list.append(backButton)
        wpp_list.append(list_view)
        wpp_list.append(attack)
        wpp_list.append(Damage)
        wpp_list.append(sLabel)
        wpp_list.append(sLabel2)
        wpp_list.append(sLabel3)
        wpp_list.append(sLabel4)
        wpp_list.append(manualButton)
        wpp_list.append(autoButton)
        wpp_list.append(autoButton2)
        wpp_list.append(sLabel5)

        initp_list.append(dImg4)
        initp_list.append(sLabel5)
        initp_list.append(list_view2)
        initp_list.append(backButton)
        initp_list.append(list_view3)
        initp_list.append(tieButton)

        spp_list.append(dImg2)
        spp_list.append(dImg4)
        spp_list.append(backButton)
        spp_list.append(list_view)
        spp_list.append(attack)
        spp_list.append(sLabel)
##        spp_list.append(sLabel2)
        spp_list.append(sLabel3)
        spp_list.append(sLabel5)
        spp_list.append(manualButton)
        spp_list.append(rollButton)

        stp_list.append(dImg2)
        stp_list.append(dImg4)
        stp_list.append(backButton)
        stp_list.append(list_view)
        stp_list.append(attack)
        stp_list.append(sLabel)
        stp_list.append(sLabel5)
        stp_list.append(sLabel3)
        stp_list.append(manualButton)
        stp_list.append(rollButton)

        skp_list.append(dImg2)
        skp_list.append(dImg4)
        skp_list.append(backButton)
        skp_list.append(list_view)
        skp_list.append(attack)
        skp_list.append(sLabel)
        skp_list.append(sLabel5)
        skp_list.append(sLabel3)
        skp_list.append(manualButton)
        skp_list.append(rollButton)
        skp_list.append(skStatLabel)
        
        tp_list.append(backButton)
        f2p_list.append(backButton)

##
##        for item in sp_list:
##            self.remove_widget(item)

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
