from kivymd.uix.screen import Screen
from kivymd.app import MDApp
import sqlite3
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton




class ProfileScreen(Screen):
	# Go Back Function :
	def go_back(self):
		app = MDApp.get_running_app()
		app.root.ids.screen_manager.current = 'main_screen'

	def save_password(self):
		if self.ids.password.text == '' or self.ids.re_password.text == '':
			dialog = MDDialog(title ='Error !', size_hint_y= None, height='90dp',padding=10, 
								text='Password is left Empty !',
								buttons=[
								MDRaisedButton(text="OK")
								])
			dialog.open()
			
		else:
			if self.ids.password.text == self.ids.re_password.text:
				dialog = MDDialog(title ='Password saved !', size_hint_y= None, height='90dp', padding=10, 
								text='Kindly click on save Profile to save changes...',
								buttons=[
									MDRaisedButton(text="OK")
								])
				dialog.open()
			else :
				dialog = MDDialog(title ='Error !', size_hint_y= None, height='90dp',padding=10, 
								text='Password didn\'t match. Please Re-enter...', 
								buttons=[
									MDRaisedButton(text="OK")
								])
				dialog.open()


	def save_profile(self):
		connect = sqlite3.connect('Lib\\site_packages\\Profile\\data\\data.db')
		self.connect = connect

		connect.execute('''CREATE TABLE IF NOT EXISTS todo(
							id INTEGER PRIMARY KEY,
							name TEXT NOT NULL, 
							email TEXT NOT NULL,
							password TEXT NOT NULL
							);
						''')

		if self.ids.name.text == '' or self.ids.email.text == '' or self.ids.password.text == '' or self.ids.re_password.text == '':
			dialog = MDDialog(title ='Error !', size_hint_y= None, height='90dp',padding=10, 
								text='Fill all the Details...', 
								buttons=[
									MDRaisedButton(text="OK")
								])
			dialog.open()
		else:
			if self.ids.password.text == self.ids.re_password.text:
				dialog = MDDialog(title ='Profile Saved', size_hint_y= None, height='90dp',padding=10, 
									text='Profile is Saved', 
									buttons=[
										MDRaisedButton(text="OK")
									])
				dialog.open()
				name = self.ids.name.text
				email = self.ids.email.text
				password = self.ids.password.text 
				self.insert_data(name, email, password)
			else :
				toast('Password didn\'t matched !')

	def insert_data(self, name, email, password):
		print(name, email, password)
		connect = self.connect
		query = "INSERT INTO todo(name, email, password) VALUES(?,?,?);"
		connect.execute(query, (name, email, password,))
		connect.commit()
		print('CREATE')

		query = 'SELECT * FROM todo;'
		for rows in connect.execute(query):
			print(rows)
		
		# Changing NavDrawer name and mail :
		connect = sqlite3.connect('Lib\\site_packages\\Profile\\data\\data.db')
		cursor = connect.cursor()

		# Fentch Name :
		cursor.execute("SELECT name FROM todo")
		cols = cursor.fetchall()
		user_name = cols[0][0]
		
		app = MDApp.get_running_app()
		name = app.root.ids.content_navdrawer.ids.user_name
		name.text = 'Welcome, {0}'.format(user_name)

		# Fentch Mail name:
		cursor.execute("SELECT email FROM todo")
		mail = cursor.fetchall()
		user_mail = mail[0][0]
		gmail = app.root.ids.content_navdrawer.ids.user_gmail
		gmail.text = 'Mail: {0}'.format(user_mail)
		

	def edit_profile(self):
		connect = sqlite3.connect('Lib\\site_packages\\Profile\\data\\data.db')
		print('File cleared...')
		query = "DELETE FROM todo;"
		connect.execute(query, ())
		connect.commit()
		toast('Edit New Profile...')
