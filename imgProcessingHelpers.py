import numpy as np
import cv2
from matplotlib import pyplot as plt

from config import *

from shapeHelpers import *
from colourHelpers import *

def create_blank_canvas(img, params):
	img = np.zeros((params[0],params[1],3), np.uint8)
	return img

def add_shape_group(img, params):
	group = params[0]
	group.draw(img)
	return img

def convert_colour(img, params):
	img = cv2.cvtColor(img, params[0])	
	return img

def draw_crosshairs_at_centre(img, params):
	circ = Circle((int(img.shape[1]/2), int(img.shape[0]/2)), 50, BGR_BLACK, 3)
	circ.draw(img)
	return img

def threshold_binary(img, params):
	ret,th1 = cv2.threshold(img,params[0],params[1],cv2.THRESH_BINARY)
	return th1	

def threshold_binary_adaptive_mean(img, params):
	th1 = cv2.adaptiveThreshold(img,params[0],cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,params[1],params[2])
	return th1	


def threshold_binary_gaussian_mean(img, params):
	th1 = cv2.adaptiveThreshold(img,params[0],cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,params[1],params[2])
	return th1

def median_blur(img, params):
	img = cv2.medianBlur(img,params[0])	
	return img

def hsv_threshold(img, params):
    # define range of blue color in HSV
    #lower_blue = np.array([110,50,50])
    #upper_blue = np.array([130,255,255])

	lower_colour = np.array(params[0])
	upper_colour = np.array(params[1])

    # Threshold the HSV image to get only blue colors
	mask = cv2.inRange(img, lower_colour, upper_colour)
	return mask

CONVERT_TO_GRAYSCALE = [{ "func": convert_colour, "params": [cv2.COLOR_BGR2GRAY]}]

CONVERT_TO_HSV = [{ "func": convert_colour, "params": [cv2.COLOR_BGR2HSV]}]

MEDIAN_BLUR_5 = [{ "func": median_blur, "params": [5]}]

IDENTITY = []


	#{ "func": add_shape_group, "params": [group]}
	#{ "func": draw_crosshairs_at_centre, "params": [None]}
	#{ "func": threshold_binary, "params": [127, 255]}
	#{ "func": threshold_binary_adaptive_mean, "params": [255, 11, 2]}
	#{ "func": threshold_binary_gaussian_mean, "params": [255, 11, 2]}
