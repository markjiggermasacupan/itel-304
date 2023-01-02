from kivy.properties import ListProperty, StringProperty, \
        NumericProperty, BooleanProperty, AliasProperty
import json
from os.path import join
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivymd.uix.screen import Screen
from kivymd.app import MDApp
import requests
from kivymd.toast import toast
from Lib.site_packages.City.Inherit_Screen.bar_view import BarView

# for Data:
from Lib.site_packages.City.Inherit_Screen.bar_view import BarView


class CityView_content(Screen):
	def call_data_for_bar(self):
		barview = BarView()
		data = barview.extract_data()
		

class Cities_inhert(Screen):
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


class CityView(Screen):
	

	city_content = StringProperty()
	city_title = StringProperty()
	city_index = NumericProperty()

	

	def go_back(self):
		app = MDApp.get_running_app()
		self.app = app

		app.root.ids.screen_manager.current = 'city_screen'

	def __init__(self, **kwargs):
		super(CityView, self).__init__(**kwargs)
		Clock.schedule_once(self.screen_label_name, 0)

	def screen_label_name(self, *args):
		
		pass

	def fentch(self):
		try:
		
			app = MDApp.get_running_app()
			self.city_label = app.root.ids['City_View'].ids['city_text']
			city = self.city_label.text

			weather_key = '' # Visit to openweathermapapi.com and paste the key and url here...
			url = ''
			params = {'APPID' : weather_key, 'q': city, 'units':'metric'}
			response = requests.get(url, params=params)
			weather=response.json()
			self.weather = weather
			
			self.access()
			self.load_file()

			
			#self.save_again()
		except:
			app = MDApp.get_running_app()
			app.root.ids.screen_manager.current = 'city_screen'
			toast('You are not Connected to Internet')


	def load_file(self):
		self.cities = Cities_inhert(name = 'cities')
		with open('Lib\\site_packages\\City\\Data\\cities.json') as fd:
			self.data = json.load(fd)
		self.cities.data = self.data


		app = MDApp.get_running_app()
		self.city_label = app.root.ids['City_View'].ids['city_text']
		city = self.city_label.text
		
		for i in self.data:
			if i['name'] == city:
				print(i)

				self.save_again(i)

	def save_again(self, i):
		try:
			i['content'] = 'Country Name :{0}, City-cod: {1},  city-id: {2}, visibility: {3}, timezone : {4}, GMT time: {5}, sunrise : {6} , Sunset : {7}, Tempreature : {8}, Tempreature_feel_like : {9}, Pressure : {10}, Humidity :{11}, Min Temp: {12}, Max Temp: {13}, Sea Level : {14} , Ground Level : {15}, Weather Description : {16}, Current Weather: {17}, Longitude : {18}, latitude : {19}, Wind-Speed : {20}, Wind-Direction : {21}, past_rain : {22}, cloudiness : {23}, Weather-Code : {24}, weather-icon : {25}'.format(self.country_name.text, self.city_cod.text, self.city_id.text, self.visibility.text, self.timezone.text, self.GMT_time.text, self.sunrise.text, self.sunset.text, self.tempreature.text, self.tempreature_feel.text, self.pressure.text, self.humidity.text, self.min_temp.text, self.max_temp.text, self.sea_level.text, self.grnd_level.text, self.weather_desp.text, self.current_weather.text, self.longitude.text, self.latitude.text, self.wind_speed.text, self.wind_direction.text, self.past_rain.text, self.cloudiness.text, self.weather_cod.text, self.icon_is.icon)


			with open('Lib\\site_packages\\City\\Data\\cities.json', 'w') as fd:
				json.dump(self.cities.data, fd, indent=3)
		except:
			print('Error')


	

	def access(self):

		weather = self.weather
		print(weather)
		app = MDApp.get_running_app()

		self.labels = app.root.ids['City_View'].ids['city_content']
		
		try:
			#print("City Id : ",weather['id'])
			self.country_name = self.labels.ids['country_id']
			value = weather['sys']['country']
			self.country_name.text = value

			print(self.country_name.text)
			
		except:
			self.country_name = self.labels.ids['country_id']
			self.country_name.text = 'No Data'

		try:
			self.city_cod = self.labels.ids['city_code']

			if weather['cod'] != '404':
				self.city_cod.text = str(weather['cod'])
			else :
				self.city_cod.text = 'No Data'

		except:
			self.city_cod = self.labels.ids['city_code']
			self.city_cod.text = weather['cod']
			

		try:
			self.city_id = self.labels.ids['city_id']
			self.city_id.text = str(weather['id'])
		except:
			self.city_id = self.labels.ids['city_id']
			self.city_id.text = 'No Data'


		try:
			self.visibility = self.labels.ids['visibility']
			self.visibility.text = '{} m'.format(str(weather['visibility1']))
		except:
			self.visibility = self.labels.ids['visibility']
			self.visibility.text = 'No Data'

		try:
			self.timezone = self.labels.ids['timezone']
			self.timezone.text = '{} sec (UTC)'.format(str(weather['timezone']))
		except:
			self.timezone = self.labels.ids['timezone']
			self.timezone.text = 'No Data'

		try:
			self.GMT_time = self.labels.ids['GMT']
			self.GMT_time.text = '{} UTC'.format(str(weather['dt']))
		except:
			self.GMT_time = self.labels.ids['GMT']
			self.GMT_time.text = 'No Data'

		try :
			self.sunrise = self.labels.ids['sunrise']
			self.sunrise.text = '{} UTC'.format(str(weather['sys']['sunrise']))

			self.sunset = self.labels.ids['sunset']
			self.sunset.text = '{} UTC'.format(str(weather['sys']['sunrise']))
		except:
			self.sunrise = self.labels.ids['sunrise']
			self.sunrise.text = 'No Data'

			self.sunset = self.labels.ids['sunset']
			self.sunset.text = 'No Data'

		try :
			self.tempreature = self.labels.ids['tempreature']
			self.tempreature.text = '{} °C'.format(str(weather['main']['temp']))
		except:
			self.tempreature = self.labels.ids['tempreature']
			self.tempreature.text = 'No Data'

		try :
			self.tempreature_feel = self.labels.ids['tempreature_feel_like']
			self.tempreature_feel.text = '{} °C'.format(str(weather['main']['feels_like']))
		except:
			self.tempreature_feel = self.labels.ids['tempreature_feel_like']
			self.tempreature_feel.text = 'No Data'

		try:
			self.pressure = self.labels.ids['pressure']
			self.pressure.text = '{} hPa'.format(str(weather['main']['pressure']))
		except:
			self.pressure = self.labels.ids['pressure']
			self.pressure.text = 'No Data'

		try:
			self.humidity = self.labels.ids['humidity']
			self.humidity.text = '{} %'.format(str(weather['main']['humidity']))
		except:
			self.humidity = self.labels.ids['humidity']
			self.humidity.text = 'No Data'

		try:
			self.min_temp = self.labels.ids['min_temp']
			self.min_temp.text = '{} °C'.format(str(weather['main']['temp_min']))

			self.max_temp = self.labels.ids['max_temp']
			self.max_temp.text = '{} °C'.format(str(weather['main']['temp_max']))
		except:
			self.min_temp = self.labels.ids['min_temp']
			self.min_temp.text ='No Data'

			self.max_temp = self.labels.ids['max_temp']
			self.max_temp.text = 'No Data'

		try:
			self.sea_level = self.labels.ids['sea_level']
			self.sea_level.text = '{} hPa'.format(str(weather['main']['sea_level']))
		except:
			self.sea_level = self.labels.ids['sea_level']
			self.sea_level.text = 'No Data'

		try:
			self.grnd_level = self.labels.ids['grnd_level']
			self.grnd_level.text = '{} hPa'.format(str(weather['main']['grnd_level']))
		except:
			self.grnd_level = self.labels.ids['grnd_level']
			self.grnd_level.text = 'No Data'

		try :
			self.weather_desp = self.labels.ids['desc_weather']
			self.weather_desp.text = str(weather['weather'][0]['description'])
		except:
			self.weather_desp = self.labels.ids['desc_weather']
			self.weather_desp.text = 'No Data'

		try:
			self.current_weather = self.labels.ids['current_weather']
			self.current_weather.text = str(weather['weather'][0]['main'])
		except:
			self.current_weather = self.labels.ids['current_weather']
			self.current_weather.text = 'No Data'

		try:
			#print('id (search code on openweathermap):', weather['weather'][0]['id'])
			#print('icon (search png on openweathermap): ', weather['weather'][0]['icon'])
			self.longitude = self.labels.ids['longitude']
			self.longitude.text = str(weather['coord']['lon'])

			self.latitude = self.labels.ids['latitude']
			self.latitude.text =str(weather['coord']['lat'])
		except:
			self.longitude = self.labels.ids['longitude']
			self.longitude.text = 'No Data'

			self.latitude = self.labels.ids['latitude']
			self.latitude.text ='No Data'
		

		try:
			self.wind_speed = self.labels.ids['wind_speed']
			self.wind_speed.text = '{} m/s'.format(str(weather['wind']['speed']))
		except:
			self.wind_speed = self.labels.ids['wind_speed']
			self.wind_speed.text = 'No Data'

		try:
			self.wind_direction = self.labels.ids['wind_direction']
			self.wind_direction.text = '{} degrees\n(in meterogical)'.format(str(weather['wind']['deg']))
		except:
			self.wind_direction = self.labels.ids['wind_direction']
			self.wind_direction.text = 'No Data'

		try:
			self.past_rain = self.labels.ids['past_rain']
			self.past_rain.text = '{} mm'.format(str(weather['rain']['1h']))
		except:
			self.past_rain = self.labels.ids['past_rain']
			self.past_rain.text = 'No Data'

		try :
			self.cloudiness = self.labels.ids['cloudiness']
			self.cloudiness.text = '{} %'.format(str(weather['clouds']['all']))
		except:
			self.cloudiness = self.labels.ids['cloudiness']
			self.cloudiness.text = 'No Data'

		try:
			icon_list = {'01d': 'weather-sunny', '01n':'weather-night', '02d':'weather-partly-cloudy', '02n':'weather-night-partly-cloudy','03d': 'weather-cloudy', '03n':'weather-cloudy','04d': 'weather-sunny', '04n':'weather-night','09d': 'weather-partly-rainy', '09n': 'weather-partly-rainy', '10d': 'weather-rainy', '10n':'weather-rainy', '11d':'weather-lightning-rainy', '11n':'weather-lightning-rainy', '13d': 'snowflake', '13n':'snowflake'}
			self.icon_is = self.labels.ids['icon_id']

			weather_cod_list = {
									'200': 'thunderstorm with \nlight rain', '201': 'thunderstorm with \nrain', '202': 'thunderstorm with \nheavy rain', '210': 'light thunderstorm', '211': 'thunderstorm', '212': 'heavy thunderstorm', '221': 'ragged thunderstorm', '230': 'thunderstorm with \nlight drizzle', '231': 'thunderstorm with \ndrizzle', '232': 'thunderstorm with \nheavy drizzle', 
									'300':'light intensity \ndrizzle', '301':'drizzle', '302':'heavy intensity \ndrizzle', '310':'	light intensity \ndrizzle rain', '311':'	drizzle rain', '312':'heavy intensity \ndrizzle rain', '313':'shower rain \nand drizzle', '314':'heavy shower \nrain and drizzle', '321':'shower drizzle', 
									'500':'light rain', '501':'moderate rain', '502':'heavy intensity \nrain', '503':'very heavy \nrain', '504':'extreme rain', '511':'freezing rain', '520':'light intensity \nshower rain', '521':'shower rain', '522':'heavy intensity \nshower rain', '531': 'ragged shower \nrain',
									'600':'light snow', '601':'	Snow', '602':'Heavy snow', '611':'Sleet', '612':'Light shower \nsleet', '613':'Shower sleet', '615':'Light rain \nand snow',  '616':'Rain and snow', '620':'Light shower \nsnow', '621':'Shower snow', '622':'Heavy shower \nsnow', 
									'701':'mist', '711':'Smoke', '721':'Haze', '731':'sand/dust \nwhirls',  '741':'fog', '751':'Sand', '761':'Dust', '762':'volcanic ash',  '771':'squalls', '781':'tornado',
									'800':'clear sky', '801':'few clouds: \n11-25%', '802':'scattered clouds: \n25-50%', '803'	:'broken clouds: \n51-84%', '804'	:'overcast clouds: \n85-100%'
								}

			

			self.weather_cod = self.labels.ids['weather_code']
			#self.weather_cod.text = str(weather['weather'][0]['id'])
			code_is = weather_cod_list[str(weather['weather'][0]['id'])]
			self.weather_cod.text = code_is

			self.weather_icon = self.labels.ids['weather_icon']
			#self.weather_icon.text = weather['weather'][0]['icon']

			icon = icon_list[weather['weather'][0]['icon']]
			self.icon_is.icon = icon
		except:
			self.weather_cod = self.labels.ids['weather_code']
			self.weather_cod.text = 'No Data'

			self.weather_icon = self.labels.ids['weather_icon']
			#self.weather_icon.text = 'No Data'

			self.icon_is = self.labels.ids['icon_id']
			self.icon_is.icon = 'apple-icloud'


		





	