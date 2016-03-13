import numpy as np
import cv2


BGR_BLUE = (255,0,0)
BGR_GREEN = (0,255,0)
BGR_RED = (0,0,255)
BGR_WHITE = (255,255,255)
BGR_BLACK = (0,0,0)


def bgr_to_hsv_values(colour_BGR):
    colour = np.uint8([[colour_BGR]])
    hsv_colour = cv2.cvtColor(colour,cv2.COLOR_BGR2HSV)
    print hsv_colour