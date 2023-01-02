from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition,FadeTransition
from kivymd.uix.dialog import MDDialog
from kivy.clock import Clock
from kivymd.app import MDApp
from Lib.site_packages.main.home import Content
# Necessary :
from Lib.site_packages.City.Inherit_Screen.CityView import CityView

# Required
from kivy.properties import ListProperty, StringProperty, \
        NumericProperty, BooleanProperty, AliasProperty
import json
from os.path import join
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from Lib.site_packages.City.Inherit_Screen.CityView import CityView
from kivymd.toast import toast



class NoteListItem(BoxLayout):
	city_content = StringProperty()
	city_title = StringProperty()
	city_index = NumericProperty()

	def open_city(self, value):
		app = MDApp.get_running_app()
		# Created a back-up for name
		app.root.ids['city_screen'].ids['note_list_item_id'].ids['citytitle'].text = value

		# giving CityView screen a city name
		self.city_label =app.root.ids['City_View'].ids['city_text']
		self.city_label.text = value

		cities = CityView()
		city = cities.fentch()
		app.root.ids.screen_manager.current = 'City_View'

	def delete(self, delete_this):
		print('Deleting This list :', delete_this)

		with open('Lib\\site_packages\\City\\Data\\cities.json') as f:
			obj = json.load(f)
		self.obj = obj


		for i in range(len(obj)):
			if obj[i]["name"] == delete_this :
				print(obj[i])
				obj.pop(i)
				print('deleted')
				break
		open('C:\\Users\\kiran\\Desktop\\Weather\\Lib\\site_packages\\City\\Data\\cities.json', "w").write(
			json.dumps(obj, indent=4) )
		print('Saved !')
		self.show_new_file()

	def show_new_file(self):
		city = CityScreen()
		self.load = city.load_cities()








class Cities(Screen):
	data = ListProperty()

	def _get_data_for_widgets(self):
		return [{
			'city_index': index,
			'city_title': item['name'],
			'city_id' : item['id'],
			'city_content' : item['content']

				}

			for index, item in enumerate(self.data)]


	data_for_widgets = AliasProperty(_get_data_for_widgets, bind=['data'])





class CityScreen(Screen):

	def go_back(self):
		app = MDApp.get_running_app()

		app.root.ids.screen_manager.current = 'main_screen'

	def check1(self):
		app = MDApp.get_running_app()
		self.app = app
		self.city_entered = app.root.ids['Content_dialog'].ids.city_entered.text
		print('tr', self.city_entered)

	def __init__(self, **kwargs):
		super().__init__()
			
		#self.load_cities()
		Clock.schedule_once(self.screen_label_name, 0)

	def screen_label_name(self, *args):
		self.load_cities()
		
		

		

	def load_cities(self):
		self.cities = Cities(name = 'cities')
		
		self.load_json()

		app = MDApp.get_running_app()

		screen = app.root.ids['city_screen'].ids['city_list']
		
		screen.add_widget(self.cities)
		return screen
		
	
	def load_json(self):
		try :
			with open('Lib\\site_packages\\City\\Data\\cities.json', 'r') as fd:
				data = json.load(fd)
			self.cities.data = data
		except: 
			data = []

			with open('Lib\\site_packages\\City\\Data\\cities.json', 'w') as fd:
				json.dump(data, fd, indent=3)
	def check(self):
		app = MDApp.get_running_app()
		print(app.root.ids['city_screen'].ids['note_list_item_id'].ids['citytitle'].text)

	def refresh(self):
		
		toast('Refreshing ...')


		
		

