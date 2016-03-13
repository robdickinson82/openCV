import numpy as np
import cv2

from windowHelpers import Window 
from colourHelpers import * 

#frame_inputs = [{"source": cv2.VideoCapture(0),
#			"windows": [
#						{
#							"title": "Threshold",
#							"frame_processes": CONVERT_TO_GRAYSCALE + \
#												MEDIAN_BLUR_5 + \
#												[{ "func": threshold_binary_gaussian_mean, "params": [255, 11, 2]},
#												{ "func": draw_crosshairs_at_centre, "params": [None]}],
#							"mouse_event_mappings": [
#													{"event": cv2.EVENT_LBUTTONDOWN, "func": mouse_left_click},
#
#							]
#						},
#						{
#							"title": "HSV",
#							"frame_processes": CONVERT_TO_HSV + \
#												[{ "func": hsv_threshold, "params": [[110,50,50], [130,255,255]]}]
#						},
#						{
#							"title": "Raw",
#							"frame_processes": IDENTITY,
#						}
#						]
#			}
#]


def video_cap_process_display(frame_inputs):

	for frame_input in frame_inputs:
		for window in frame_input["windows"]:
			window["window"] = Window(window["title"])
			if window.has_key("mouse_event_mappings"):
				for mouse_event_mapping in window["mouse_event_mappings"]:
					window["window"].add_event_mapping(mouse_event_mapping["event"], mouse_event_mapping["func"])

	while(True):
	    # Capture frame-by-frame
		for frame_input in frame_inputs:
			ret, frame = frame_input["source"].read()
			for window in frame_input["windows"]:
				processed_frame = frame.copy()
				# Our operations on the frame come here
				if window["frame_processes"]:
			   		for frame_process in window["frame_processes"]:
						processed_frame = frame_process["func"](processed_frame, frame_process["params"])

			    # Display the resulting frame
				window["window"].set_base_image(processed_frame)
				window["window"].update()

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	# When everything done, release the capture
	for frame_input in frame_inputs:
		frame_input["source"].release()
		for window in frame_input["windows"]:
			window["window"].close()
	
	return