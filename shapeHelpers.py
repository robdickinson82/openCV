import numpy as np
import cv2

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