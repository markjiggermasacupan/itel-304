from kivy.app import App
from kivy.core.window import Window
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="BSIT 3RD YEAR (WMAD) AY 2022-23")

MyApp().run() 

if __name__ == '__main__':
    MyApp().run()

# Process finished with exit code 0 #