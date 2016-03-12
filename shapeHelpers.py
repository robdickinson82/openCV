import numpy as np
import cv2


BLUE = (255,0,0)
GREEN = (0,255,0)
RED = (0,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

class Window:
	def __init__(self, window_name):
		self.window_name = window_name
		self.window = cv2.namedWindow(window_name)
		self.event_mapping = {}
		self.key_mapping = {}
		cv2.setMouseCallback(window_name, self.event_handler)
		self.image = None
		self.shape_overlay = Group()
		return

	def event_handler(self, event, x, y, flags, params):
		if self.event_mapping.has_key(event):
			print ("Got Event")
			self.image = self.event_mapping[event](self, x,y, flags, params)
		return 
		
	def add_event_mapping(self, event, function):
		self.event_mapping[event] = function
		return

	def set_base_image(self, image):
		self.image = image
		return

	def add_shape_overlay(self, shape):
		self.shape_overlay.add(shape)
		return

	def clear_shape_overlay(self):
		self.shape_overlay = Group()
		return	

	def update(self):
		#print (self.image)
		if self.image.any():
			display_image = self.image.copy()
			self.shape_overlay.draw(display_image)
			cv2.imshow(self.window_name, display_image)
		return

	def close(self):
		cv2.destroyWindow(self.window_name)
		return


class Shape:
	def __init__(self, centre, colour_BGR, thickness):
		self.centre = centre
		self.colour_BGR = colour_BGR
		self.thickness = thickness
		self.parent = None
		self.id = None

	def translate(self, vector):
		self.centre = (self.centre[0] + vector[0], self.centre[1] + vector[1])
		return

	def set_colour(self, colour_BGR):
		self.colour_BGR = colour_BGR
		return

	def set_thickness(self, thickness):
		self.thickness = thickness
		return

	def set_parent(self, parent, id):
		self.parent = parent
		self.id = id
		return

	def remove_parent(self):
		self.parent = None
		self.id = None
		return

class Group:

	def __init__(self):
		self.members = {}
		self.next_id = 0
		return

	def add(self, shape):
		self.members[self.next_id] = shape
		shape.set_parent(self, self.next_id)
		self.next_id = self.next_id + 1
		return

	def remove(self, shape):
		del self.members[shape.id]
		shape.remove_parent()
		return

	def draw(self, img):
		for member in self.members:
			self.members[member].draw(img)
		return

	def resize(self, factor):
		for member in self.members:
			self.members[member].resize(factor)
		return

	def translate(self, vector):
		for member in self.members:
			self.members[member].translate(vector)
		return

	def set_colour(self, colour_BGR):
		for member in self.members:
			self.members[member].set_colour(colour_BGR)
		return

	def set_thickness(self, thickness):
		for member in self.members:
			self.members[member].set_thickness(thickness)
		return				

class Text(Shape):

	FONT = cv2.FONT_HERSHEY_SIMPLEX
	LINE_TYPE = cv2.LINE_AA

	def __init__(self, contents, origin, font_size, colour_BGR, thickness):
		self.centre = origin
		self.contents = contents
		self.font_size = font_size
		self.colour_BGR = colour_BGR
		self.thickness = thickness	

	def draw(self, img):
		cv2.putText(img, self.contents, self.centre, self.FONT, self.font_size, self.colour_BGR, self.thickness, self.LINE_TYPE)
		return

	def resize(self, factor):
		self.font_size = int(self.font_size * factor)
		return	

class Rectangle(Shape):
	def __init__(self, centre, size, colour_BGR, thickness):
		self.centre = centre
		self.size = size
		self.colour_BGR = colour_BGR
		self.thickness = thickness	

	def draw(self, img):
		img = cv2.rectangle(img, (self.centre[0] - self.size[0]/2, self.centre[1] - self.size[1]/2), (self.centre[0] + self.size[0]/2, self.centre[1] + self.size[1]/2), self.colour_BGR, self.thickness)
		return

	def resize(self, factor):
		self.size = (int(self.size[0] * factor), int(self.size[1] * factor))
		return

class Circle(Shape):
	def __init__(self, centre, radius, colour_BGR, thickness):
		self.centre = centre
		self.radius = radius
		self.colour_BGR = colour_BGR
		self.thickness = thickness	

	def draw(self,img):
		cv2.circle(img, self.centre, self.radius, self.colour_BGR, self.thickness)
		return

	def resize(self, factor):
		self.radius = int(self.radius * factor)
		return

class Ellipse(Shape):
	def __init__(self, centre, radii, angle, arc, colour_BGR, thickness):
		self.centre = centre
		self.radii = radii
		self.angle = angle
		self.arc = arc
		self.colour_BGR = colour_BGR
		self.thickness = thickness	

	def draw(self,img):
		img = cv2.ellipse(img, self.centre, self.radii, self.angle, self.arc[0], self.arc[1], self.colour_BGR, self.thickness)
		return

	def resize(self, factor):
		self.radii = (int(self.radii[0] * factor), int(self.radii[1] * factor))
		return

