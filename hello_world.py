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

def event_handler(event, x, y, flags, params):
	print (event, flags, params)
	event_dict = {cv2.EVENT_FLAG_ALTKEY : None, 
					cv2.EVENT_FLAG_CTRLKEY : mouse_click, 
					cv2.EVENT_FLAG_LBUTTON : None, 
					cv2.EVENT_FLAG_MBUTTON : None, 
					cv2.EVENT_FLAG_RBUTTON : None, 
					cv2.EVENT_FLAG_SHIFTKEY : None, 
					cv2.EVENT_LBUTTONDBLCLK : None, 
					cv2.EVENT_LBUTTONDOWN : mouse_click, 
					cv2.EVENT_LBUTTONUP : None, 
					cv2.EVENT_MBUTTONDBLCLK : None, 
					cv2.EVENT_MBUTTONDOWN : None, 
					cv2.EVENT_MBUTTONUP : None, 
					cv2.EVENT_MOUSEHWHEEL : None, 
					cv2.EVENT_MOUSEMOVE : None, 
					cv2.EVENT_MOUSEWHEEL : None, 
					cv2.EVENT_RBUTTONDBLCLK : None, 
					cv2.EVENT_RBUTTONDOWN : None, 
					cv2.EVENT_RBUTTONUP : None
			}


	print (event)
	if event_dict[event]:
		event_dict[event](x,y, flags, params)
	return

def mouse_left_click(window, x,y, flags, params):
	circ = Circle((x,y), 50, WHITE, 3)
	text = Text("(" + str(x) + "," + str(y) + ")", (x+50,y+50), 1, WHITE, 2)
	window.clear_shape_overlay()
	window.add_shape_overlay(circ)
	window.add_shape_overlay(text)
	return


def mouse_left_click2(window, x,y, flags, params):
	circ = Circle((x,y), 75, RED, 3)
	window.clear_shape_overlay()
	window.add_shape_overlay(circ)
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

def video_capture_and_process2( filename = None, frame_processes = None):
	window1_name = 'frame'
	window2_name = 'frame2'

	if filename:
		filename = INPUT_PATH + filename
	else:
		filename = 0
	print (filename)
	cap = cv2.VideoCapture(filename)

	window1 = Window(window1_name)
	window1.add_event_mapping(cv2.EVENT_LBUTTONDOWN, mouse_left_click)

	window2 = Window(window2_name)
	window2.add_event_mapping(cv2.EVENT_LBUTTONDOWN, mouse_left_click2)

	while(True):
	    # Capture frame-by-frame
	    ret, frame = cap.read()

	    # Our operations on the frame come here
	    if frame_processes:
	    	for frame_process in frame_processes:
	    		frame = frame_process["func"](frame, frame_process["params"])

	    # Display the resulting frame
	    window1.set_base_image(frame)
	    window1.update()
	    window2.set_base_image(frame)
	    window2.update()
	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break

	# When everything done, release the capture
	cap.release()
	window1.close()
	window2.close()
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

def add_shape_group(img, params):
	group = params[0]
	group.draw(img)
	return img

def convert_colour(img, params):
	img = cv2.cvtColor(img, params[0])	
	return img

def draw_crosshairs_at_centre(img, params):
	circ = Circle((int(img.shape[1]/2), int(img.shape[0]/2)), 50, WHITE, 3)
	circ.draw(img)
	return img

frame_processes = [
	#{ "func": convert_colour, "params": [cv2.COLOR_BGR2GRAY]},
	#{ "func": add_shape_group, "params": [group]}
	#{ "func": draw_crosshairs_at_centre, "params": [None]}
]

video_capture_and_process2(None, frame_processes)

#print (dir(cv2))

#events = [i for i in dir(cv2) if 'estroy' in i]
#print (events)

#print (cv2.EVENT_RBUTTONDOWN)



