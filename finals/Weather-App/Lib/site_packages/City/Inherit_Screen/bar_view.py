from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivymd.uix.label import MDLabel

import requests

from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

# For Plotting :
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt2
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg, FigureCanvas


from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage

# Histo Plot:
import matplotlib
matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')
from matplotlib.figure import Figure
from numpy import arange, sin, pi
from kivy.app import App

import numpy as np
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvas,\
                                                NavigationToolbar2Kivy
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from matplotlib.transforms import Bbox
from kivy.uix.button import Button
from kivy.graphics import Color, Line, Rectangle

import matplotlib.pyplot as plt

class CustomDropDown(Screen):
    pass




class BarView(Screen):



	def go_back(self):
		app = MDApp.get_running_app()
		self.app = app
		screen = app.root.ids['bar_view'].ids['corousel_view']
		screen.clear_widgets()


		screen2 = app.root.ids['bar_view'].ids['next_day_view']
		screen2.clear_widgets()

		

		

		app.root.ids.screen_manager.current = 'City_View'
	
	def dates(self, value):
		print(value)

	def condition(self, value):
		print(value)
		self.plot_condition = value

		

	def draw_line_plot(self, plot_this):
		print(plot_this)
		plot_items = {
						1 : self.temp , 2 : self.temp_feel, 3 : self.temp_min, 
						4 : self.temp_max , 5 : self.humidity, 6 : self.pressure, 
						7 : self.cloud, 8 : self.wind_speed , 9 : self.weather_id, 
						10 : self.weather_icon
					}
		
		app = MDApp.get_running_app()
		screen = app.root.ids['bar_view'].ids['corousel_view'] 

		self.carousel = Carousel(direction='right')

		
		# Histo Graph for self.temp

		# Fentching Date :
		date = self.date_data
		
		# Dates which are needed to plot:
		plot_date = []
		for i in range(len(date)):
			if date[i] not in plot_date:
				plot_date.append(date[i])

		print(plot_date)
		
		# 1st Date :
		current_date_plot = 0
		for i in date:
			if i == plot_date[0]:
				current_date_plot = current_date_plot + 1
		print(current_date_plot)

		# No of bars for 1st Date :
		N = int(current_date_plot)

		# x-axis time Plot :
		time = self.time_data
		time_plot = []
		for i in range(0, current_date_plot):
			time_plot.append(time[i])
		#print(time)

		tm = { '00:00:00': 00 , '03:00:00': 3 , '06:00:00': 6, '09:00:00': 9 , '12:00:00': 12 ,
						 '15:00:00': 15 , '18:00:00': 18 , '21:00:00': 21}

		x_Std = []

		for j in time_plot:
			x_Std.append(tm[j])
		# ------------------------------------------



		x_data = []

		db = [self.temp, self.temp_feel, self.temp_min, self.temp_max, self.humidity, 
					self.pressure, self.cloud, self.wind_speed]
		color = ['red', 'yellow', 'orange', 'magenta', 'blue', 'pink',
					'green', 'purple']
		title = ['Tempreature', 'Tempreature feels_like', 'Min. Temp', 'Max Temp.', 'Humidity',
						'Pressure', 'Clouds', 'Wind Speed']



		for i in range(0,len(db)):
			temp = db[i]
			print('temp ', temp)


			for j in range(0 , current_date_plot):
				x_data.append(temp[j])
			print('x_data :', x_data)

			#x_Std = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21, 22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,39,40)
			ind = np.arange(N)

			width = 0.35        # the width of the bars
			fig, ax = plt.subplots()

			rects1 = ax.bar(ind , x_data , width, color='{}'.format(color[i]), yerr=x_Std) # , yerr=x_Std

			ax.set_ylabel('params')
			ax.set_title('{0} v/s Time'.format(title[i]))
			ax.set_xticks(ind)
			ax.set_xticklabels(x_Std)
			ax.legend(['{0}'.format(title[i])], loc="upper right")
			canvas = fig.canvas
			fl = BoxLayout(orientation="vertical")
			fl.add_widget(canvas)
			self.carousel.add_widget(fl)
			print('x_data was ', x_data)


			for i in range(len(x_data)):
				del x_data[0]
			print('x_data is ', x_data)


		lb2 = MDLabel(text= 'label2')
		self.carousel.add_widget(lb2)

		screen.add_widget(self.carousel)




		# Next Date :

		color1 = ['magenta', 'blue','red',   'pink', 'green',
										'yellow', 'orange', 'purple']
		title1 = ['Tempreature', 'Tempreature feels_like', 'Min. Temp', 'Max Temp.', 'Humidity',
						'Pressure', 'Clouds', 'Wind Speed']


		screen2 = app.root.ids['bar_view'].ids['next_day_view']
		carousel1 = Carousel(direction='right')

		start = current_date_plot

		ini = 0
		for i in date:
			if i == plot_date[1]:
				ini = ini + 1
		print(ini)

		current_date_plot1 = int(ini)
		print('current_date_plot1' ,current_date_plot1)
		x_data = []


		# X-Axis :
		time_plot = []

		time = self.time_data
		for i in range(start , current_date_plot1+start):
			time_plot.append(time[i])
		#print(time)
		print(time_plot)
		tm = { '00:00:00': 00 , '03:00:00': 3 , '06:00:00': 6, '09:00:00': 9 , '12:00:00': 12 ,
						 '15:00:00': 15 , '18:00:00': 18 , '21:00:00': 21}

		x_Std = []

		for j in time_plot:
			x_Std.append(tm[j])
		

		# parameters :
		N = int(current_date_plot1)

		for i in range(len(db)):
			print(title1[i])

			temp = db[i]
			print(temp)
			j = i 

			for i in range(start  , current_date_plot1+start):
				x_data.append(temp[i])
			print(x_data)

			ind = np.arange(N)
			width = 0.35        # the width of the bars

			fig, ax = plt.subplots()

			rects2 = ax.bar(ind , x_data , width, color='{}'.format(color1[j]), yerr=x_Std) # , yerr=x_Std

			ax.set_ylabel('params')
			ax.set_title('{} v/s Time'.format(title1[j]))
			ax.set_xticks(ind)
			ax.set_xticklabels(x_Std)
			ax.legend(['{}'.format(title1[j])], loc="upper left")
			canvas2 = fig.canvas

			f2 = BoxLayout(orientation="vertical")
			f2.add_widget(canvas2)
			carousel1.add_widget(f2)
			print(i)
			print(len(db))

			

			for i in range(len(x_data)):
				del x_data[0]
			print('x_data is ', x_data)

		for i in range(len(title1)):
			print(title1[i])
		print(len(title1))

		screen2.add_widget(carousel1)

		
		
		return screen, screen2

	def swipe_right(self):
		print('Pending')

	def swipe_left(self):
		print(self.ids)

		

	def add_it(self):
		

		lb= MDLabel(text = 'done')
		screen.add_widget(lb)
		return screen
		print('added')

		

	


	def extract_data(self):

		# Fentch Request :
		self.fentch_request()
		
		# plot initial graph:
		value = 'Tempreature'
		self.draw_line_plot(value)
	

	def fentch_request(self):
		# Getting Data:
		app = MDApp.get_running_app()
		self.app = app
		self.my_city = app.root.ids['City_View'].ids['city_text'].text

		bar_city = app.root.ids['bar_view'].ids['bar_city']
		bar_city.text = self.my_city


		city = self.my_city
		print(city)
		try:
			weather_key = ''# Visit to openweathermapapi.com and paste the key and url here...
			url = ''
			params = {'APPID' : weather_key, 'q': city, 'units':'metric'}
			response = requests.get(url, params=params)
			weather=response.json()
			self.weather = weather

			self.get_list()

			

		except:
			print("error")



	def get_list(self):

		weather = self.weather
		raw = []
		raw_data =[]

		# Main-list :
		temp = []
		temp_feel = []
		temp_min = []
		temp_max = []
		humidity = []
		pressure = []

		# Weather Ids :
		weather_id = []
		weather_icon = []

		# cloud :
		cloud = []

		# Speed :
		wind_speed = []

		for data in range(len(weather['list'])):
			# Getting date from weather.json :
			#print('{0} - {1}'.format(data,weather['list'][data]['dt_txt']))
			raw.append(weather['list'][data]['dt_txt'])

			# From Main :
			temp.append(weather['list'][data]['main']['temp'])
			temp_feel.append(weather['list'][data]['main']['feels_like'])
			temp_min.append(weather['list'][data]['main']['temp_min'])
			temp_max.append(weather['list'][data]['main']['temp_max'])
			humidity.append(weather['list'][data]['main']['humidity'])
			pressure.append(weather['list'][data]['main']['pressure'])

			# Weather id: 
			weather_id.append(weather['list'][data]['weather'][0]['id'])
			weather_icon.append(weather['list'][data]['weather'][0]['icon'])

			# Cloud :
			cloud.append(weather['list'][data]['clouds']['all'])

			# wind_speed :
			wind_speed.append(weather['list'][data]['wind']['speed'])



		# Split date and time :
		for i in raw:
			raw_data.append(i.split())
		#print(raw_data)


		# extract date and time :
		time_data = []
		date_data = []
		for i in raw_data:
			for j in i:
				if len(j) == 8:
					#print(j)
					time_data.append(j)
				else :
					date_data.append(j)
		#print(time_data)
		#print(date_data)
		#print(len(wind_speed))


		self.time_data = time_data 
		self.date_data = date_data 
		self.temp = temp
		self.temp_feel = temp_feel
		self.temp_min = temp_min 
		self.temp_max = temp_max 
		self.humidity = humidity 
		self.pressure = pressure 
		self.weather_id = weather_id 
		self.weather_icon = weather_icon 
		self.cloud = cloud 
		self.wind_speed = wind_speed 
		


	