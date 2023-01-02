from kivymd.uix.screen import Screen

from kivy.animation import Animation
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.widget import Widget
from kivy.core.window import Window
import time
class BarLoad(Screen):
	pass



class AnimRect(Widget): 
    velocity = ListProperty([10, 15]) 
  
    def __init__(self, **kwargs): 
        super(AnimRect, self).__init__(**kwargs)
        self.time = 0 
        Clock.schedule_interval(self.update, 1 / 60.) 
  
    def update(self, *args): 
        self.x += self.velocity[0]
        timer = 0
        if self.time < 20:
            if self.x < 0 or (self.x) > Window.width:
                self.time = timer + 1
                #print(self.time) 
                self.velocity[0] *= -1
            
    def count_timer(self):
        print('init')
        
        for timer in range(1,21):
            print(timer)
            if timer < 10:
                time.sleep(1)
            else:
                print('call')
        
  

