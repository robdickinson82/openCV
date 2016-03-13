import numpy as np
import cv2

from shapeHelpers import *



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