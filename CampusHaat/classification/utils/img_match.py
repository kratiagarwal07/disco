from glob import glob
import numpy as np
import cv2, os, sys


def match(category, filename):
    train = cv2.imread(filename)
    category = "files/images/" + category
    arr = glob(category + '/*')
    res = []
    for file in arr:
        if "(copy)" not in file:
            res.append(file)

    result_img = ""
    result_score = 0

    for img in res:
        test = cv2.imread(img)
        score = run(test, train)
        if score > result_score:
            result_img = img
            result_score = score

    return result_img, result_score




def run(train, test, conn):
	# Detect the SIFT key points and compute the descriptors for the two images
	name = test
        test = cv2.imread(test)
	sift = cv2.xfeatures2d.SIFT_create()
	keyPoints1, descriptors1 = sift.detectAndCompute(train, None)
	keyPoints2, descriptors2 = sift.detectAndCompute(test, None)

	# Create brute-force matcher object
	bf = cv2.BFMatcher()
	matches = bf.knnMatch(descriptors1, descriptors2, k=2)

	# Select the good matches using the ratio test
	goodMatches = []

	for m, n in matches:
	    if m.distance < 0.9 * n.distance:
			goodMatches.append(m)

	result =  len(goodMatches)

	temp = {"Result" : result, "Img" : name}

	conn.send(temp)
	conn.close()

def format(img):
	temp = cv2.imread(img)
	cv2.imwrite(img + ".jpg", temp)
	os.remove(img)
