import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp

Window.size = (350, 600)
#Window.fullscreen = 'auto'

kv = '''
MDFloatLayout:
      md_bg_color: 1, 1, 1, 1 
      MDLabel:
            id: location
            text: "--"
            pos_hint: {"center_x": .5,"center_y": .89 }
            halign: "center"
            font_size: "20sp"
            font_name: "Roboto"
      Image:
            id: weather_icon
            source: "assets/Image/default.png"
            pos_hint: {"center_x": .5,"center_y": .77 }
      MDLabel:
            id: temperature
            text: "[b]--[/b]"
            markup: True
            pos_hint: {"center_x": .5,"center_y": .62 }
            halign: "center"
            font_size: "55sp" 
      MDLabel:
            id: weather
            text: "-" 
            pos_hint: {"center_x": .5,"center_y": .54 }
            halign: "center"
            font_size: "20sp" 
            font_name: "Roboto"
      MDFloatLayout:
            pos_hint: {"center_x": .25, "center_y": .4}
            size_hint: .22, .1
            Image: 
                  source: "assets/Image/humidity.png"
                  pos_hint: {"center_x": .1,"center_y": .5}
            MDLabel: 
                  id: humidity
                  text: "--"
                  pos_hint: {"center_x": 1.1,"center_y": .7}  
                  font_size: "18sp"   
                  font_name: "Roboto"
            MDLabel: 
                  text: "Humidity"
                  pos_hint: {"center_x": 1.1,"center_y": .3 }
                  font_size: "14sp"   
                  font_name: "Roboto"
      MDFloatLayout:
            pos_hint: {"center_x": .25, "center_y": .4}
            size_hint: .22, .1
            Image: 
                  source: "assets/Image/windy-weather.gif"
                  pos_hint: {"center_x": 2,"center_y": .5}
            MDLabel: 
                  id: wind_speed
                  text: "--"
                  pos_hint: {"center_x": 3,"center_y": .7}  
                  font_size: "18sp"   
                  font_name: "Roboto"
            MDLabel: 
                  text: "Wind"
                  pos_hint: {"center_x": 3,"center_y": .3 }
                  font_size: "14sp"   
                  font_name: "Roboto"               
      MDFloatLayout:
            size_hint_y: .3
            canvas:
                  Color:
                        rgb: rgba(148, 117, 225, 255)
                  RoundedRectangle:
                        pos: self.pos
                        size: self.size                     
                        radius: [10, 10, 0, 0]
      MDFloatLayout:
            pos_hint: {"center_x": .5, "center_y": .20}
            size_hint: .9, .10
            canvas:
                  Color:
                        rgb: rgba(131, 69, 225, 255)
                  RoundedRectangle:
                        pos: self.pos
                        size: self.size                     
                        radius: [6]
            TextInput:
                  id: city_name
                  hint_text: "Search location"
                  size_hint: 1, None 
                  pos_hint: {"center_x": .5, "center_y": .11}
                  heigth: self.minimum_height
                  multiline: False
                  font_name: "Roboto"
                  font_size: "20sp"
                  hint_text_color: 1, 1, 1, 1
                  foreground_color: 1, 1, 1, 1
                  background_color: 1, 1, 1, 0
                  padding: 15
                  cursor_color: 1, 1, 1, 1 
                  cursor_width: "2sp"
            Button:
                  text: "Get Weather" 
                  font_name: "Roboto" 
                  pos_hint: {"center_x": .5, "center_y": -.5 }
                  font_size: "20sp"
                  size_hint: .5, .70
                  background_color: 1, 1, 1, 0
                  color: rgba(148, 117, 255, 255)
                  on_press: app.search_weather()
                  canvas.before:
                        Color:
                              rgb: 1, 1, 1, 1
                        RoundedRectangle:
                              pos: self.pos
                              size: self.size      
                              radius: [6]
'''

class WeatherApp(MDApp):
    geolocator = Nominatim(user_agent="weatherApp")
    api_key= "d3e8f04371cbbd107ced3672e5117146"

    def on_start(self):
        try:
            soup = BeautifulSoup(requests.get(f"https://www.google.com/search?q=weather+at+my+current+location").text, "html.parser")
            temp = soup.find("span", class_="BNeawe tAd8D AP7Wnd")
            location = ''.join(filter(lambda item: not item.isdigit(), temp.text)).split(",",1)
            self.get_weather(location[0])

        except requests.ConnectionError:
            print("No Internet Connection")
            exit()

    def build(self):
        return Builder.load_string(kv)

    def get_weather(self, city_name):
        try:
            location = self.geolocator.geocode(city_name)
            lat = location.latitude
            lon = location.longitude

            url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}"
            response = requests.get(url)
            x = response.json()
            print(x)
            if x["cod"] != "404":
                temperature = round(x["main"]["temp"]-273.15)
                humidity = x["main"]["humidity"]
                weather = x["weather"][0]["main"]
                id = str(x["weather"][0]["id"])
                wind_speed = round(x["wind"]["speed"]*18/5)
                location = x["name"] + ", " + x["sys"]["country"]
                self.root.ids.temperature.text = f"[b]{temperature}°[/b]"
                self.root.ids.weather.text = str(weather)
                self.root.ids.humidity.text = f"{humidity}%"
                self.root.ids.wind_speed.text = f"{wind_speed} kp/h"
                self.root.ids.location.text = location
                if id == "800":
                     self.root.ids.weather_icon.source = "assets/Image/clear-sky.png"
                elif "200" <= id <= "232":
                     self.root.ids.weather_icon.source = "assets/Image/storm.png"
                elif "300" <= id <= "321" and "500" <= id <= "531":
                    self.root.ids.weather_icon.source = "assets/Image/drizzle.png"
                elif "600" <= id <= "622":
                     self.root.ids.weather_icon.source = "assets/Image/snow.png"
                elif "701" <= id <= "781":
                     self.root.ids.weather_icon.source = "assets/Image/haze.png"
                elif "801" <= id <= "804":
                     self.root.ids.weather_icon.source = "assets/Image/clouds.png"

        except requests.ConnectionError:
            print("No Internet Connection")

    def search_weather(self):

        city_name = self.root.ids.city_name.text
        if not city_name:
            print("enter city")
        else:
            self.get_weather(city_name)

if __name__=='__main__':
    LabelBase.register(name="Roboto", fn_regular="assets\\Fonts\\Roboto-Regular.ttf")

WeatherApp().run()