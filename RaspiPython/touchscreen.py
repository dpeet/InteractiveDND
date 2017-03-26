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


class RootWidget(FloatLayout):
    def callback2(instance):
        print('The button <%s> is being pressed' % instance.text)


        
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        fp_list = list()
        sp_list = list()
        tp_list = list()
        f2p_list = list()
        pageNum = 1
        setting = 0 ## 0 = no preference
                    ## 1 = manual calculation
                    ## 2 = automatic calculation
        
        dmgData = ["Slashing (cut)",
                "Bludgeoning (smash)",
                "Piercing (pierce)",
                "Fire (burn)",
                "Cold (Freeze)",
                "Poison (Toxin)",
                "Acid (Corrosion)",
                "Psychic (Mental Durability)",
                "Necrotic (Decay)",
                "Lightning (Electrical)",
                "Thunder (Sound)",
                "Force (Force)"]

        saData = ["Ability Score Loss",
                "Alternate Form",
                "Antimagic",
                "Blindsight And Blindsense",
                "Breath Weapon",
                "Change Shape",
                "Charm and Compulsion",
                "Cold Immunity",
                "Constrict",
                "Damage Reduction",
                "Darkvision",
                "Death Attacks",
                "Disease",
                "Energy Drain And Negative Levels",
                "Etherealness",
                "Evasion And Improved Evasion",
                "Fast Healing",
                "Fear",
                "Fire Immunity",
                "Gaseous Form",
                "Gaze Attacks",
                "Improved Grab",
                "Incorporeality",
                "Invisibility",
                "Level Loss",
                "Low-Light Vision",
                "Manufactured Weapons",
                "Movement Modes",
                "Natural Weapons",
                "Nonabilities",
                "Paralysis",
                "Poison",
                "Polymorph",
                "Pounce",
                "Powerful Charge",
                "Psionics",
                "Rake",
                "Rays",
                "Regeneration",
                "Resistance To Energy",
                "Scent",
                "Sonic Attacks",
                "Spell Immunity",
                "Spell Resistance",
                "Spells",
                "Summon",
                "Swallow Whole",
                "Telepathy",
                "Trample",
                "Tremorsense",
                "Turn Resistance",
                "Vulnerability to Energy"]

        wpData = ["Club (B 1d4)",
                "Dagger (P 1d4)",
                "Greatclub (B 1d8)",
                "Handaxe (S 1d6)",
                "Javelin (P 1d6)",
                "Light hammer (B 1d4)",
                "Mace (B 1d6)",
                "Quarterstaff (B 1d6)",
                "Sickle (S 1d4)",
                "Spear (P 1d6)",
                "Unarmed strike (B 1)",
                "Crossbow, light (P 1d8)",
                "Dart (P 1d4)",
                "Shortbow (P 1d6)",
                "Sling (B 1d4)",
                "Battleaxe (S 1d8)",
                "Flail (B 1d8)",
                "Glaive (S 1d10)",
                "Greataxe (S 1d12)",
                "Greatsword (S 2d6)",
                "Halberd (S 1d10)",
                "Lance (P 1d12)",
                "Longsword (S 1d8)",
                "Maul (B 2d6)",
                "Morningstar (P 1d8)",
                "Pike (P 1d10)",
                "Rapier (P 1d8)",
                "Scimitar (S 1d6)",
                "Shortsword (P 1d6)",
                "Trident (P 1d6)",
                "War pick (P 1d8)",
                "Warhammer (B 1d8)",
                "Whip (S 1d4)",
                "Blowgun (P 1)",
                "Crossbow, hand (P 1d6)",
                "Crossbow, heavy (P 1d10)",
                "Longbow (P 1d8)",
                "Net"]


        wpData.sort()

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

        stData = ["Strength",
                "Dexterity",
                "Constitution",
                "Intelligence",
                "Wisdom",
                "Charisma"]

        initData = ["Tie Roll (1d20)"]

        
################################# First page widgets! ##############################################################################
    
        def callback2(instance, value):
            print('My button <%s> state is <%s>' % (instance, value))

        def nextPage(instance):
            self.remove_widget(initButton)

        def backPage(instance):
            global die
            global selected1
            global pageNum
            if pageNum == 2:
                for item in sp_list:
                    self.remove_widget(item)

                for item2 in fp_list:
                    self.add_widget(item2)
                
                die = 0
                dLabel.text = ('Select your Die!')
                changePageNum(1)
##                pageNum = 1
            elif pageNum == 3:
                for item in tp_list:
                    self.remove_widget(item)

                for item2 in sp_list:
                    self.add_widget(item2)
                changePageNum(2)
                print("herewego")
##                pageNum = 2
            elif pageNum == 4:
                for item in f2p_list:
                    self.remove_widget(item)

                for item2 in tp_list:
                    self.add_widget(item2)
                changePageNum(3)

        def diceSelection(instance):
            global die
            global selected1
            global pageNum
            if instance == manualDiceButton:
                print("%d page is selected" % pageNum)
                print("%d option is selected" % die)
                print(selected1)
                changePageNum(4)

            elif instance == autoDiceButton:
                print("%d page2 is selected" % pageNum)
                print("%d option is selected" % die)
                print(selected1)
                for item in tp_list:
                    self.remove_widget(item)

                for item2 in f2p_list:
                    self.add_widget(item2)
                changePageNum(4)

        def changePageNum(num):
            global pageNum
            pageNum = num

        def autoSelection(instance):
            lh = ""
            rh = ""
            if instance == oneButton:
                lh = instance.text
            elif instance == twoButton:
                lh = instance.text
            elif instance == threeButton:
                lh = instance.text
            elif instance == fourButton:
                lh = instance.text
            elif instance == fiveButton:
                lh = instance.text
            elif instance == d4Button:
                rh = instance.text
            elif instance == d6Button:
                rh = instance.text
            elif instance == d8Button:
                rh = instance.text
            elif instance == d10Button:
                rh = instance.text
            elif instance == d12Button:
                rh = instance.text
            elif instance == d20Button:
                rh = instance.text
            elif instance == cal2Button:
                mylist = totalLabel.text.split(" ")
                if mylist[0] != "?" and mylist[2] != "?":
                    totalValLabel.text = str(random.randint(int(mylist[0]), int(mylist[0]) * int(mylist[2])))
                
            if lh:
                lhs, rhs = totalLabel.text.split(" ", 1)
                totalLabel.text = "%s %s" % (lh, rhs)
            elif rh:
                lhs, rhs = totalLabel.text.split(" ", 1)
                totalLabel.text = "%s %s to Roll" % (lhs, rh)

                
            
        def dieSelect(instance):
            global die
            global selected1
            global pageNum
            flag = True
            if instance == initButton:
                dLabel.text = ('%s is selected!' % instance.text)
                data = [{'text': i, 'is_selected': False} for i in initData]
                sLabel2.text = 'Value: --'
                sLabel.text = 'Select your option'
                die = 1
            elif instance == stButton:
                dLabel.text = ('%s is selected!' % instance.text)
                data = [{'text': i, 'is_selected': False} for i in stData]
                sLabel2.text = 'Value: --'
                sLabel.text = 'Select your option'
                die = 2
            elif instance == wpButton:
                dLabel.text = ('%s is selected!' % instance.text)
                data = [{'text': i, 'is_selected': False} for i in wpData]
                sLabel2.text = 'Value: --'
                sLabel.text = 'Select your option'
                die = 3
            elif instance == skButton:
                dLabel.text = ('%s is selected!' % instance.text)
                data = [{'text': i, 'is_selected': False} for i in skData]
                sLabel2.text = 'Value: --'
                sLabel.text = 'Select your option'
                die = 4
            elif instance == dmgButton:
                dLabel.text = ('%s is selected!' % instance.text)
                data = [{'text': i, 'is_selected': False} for i in dmgData]
                sLabel2.text = 'Value: --'
                sLabel.text = 'Select your option'
                die = 5
            elif instance == saButton:
                dLabel.text = ('%s is selected!' % instance.text)
                data = [{'text': i, 'is_selected': False} for i in saData]
                sLabel2.text = 'Value: --'
                sLabel.text = 'Select your option'
                die = 6
            elif instance == calButton:
                flag = False
                selected1 = list_adapter.selection
                if not selected1:
                    sLabel.text = "Select One!"
                    sLabel.color = (1,0,0,1)
                else:
                    selectedItem = list_adapter.selection[0].text
                    sLabel.color = (0,0,0,1)
                    sLabel.text = selectedItem
                    ran = random.randint(1, 100)
                    sLabel2.text = ('Value: %d' % ran)

                    for item in sp_list:
                        self.remove_widget(item)

                    for item2 in tp_list:
                        self.add_widget(item2)
                    changePageNum(3)
                    print("here %d" % pageNum)

                    
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

        initButton = Button(
                    size_hint = (.2, .2),
                    background_normal = "./images/initiative.png",
                    pos_hint = {'center_x': .20, 'center_y': .6})

        initButton.bind(on_press=dieSelect)

        initLabel = Label(
                text='Initiative',
                color = (0,0,0,1),
                font_size='20sp',
                pos_hint = {'center_x': .2, 'center_y': .47})

        
        
        stButton = Button(
                    size_hint = (.2, .2),
                    background_normal = "./images/save throw.png",
                    pos_hint = {'center_x': .5, 'center_y': .6})

        stButton.bind(on_press=dieSelect)

        stLabel = Label(
                text='Saving Throw',
                color = (0,0,0,1),
                font_size='20sp',
                pos_hint = {'center_x': .5, 'center_y': .47})

        wpButton = Button(
                    size_hint = (.2, .2),
                    background_normal = "./images/weapon.png",
                    pos_hint = {'center_x': .8, 'center_y': .6})

        wpButton.bind(on_press=dieSelect)

        wpLabel = Label(
                text='Weapons',
                color = (0,0,0,1),
                font_size='20sp',
                pos_hint = {'center_x': .8, 'center_y': .47})

        skButton = Button(
                    size_hint = (.2, .2),
                    background_normal = "./images/skill.png",
                    pos_hint = {'center_x': .2, 'center_y': .30})

        skButton.bind(on_press=dieSelect)

        skLabel = Label(
                text='Skills',
                color = (0,0,0,1),
                font_size='20sp',
                pos_hint = {'center_x': .2, 'center_y': .17})

        dmgButton = Button(
                    size_hint = (.2, .2),
                    background_normal = "./images/damage.png",
                    pos_hint = {'center_x': .5, 'center_y': .30})

        dmgButton.bind(on_press=dieSelect)

        dmgLabel = Label(
                text='Damage',
                color = (0,0,0,1),
                font_size='20sp',
                pos_hint = {'center_x': .5, 'center_y': .17})

        saButton = Button(
                    size_hint = (.2, .2),
                    background_normal = "./images/specialAbil.png",
                    pos_hint = {'center_x': .8, 'center_y': .30})

        saButton.bind(on_press=dieSelect)

        saLabel = Label(
                text='Special Abilities',
                color = (0,0,0,1),
                font_size='20sp',
                pos_hint = {'center_x': .8, 'center_y': .17})

        tLabel = Label(
                text='Welcome to the Die Tower!',
                color = (0,0,0,1),
                font_size='40sp',
                pos_hint = {'center_x': .5, 'center_y': .85})
        self.add_widget(tLabel)

        dLabel = Label(
                text='Select your Option!',
                color = (0,0,0,1),
                font_size='25sp',
               pos_hint = {'center_x': .5, 'center_y': .75})

####################################################################################################################################


##        
##        btn1.bind(on_press=callback)
##        cb = CustomBtn()
##        cb.bind(pressed=self.btn_pressed)
##        self.add_widget(cb)


################################# Second page widgets! ##############################################################################

        backButton = Button(
                        text = 'Back',
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .85, 'center_y': .23})
        backButton.bind(on_press=backPage)

        calButton = Button(
                        text = "Calculate!",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .65, 'center_y': .23})
        calButton.bind(on_press=dieSelect)

        sLabel = Label(
                text='Select your option',
                color = (0,0,0,1),
                font_size='40sp',
                pos_hint = {'center_x': .72, 'center_y': .6})
        
        sLabel2 = Label(
                text='Value: --',
                color = (0,0,0,1),
                font_size='40sp',
                pos_hint = {'center_x': .72, 'center_y': .50})
        
        data = [{'text': i, 'is_selected': False} for i in wpData]

        args_converter = lambda row_index, rec: {'text': rec['text'],
                                                 'size_hint_x': 10,
                                                 'size_hint_y': None,
                                                 'selected_color': (1,0,0,1),
                                                 'deselected_color': (0,0,0,1),
                                                 'height': 45}
        
        list_adapter = ListAdapter(data=data,
                                    args_converter=args_converter,
                                    cls=ListItemButton,
                                    selection_mode='single',
                                    allow_empty_selection=True)


        list_view = ListView(adapter = list_adapter,
                             pos_hint = {'center_x': .3, 'center_y': .43},
                             size_hint = (0.4, 0.6))
        list_view.background_normal = (0,0,0,1)
##
##        list_adapter.bind(on_selection_change=self.selection_change)


        dImg1 = Image(source='./images/dice.png',
                     pos_hint = {'center_x': .15, 'center_y': .84},
                     size_hint = (0.08, 0.08))
        dImg2 = Image(source='./images/dice.png',
                     pos_hint = {'center_x': .85, 'center_y': .84},
                     size_hint = (0.08, 0.08))
        self.add_widget(dImg1)
        self.add_widget(dImg2)

################################# Third page widgets! ##############################################################################

        manualDiceButton = Button(
                        text = 'Manual',
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .25, 'center_y': .5})
        manualDiceButton.bind(on_press=diceSelection)

        autoDiceButton = Button(
                        text = 'AutoCal',
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .75, 'center_y': .5})
        autoDiceButton.bind(on_press=diceSelection)
        

################################# Forth page widgets! ##############################################################################

        diceNumLabel = Label(
                text='Number of Dice?',
                color = (0,0,0,1),
                font_size='30sp',
                pos_hint = {'center_x': .25, 'center_y': .7})

        yVal1 = 0.6
        oneButton = Button(
                        text = "1",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .16, 'center_y': yVal1})
        oneButton.bind(on_press=autoSelection)

        twoButton = Button(
                        text = "2",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .32, 'center_y': yVal1})
        twoButton.bind(on_press=autoSelection)

        threeButton = Button(
                        text = "3",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .48, 'center_y': yVal1})
        threeButton.bind(on_press=autoSelection)

        fourButton = Button(
                        text = "4",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .64, 'center_y': yVal1})
        fourButton.bind(on_press=autoSelection)

        fiveButton = Button(
                        text = "5",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .8, 'center_y': yVal1})
        fiveButton.bind(on_press=autoSelection)

##        sixButton = Button(
##                        text = "6",
##                        color = (0,0,0,1),
##                        size_hint = (.1, .1),
##                        pos_hint = {'center_x': .96, 'center_y': .7})
##        sixButton.bind(on_press=dieSelect)


        diceTypLabel = Label(
                text='Type of Dice?',
                color = (0,0,0,1),
                font_size='30sp',
                pos_hint = {'center_x': .22, 'center_y': .45})

##        diceTypLabel
        yVal2 = 0.35
        d4Button = Button(
                        text = "d 4",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .16, 'center_y': yVal2})
        d4Button.bind(on_press=autoSelection)

        d6Button = Button(
                        text = "d 6",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .288, 'center_y': yVal2})
        d6Button.bind(on_press=autoSelection)

        d8Button = Button(
                        text = "d 8",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .416, 'center_y': yVal2})
        d8Button.bind(on_press=autoSelection)

        d10Button = Button(
                        text = "d 10",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .544, 'center_y': yVal2})
        d10Button.bind(on_press=autoSelection)

        d12Button = Button(
                        text = "d 12",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .672, 'center_y': yVal2})
        d12Button.bind(on_press=autoSelection)

        d20Button = Button(
                        text = "d 20",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .8, 'center_y': yVal2})
        d20Button.bind(on_press=autoSelection)


        totalLabel = Label(
                text='? d ? to Roll',
                color = (0,0,0,1),
                font_size='40sp',
                pos_hint = {'center_x': .3, 'center_y': .2})

        cal2Button = Button(
                        text = "=",
                        color = (0,0,0,1),
                        size_hint = (.1, .1),
                        pos_hint = {'center_x': .5, 'center_y': .2})
        cal2Button.bind(on_press=autoSelection)
        
        totalValLabel = Label(
                text='??',
                color = (0,0,0,1),
                font_size='40sp',
                pos_hint = {'center_x': .6, 'center_y': .2})

        
        


        
####################################################################################################################################

        
        
        fp_list.append(initButton)
        fp_list.append(stButton)
        fp_list.append(dmgButton)
        fp_list.append(skButton)
        fp_list.append(saButton)
        fp_list.append(wpButton)
        fp_list.append(dLabel)
        fp_list.append(initLabel)
        fp_list.append(stLabel)
        fp_list.append(dmgLabel)
        fp_list.append(skLabel)
        fp_list.append(saLabel)
        fp_list.append(wpLabel)
        
        sp_list.append(backButton)
        sp_list.append(calButton)
        sp_list.append(list_view)
        sp_list.append(sLabel)
        sp_list.append(sLabel2)

        tp_list.append(manualDiceButton)
        tp_list.append(autoDiceButton)
        tp_list.append(backButton)

        
        f2p_list.append(diceNumLabel)
        f2p_list.append(diceTypLabel)
        f2p_list.append(oneButton)
        f2p_list.append(twoButton)
        f2p_list.append(threeButton)
        f2p_list.append(fourButton)
        f2p_list.append(fiveButton)
        f2p_list.append(totalLabel)
        f2p_list.append(d4Button)
        f2p_list.append(d6Button)
        f2p_list.append(d8Button)
        f2p_list.append(d10Button)
        f2p_list.append(d12Button)
        f2p_list.append(d20Button)
        f2p_list.append(backButton)
        f2p_list.append(totalValLabel)
        f2p_list.append(cal2Button)
        
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
