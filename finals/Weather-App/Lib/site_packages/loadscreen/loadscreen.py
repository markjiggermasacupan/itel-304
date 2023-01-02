from kivymd.uix.progressbar import MDProgressBar
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
import time

from kivy.clock import Clock 

class LoadScreen(Screen):
	def __init__(self, **kwargs):
		super().__init__()
		print('in it')
		
		self.ids.pd.value = 0
		def next(dt):
			if self.ids.pd.value>= 100:
				return False
			self.ids.pd.value += 1
			
			if self.ids.pd.value>=5 and self.ids.pd.value <=20:
				self.ids.hint_text.text = 'Welcome to WeatherAPI'
				self.ids.label.text = 'Building Cache: {}%'.format(self.ids.pd.value)

			if self.ids.pd.value>=21 and self.ids.pd.value <=35:
				self.ids.hint_text.text = 'Get Weather Updates of  city'
				self.ids.bg_image.source = 'Resorces\\weather_iconPNG1.png'
				self.ids.label.text = 'Checking Version: {}%'.format(self.ids.pd.value)
			
			if self.ids.pd.value>=36 and self.ids.pd.value <=50:
				self.ids.hint_text.text = 'Know current Climate Conditions'
				self.ids.bg_image.source = 'Resorces\\weather_icon4.jpg'
				self.ids.label.text = 'Checking Modules: {}%'.format(self.ids.pd.value)

			if self.ids.pd.value>=51 and self.ids.pd.value <=60:
				self.ids.hint_text.text = 'with City weather details'
				#self.ids.bg_image.source = 'Resorces\\weather_icon3.jpg'
				self.ids.label.text = 'Creating Env: {}%'.format(self.ids.pd.value)

			if self.ids.pd.value>=61 and self.ids.pd.value <= 73:
				self.ids.hint_text.text = 'Features awaiting for You !'
				self.ids.label.text = 'Dependencies: {}%'.format(self.ids.pd.value)

			if self.ids.pd.value>=74 and self.ids.pd.value <=86:
				self.ids.hint_text.text = '   Unable GPS Mode'
				self.ids.bg_image.source = 'Resorces\\gps_icon.jpg'
				self.ids.label.text = 'Initializing... {}%'.format(self.ids.pd.value)

			if self.ids.pd.value>=87 and self.ids.pd.value <=95:
				self.ids.hint_text.text = '  Enjoy the Functionality !'
				self.ids.label.text = 'Completing... {}%'.format(self.ids.pd.value)

			if self.ids.pd.value>=95 and self.ids.pd.value <= 100:
				self.ids.label.text = 'Hold On... {}%'.format(self.ids.pd.value)

				if self.ids.pd.value == 100:
					print('completed')
					app = MDApp.get_running_app()
					app.root.ids.screen_manager.current = 'main_screen'
				
	
		Clock.schedule_interval(next, 0.04)

		
		return 