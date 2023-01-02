from Lib.GPS.GpsHelper.GpsBlinker import GpsBlinker
from kivymd.app import MDApp

#
from kivy.utils import platform
from kivymd.uix.dialog import MDDialog



class GpsHelper():
	has_centered_map = False

	def run(self):
		#Blinker :


		#Get Refrence for Blinker and call Blink()
		app = MDApp.get_running_app()
		gps_blinker = app.root.ids['map_view'].ids['gps_blinker']
		gps_blinker.blink()

		# Permission:
		if platform == 'android':
			from android.permission import Permission, request_permission
			def callback(permission, results):
				if all([res for res in results]):
					print("Got all Permissions")

					# switches :
					app = MDApp.get_running_app()
					gps_switch = app.root.ids.setting_screen.ids.gps_switch
					gps_switch.active = True

					internet_switch = app.root.ids.setting_screen.ids.internet_switch
					internet_switch.active = True


				else:
					print("Did not get all Permissions")

					# switches :
					app = MDApp.get_running_app()
					gps_switch = app.root.ids.setting_screen.ids.gps_switch
					gps_switch.active = False

					internet_switch = app.root.ids.setting_screen.ids.internet_switch
					internet_switch.active = False

			request_permission([Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION], callback)




		# Configure GPS:
		if platform == 'android' or platform =='ios':
			from plyer import gps

			gps.configure(on_location= self.update_blinker_position, on_status= self.on_auth_status)

			gps.start(minTime = 1000, minDistance=0)

	def update_blinker_position(self, *args, **kwargs):
		my_lat = kwargs['lat']
		my_lon = kwargs['lon']
		
		print("GPS Position", my_lat, my_lon)

		# Update Blinker Position:
		app = MDApp.get_running_app()
		gps_blinker = app.root.ids['map_view'].ids['gps_blinker']
		gps_blinker.lat = my_lat
		gps_blinker.lon = my_lon

		# Center Map Positon:
		if not self.has_centered_map:
			mapview = app.root.ids['map_view'].ids['map_views_id']
			mapview.center_on(my_lat, my_lon)
			self.has_centered_map = True

	def on_auth_status(self, general_stauts, status_message):
		if general_stauts == 'provider-enabled':
			# switches :
			app = MDApp.get_running_app()
			gps_switch = app.root.ids.setting_screen.ids.gps_switch
			gps_switch.active = True

			internet_switch = app.root.ids.setting_screen.ids.internet_switch
			internet_switch.active = True
			pass
		else :
			self.open_gps_access_popup()

	def open_gps_access_popup(self):
		dialog = MDDialog(title='GPS Error', text='You need to enable GPS access for the app to Function')
		dialog.size_hint = [.8, .8]
		dialog.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
		dialog.open()



		


		

