from kivymd.uix.screen import Screen
from kivymd.app import MDApp

class AboutScreen(Screen):
	def go_back(self):
		app = MDApp.get_running_app()

		app.root.ids.screen_manager.current = 'main_screen'