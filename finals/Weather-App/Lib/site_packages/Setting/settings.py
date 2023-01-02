from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivymd.toast import toast



class SettingScreen(Screen):

	def go_back(self):
		app = MDApp.get_running_app()

		app.root.ids.screen_manager.current = 'main_screen'

	#Internet Permission:
	def internet_callback(self, switchObject, switchValue):

		# Switch value are True and False
		if(switchValue):
			toast('Internet: Enabled')
		else:
			toast('Internet: Disabled')

	# Sync Switch :
	def sync_callback(self, switchObject, switchValue):

		# Switch value are True and False
		if(switchValue):
			toast('Sync ...')
		else:
			toast('Disabled')

	# GPS Switch:
	def gps_callback(self, switchObject, switchValue):

		# Switch value are True and False
		if(switchValue):
			toast('GPS: Enabled')
		else:
			toast('GPS: Disabled')

	# Storage Callback:
	def storage_callback(self, switchObject, switchValue):

		# Switch value are True and False
		if(switchValue):
			toast('Storage: Accessible')
		else:
			toast('Storage: Denied')

	# Gps Safe Mode :
	def gps_safe_mode_callback(self, switchObject, switchValue):

		# Switch value are True and False
		if(switchValue):
			toast('Safe Mode: ON')
		else:
			toast('Safe Mode: OFF')

	# Security Callback :
	def security_callback(self, switchObject, switchValue):

		# Switch value are True and False
		if(switchValue):
			toast('Securing...')
		else:
			toast('Please unable it !')

	# Data Limit Callback:
	def data_callback(self, switchObject, switchValue):

		# Switch value are True and False
		if(switchValue):
			toast('Data Limit set to 50 MB')
		else:
			toast('Disabled')	

	# Notification callback:
	def notification_callback(self, switchObject, switchValue):

		# Switch value are True and False
		if(switchValue):
			toast('Notification: Enabled')
			
		else:
			toast('Notification: Disabled')

	# Default :
	def callback(self, switchObject, switchValue):

		# Switch value are True and False
		if(switchValue):
			toast('Enabling....')
		else:
			toast('Disabling...')