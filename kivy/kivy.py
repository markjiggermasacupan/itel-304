from kivy

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self)
        return Label(text="BSIT 3RD YEAR (WMAD) AY 2022-23")

MyApp().run() 

if __name__ == '__main__':
    app.run()

# Process finished with exit code 0


# Installing Kivy on Windows:

#1 Ensure you have the latest pip and wheel:
# python -n -pip install --upgrade pip wheel setuptools

#2 Install the dependencies:
# python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
# python -m pip install kivy.desp.angle

#3 Install Kivy
# python -m pip install kivy

#4 As Optional, you may try Installing Kivy with examples
# python -m pip install kivy examples
