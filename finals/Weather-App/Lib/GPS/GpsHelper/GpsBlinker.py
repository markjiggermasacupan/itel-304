from kivy.garden.mapview import MapMarker
from kivy.animation import Animation

class GpsBlinker(MapMarker):
	def blink(self):
		#Animation change opacity and soze:
		anim = Animation(outer_opacity=0, blink_size = 50)
		#when Animation completes reset animation:
		anim.bind(on_complete= self.reset)
		anim.start(self)
		
	def reset(self, *args):
		self.outer_opacity = 1
		self.blink_size = self.default_blink_size
		self.blink()