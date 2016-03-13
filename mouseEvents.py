import numpy as np
import cv2
from matplotlib import pyplot as plt

from config import *

from shapeHelpers import *

from imgProcessingHelpers import *


MOUSE_EVENTS = [
	cv2.EVENT_FLAG_ALTKEY, 
	cv2.EVENT_FLAG_CTRLKEY, 
	cv2.EVENT_FLAG_LBUTTON, 
	cv2.EVENT_FLAG_MBUTTON, 
	cv2.EVENT_FLAG_RBUTTON, 
	cv2.EVENT_FLAG_SHIFTKEY, 
	cv2.EVENT_LBUTTONDBLCLK, 
	cv2.EVENT_LBUTTONDOWN, 
	cv2.EVENT_LBUTTONUP, 
	cv2.EVENT_MBUTTONDBLCLK, 
	cv2.EVENT_MBUTTONDOWN, 
	cv2.EVENT_MBUTTONUP, 
	cv2.EVENT_MOUSEHWHEEL, 
	cv2.EVENT_MOUSEMOVE, 
	cv2.EVENT_MOUSEWHEEL, 
	cv2.EVENT_RBUTTONDBLCLK, 
	cv2.EVENT_RBUTTONDOWN, 
	cv2.EVENT_RBUTTONUP
]

MOUSE_FLAGS = [
	cv2.EVENT_FLAG_ALTKEY, 
	cv2.EVENT_FLAG_CTRLKEY, 
	cv2.EVENT_FLAG_LBUTTON, 
	cv2.EVENT_FLAG_MBUTTON, 
	cv2.EVENT_FLAG_RBUTTON, 
	cv2.EVENT_FLAG_SHIFTKEY, 
]


#def event_handler(event, x, y, flags, params):

def mouse_left_click(window, x,y, flags, params):
	circ = Circle((x,y), 50, BGR_BLACK, 3)
	text = Text("(" + str(x) + "," + str(y) + ")", (x+50,y+50), 1, BGR_BLACK, 2)
	window.clear_shape_overlay()
	window.add_shape_overlay(circ)
	window.add_shape_overlay(text)
	return


def mouse_left_click2(window, x,y, flags, params):
	circ = Circle((x,y), 75, RED, 3)
	window.clear_shape_overlay()
	window.add_shape_overlay(circ)
	return