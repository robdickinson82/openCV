import numpy as np
import cv2
from matplotlib import pyplot as plt

from config import *

from shapeHelpers import *
from windowHelpers import *
from colourHelpers import *
from videoHelpers import *
from imgProcessingHelpers import *

from mouseEvents import *

def open_input_image(filename):
	img = cv2.imread(INPUT_PATH + filename)
	return img

def save_output_image(filename, img):
	cv2.imwrite(OUTPUT_PATH + filename, img)
	return

def display_window(title, img):
	cv2.namedWindow(title, cv2.WINDOW_NORMAL)
	cv2.imshow(title, img)
	return

def wait_for_key_press_and_close():
	k = cv2.waitKey(0)
	cv2.destroyAllWindows()	
	return

def open_display_wait(title, filename):
	img = open_input_image(filename)
	display_window(title, img)
	wait_for_key_press_and_close()
	return

def demo_plot():
	img = open_input_image(TEST_IMAGES[0])
	plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
	plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
	plt.show()
	return

def demo_shapes():
	img = create_blank_canvas(512, 512)
	shapes = Group()
	rect = Rectangle((100,100), (100,150), (0,0,255), 2)
	text = Text("Hello World", (100,100), 5, (0,128,255), 2)
	shapes.add(rect)
	shapes.add(text)
	shapes.draw(img)
	shapes.translate((100,50))
	shapes.resize(0.5)
	shapes.draw(img)
	display_window("Title", img)
	wait_for_key_press_and_close()
	return

frame_inputs = [{"source": cv2.VideoCapture(0),
			"windows": [
						{
							"title": "Threshold",
							"frame_processes": CONVERT_TO_GRAYSCALE + \
												MEDIAN_BLUR_5 + \
												[{ "func": threshold_binary_gaussian_mean, "params": [255, 11, 2]},
												{ "func": draw_crosshairs_at_centre, "params": [None]}],
							"mouse_event_mappings": [
													{"event": cv2.EVENT_LBUTTONDOWN, "func": mouse_left_click},

							]
						},
						{
							"title": "HSV",
							"frame_processes": CONVERT_TO_HSV + \
												[{ "func": hsv_threshold, "params": [[110,50,50], [130,255,255]]}]
						},
						{
							"title": "Raw",
							"frame_processes": IDENTITY,
						}
						]
			}
]

video_cap_process_display(frame_inputs)

#print (dir(cv2))

#events = [i for i in dir(cv2) if 'estroy' in i]
#print (events)

#print (cv2.EVENT_RBUTTONDOWN)



