import numpy as np
import cv2
from matplotlib import pyplot as plt

from config import *

from shapeHelpers import *

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

#open_display_wait("hello world", TEST_IMAGES[0])

def demo_plot():
	img = open_input_image(TEST_IMAGES[0])
	plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
	plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
	plt.show()
	return

def create_blank_canvas(width, height):
	img = np.zeros((width,height,3), np.uint8)
	return img

def draw_line_on_image(img, start, end, colour_BGR, thickness):
	img = cv2.line(img, start, end, colour_BGR, thickness)
	return img	

def draw_circle_on_image(img, centre, radius, colour_BGR, thickness):
	img = cv2.circle(img, centre, radius, colour_BGR, thickness)
	return img

def draw_ellipse_on_image(img, centre, minor, major, angle, start_angle, end_angle, colour_BGR, thickness):
	img = cv2.ellipse(img, centre, (minor, major), angle, start_angle, end_angle, colour_BGR, thickness)

def draw_rect_on_image(img, top_left, bottom_right, colour_BGR, thickness):
	img = cv2.rectangle(img, top_left, bottom_right, colour_BGR, thickness)
	return img

def demo_video_capture(filename = None):
	if filename:
		filename = INPUT_PATH + filename
	else:
		filename = 0
	print (filename)
	cap = cv2.VideoCapture(filename)

	while(True):
	    # Capture frame-by-frame
	    ret, frame = cap.read()

	    # Our operations on the frame come here
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    #draw_line_on_image(gray, 0, 0, 511, 511, (255,0,0), 10)

	    # Display the resulting frame
	    cv2.imshow('frame',gray)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

	# When everything done, release the capture
	cap.release()
	cv2.destroyAllWindows()
	return


def demo_shapes():
	# Create a black image
	img = create_blank_canvas(512, 512)
	# Draw a diagonal blue line with thickness of 5 px
	draw_line_on_image(img, (0, 0), (511, 511), (255,0,0), 10)
	draw_ellipse_on_image(img, (100,100), 50, 100, 45, 25, 125, (0,255,0), 2)
	draw_rect_on_image(img, (100,100), (200,300), (255,255,0), 2)
	draw_circle_on_image(img, (400,400), 100, (0,255,255), 3)

	display_window("Title", img)
	wait_for_key_press_and_close()
	return



img = create_blank_canvas(512, 512)


shapes = Group()


rect = Rectangle((100,100), (100,150), (0,0,255), 2)
shapes.add(rect)

shapes.draw(img)

shapes.translate((100,50))

shapes.draw(img)



display_window("Title", img)
wait_for_key_press_and_close()




#demo_video_capture()
#demo_shapes()



