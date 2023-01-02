from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton, MDRaisedButton
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField

from kivy.garden.mapview import MapMarkerPopup
from kivy.uix.button import Button
# Geocode:

from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivymd.toast import toast
import certifi


class Content1(Screen):
    pass


class MapDisplay(MDBoxLayout):
	def go_back(self):
		app = MDApp.get_running_app()

		app.root.ids.screen_manager.current = 'main_screen'

	def search_city(self):
		
		self.search_dialog = MDDialog(title ='Enter City :', size_hint_y= None, padding= 10,height='90dp',
									type="custom", content_cls=Content1(),

							buttons=[
								MDRaisedButton(text="CANCEL", on_release= self.closeDialog),
								MDRaisedButton(text="OK", on_release= self.is_city)
									]
								)

		self.search_dialog.set_normal_height()
		self.search_dialog.open()

	def closeDialog(self, inst):
		self.search_dialog.dismiss()

	def is_city(self, inst):
		for obj in self.search_dialog.content_cls.children:
			if isinstance(obj, MDTextField):
				self.input = obj.text
				print(obj.text)
				self.geocode_get_lat_lon(obj.text)
				self.search_dialog.dismiss()				
				

	def geocode_get_lat_lon(self, address):
		app_id= "" # ID and key required....
		app_code = ""
		print(address)
		address = parse.quote(address)

		url = ""%(address, app_id, app_code) # Visit to geocoder.com and paste the url here...
		UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error, ca_file=certifi.where())

	def success(self, urlrequest, result):
		print("Success")
		latitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
		longitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
		print(self.ids)		
		mapview = self.ids.map_views_id
		mapview.center_on(latitude, longitude)
		marker = MapMarkerPopup(lat=latitude, lon=longitude, source="Resorces\\blue_marker.png", popup_size=(200,75))
		marker.bind(on_press = self.details)
		inst = self.input
		marker.add_widget(Button(text = "{0} \nClick here and\n Add this City".format(self.input), on_press=self.details))

		mapview.add_widget(marker)

	def failure(self, urlrequest, result):
		print("failure")
		print(result)

	def error(self, urlrequest, result):
		print("Errror")
		print(result)

	def details(self, inst, *args):
		#print('Detail', *args)
		inst = self.input
		self.details1(inst)

	def details1(self, inst):
		print('Detail', inst)
		app = MDApp.get_running_app()
		app.map_city(inst)

	def message(self):
		import time
		toast('Try Nearby City !')
		time.sleep(2)
		print('init')
		toast('Try Nearby City !')

	


