import cv2, math, os
from scipy.ndimage import rotate
import numpy as np
from menu_scan_branch import run

def menu_scanner(vend):
    cap = cv2.VideoCapture(vend)
    frameRate = cap.get(5)/2
    result = []
    while(cap.isOpened()):
	    frameId = cap.get(1)
	    ret, frame = cap.read()
	    if (ret != True):
		    break
	    if (frameId % math.floor(frameRate) == 0 and frameId != 0):
		    filename = "/home/intel/FlaskApp/CampusHaat/classification/Temp/" + str(int(frameId)) + ".jpg"
		    frame = rotate(frame, -90)
		    cv2.imwrite(filename, frame)
		    first_col = run(filename)
		    for row in first_col:
			    if row not in result:
				    result.append(row)
    cap.release()
    return result
