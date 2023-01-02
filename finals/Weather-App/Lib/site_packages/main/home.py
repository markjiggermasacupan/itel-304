from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp


# for BarLoad:
from Lib.site_packages.City.Inherit_Screen.barload import AnimRect
class Content(Screen):
    pass


class MainScreen(Screen):
	def city_screen(self):
		app = MDApp.get_running_app()

		app.root.ids.screen_manager.current = 'city_screen'

	def mapview(self):
		app = MDApp.get_running_app()
		app.root.ids.screen_manager.current = 'map_screen'

	


	
	