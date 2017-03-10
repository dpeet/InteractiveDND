from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.uix.label import Label
import random

class RootWidget(FloatLayout):
    def callback2(instance):
        print('The button <%s> is being pressed' % instance.text)


        
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        
        pageNum = 1


        
################################# First page widgets! ##############################################################################
    
        def callback2(instance, value):
            print('My button <%s> state is <%s>' % (instance, value))

        def nextPage(instance):
            self.remove_widget(d1Button)

        def backPage(instance):
            self.add_widget(d1Button)
            
        def dieSelect(instance):
            global die
            if instance == d1Button:
                dLabel.text = ('%s is selected!' % instance.text)
                die = 1
            elif instance == d2Button:
                dLabel.text = ('%s is selected!' % instance.text)
                die = 2
            elif instance == d3Button:
                dLabel.text = ('%s is selected!' % instance.text)
                die = 3
            elif instance == calButton:
                if dLabel.text == 'Please select a die first!' or dLabel.text == 'Select your Die!':
                    dLabel.text = 'Please select a die first!'
                else:

##                    self.remove_widget(d1Button)
##                    self.remove_widget(d2Button)
##                    self.remove_widget(d3Button)
##                    self.remove_widget(dLabel)
                    if die == 1:
                        ran = random.randint(1, 10)
                    elif die == 2:
                        ran = random.randint(1, 100)
                    elif die == 3:
                        ran = random.randint(1, 1000)
                    dLabel.text = ('Your score is %d' % ran)

                    
            elif instance == nxtButton:
                print('%d is current die' % die)
            else:
                print('what is this?')

        d1Button = Button(
                    text = "Die 1",
                    size_hint = (.1, .1),
                    pos_hint = {'center_x': .25, 'center_y': .5})

        d1Button.bind(on_press=dieSelect)
        self.add_widget(d1Button)

        d2Button = Button(
                    text = "Die 2",
                    size_hint = (.1, .1),
                    pos_hint = {'center_x': .5, 'center_y': .5})

        d2Button.bind(on_press=dieSelect)
        self.add_widget(d2Button)

        d3Button = Button(
                    text = "Die 3",
                    size_hint = (.1, .1),
                    pos_hint = {'center_x': .75, 'center_y': .5})

        d3Button.bind(on_press=dieSelect)
        self.add_widget(d3Button)

        calButton = Button(
                    text = "Calculate!",
                    size_hint = (.1, .1),
                    pos_hint = {'center_x': .5, 'center_y': .25})

        calButton.bind(on_press=dieSelect)
        self.add_widget(calButton)

        tLabel = Label(
                text='Welcome to the Die Tower!',
                color = (0,0,0,1),
                font_size='30sp',
                pos_hint = {'center_x': 0.25, 'center_y': .9})
        self.add_widget(tLabel)

        dLabel = Label(
                text='Select your Die!',
                color = (0,0,0,1),
                font_size='20sp',
                pos_hint = {'center_x': 0.5, 'center_y': .7})
        self.add_widget(dLabel)

############################################################################################################################


##        
##        btn1.bind(on_press=callback)
##        cb = CustomBtn()
##        cb.bind(pressed=self.btn_pressed)
##        self.add_widget(cb)
        
    
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
        root.bind(size=self._update_rect, pos = self._update_rect)

        with root.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(size = root.size, pos = root.pos)
        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ == '__main__':
    MainApp().run()
