from kivymd.app import MDApp
from Imports.Packages import *
import json

try:
	import requests
except:
	import requests


from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty

from datetime import datetime, timedelta
from Lib.GPS.GpsHelper.GpsHelper import GpsHelper

class mainApp(MDApp):
	dropdown_date = ObjectProperty()
	dropdown_condition = ObjectProperty()

	def on_start(self):
		# Initialise GPS:
		GpsHelper().run()


		# cretate dropdown 
		self.dropdown_date = MDDropdownMenu(width_mult = 3)
		# Get today's date 
		presentday = datetime.now()
		

		# add items to drop date:
		self.dropdown_date.items.append(
			{"viewclass": "MDMenuItem",
			"text": "{}".format(presentday.strftime('%Y-%m-%d')),
			"callback": self.option_callback}
			)
		# adding Tomorrrow's dates :
		for i in range(1,6):
			# Tomorrow date :
			tomorrow = presentday + timedelta(i)
			

			self.dropdown_date.items.append(
				{"viewclass": "MDMenuItem",
				"text": "{}".format(tomorrow.strftime('%Y-%m-%d')),
				"callback": self.option_callback}
				)

		#create other dropmenu :
		self.dropdown_condition = MDDropdownMenu(width_mult=3)

		condition_item = ['Tempreature', 'Tempreature Feel', 'Min Tempreature', 'Max Tempreature', 'Humidity',
						'Pressure', 'Clouds', 'Wind SpeSed', 'ID','Icon']

		for i in range(len(condition_item)):

			self.dropdown_condition.items.append(
				{"viewclass": "MDMenuItem",
				"text": "{}".format(condition_item[i]),
				"callback": self.condition_callback}
				)

		# Check in Profile Database : 
		try:
			connect = sqlite3.connect('Lib\\site_packages\\Profile\\data\\data.db')
			cursor = connect.cursor()

			# Fentch Name :
			cursor.execute("SELECT name FROM todo")
			cols = cursor.fetchall()
			user_name = cols[0][0]
			print(user_name)
			app = MDApp.get_running_app()
			name = app.root.ids.content_navdrawer.ids.user_name
			name.text = 'Welcome, {0}'.format(user_name)

			# Fentch Mail name:
			cursor.execute("SELECT email FROM todo")
			mail = cursor.fetchall()
			user_mail = mail[0][0]
			gmail = app.root.ids.content_navdrawer.ids.user_gmail
			gmail.text = 'Mail: {0}'.format(user_mail)
			print(user_mail)
		except:
			pass



	def option_callback(self, text_of_the_option):
		
		bar = BarView()
		do = bar.dates(text_of_the_option)

	def condition_callback(self, text_of_the_option):
		
		bar = BarView()
		do = bar.condition(text_of_the_option)


	def build(self):
		pass

	data = {
        'home-city': 'Add City',
        'crosshairs-gps': 'Use GPS',
        
    }


	def callback(self, instance):
		self.task = instance.icon
		task = instance.icon
		#print(self.root.ids['home_screen'].ids)
		if self.task == 'home-city':

			self.dialog = MDDialog(title ='Enter City :', size_hint_y= None, padding=10, height='90dp',
										type="custom",
										content_cls=Content(),
							buttons=[
								MDRaisedButton(text="CANCEL", on_release= self.closeDialog),
								MDRaisedButton(text="OK", on_release= self.auth_city)
								]
								)

			
			self.dialog.set_normal_height()
			self.dialog.open()



			
		else :
			app = MDApp.get_running_app()
			app.root.ids.screen_manager.current = 'map_screen'

	def closeDialog(self, inst):
		self.dialog.dismiss()

	def auth_city(self, inst):
		self.auth = 1
		self.add_city(inst)

	def map_city(self, inst):
		self.map_input = inst
		print('map', self.map_input)
		
		self.fentch(inst)
		self.map_check_city()

	


	def add_city(self, inst):
		#print(self.root.ids['Content_dialog'].ids.city_entered.text)
		if self.auth == 1:
			for obj in self.dialog.content_cls.children:
				if isinstance(obj, MDTextField):
					self.input = obj.text
					self.input_text = self.root.ids['Content_dialog'].ids['city_entered']
					self.input_text.text = self.input
					self.auth = 0
		

		inst = self.input
		self.fentch(self, inst)
		self.check_city()

	def check_city(self):

		if self.process == 'Go':
			print('1')
			weather = self.weather
			print('2')
			try:
				if weather['cod'] == '404':
					print('1')
					toast("City not Found: 404 Error")
				else:
					
					self.add_city_to_json()
					self.dialog.dismiss()
			except:
				print('error in Go')
		else:
			toast('Please Connect to Internet')

	def add_city_to_json(self):
		self.cities = Cities(name = 'cities')

		self.load_file()

	def load_file(self):
		
		with open('Lib\\site_packages\\City\\Data\\cities.json') as fd:
			data = json.load(fd)
		self.cities.data = data

		if self.input == '':
			toast("Enter Something")
		else :
			ids = len(self.cities.data)
			self.cities.data.append({'name': '{0}'.format(self.input), 'id':'{}'.format(ids) ,'content': ''})
			print(self.cities.data)
			self.save_file()


	def fentch(self, inst, *args):
		url = URL()
		value = url.get_url()
		ID = url.get_id()
		try:
			city = args[0]
		except:
			print('map')
			print(inst)
			city= inst
		print('fentch', city, inst, *args)

		try :
			weather_key = ID
			url = value
			params = {'APPID' : weather_key, 'q': city, 'units':'metric'}
			response = requests.get(url, params=params)
			weather=response.json()
			self.weather = weather
			
			self.process = 'Go'
			print(self.process)
		except:
			
			self.process = 'Stop'
			print(self.process)

	def save_file(self):
		with open('Lib\\site_packages\\City\\Data\\cities.json', 'w') as fd:
			json.dump(self.cities.data, fd, indent=3)
		
		city_screen = CityScreen()
		add = city_screen.load_cities()
		
		self.root.ids.screen_manager.current = 'city_screen'

	# Save file Form Map View: 
	def map_check_city(self):

		if self.process == 'Go':
			print('1')
			weather = self.weather
			print('2')
			try:
				if weather['cod'] == '404':
					print('3')
					sm = MapDisplay()
					msg = sm.message()
					print('4')
				else:
					print('5')
					self.map_add_city_to_json()
					print('6')
					#self.dialog.dismiss()
			except:
				print('error in Go')
		else:
			toast('Please Connect to Internet')

	def map_add_city_to_json(self):
		self.cities = Cities(name = 'cities')

		self.map_load_file()

	def map_load_file(self):
		
		with open('Lib\\site_packages\\City\\Data\\cities.json') as fd:
			data = json.load(fd)
		self.cities.data = data

		ids = len(self.cities.data)
		self.cities.data.append({'name': '{0}'.format(self.map_input), 'id':'{}'.format(ids) ,'content': ''})
		print(self.cities.data)
		self.map_save_file()

	def map_save_file(self):
		with open('Lib\\site_packages\\City\\Data\\cities.json', 'w') as fd:
			json.dump(self.cities.data, fd, indent=3)
		
		city_screen = CityScreen()
		add = city_screen.load_cities()
		
		self.root.ids.screen_manager.current = 'city_screen'





	

if __name__ == '__main__':
	#Window.fullscreen = 'auto'
	mainApp().run()