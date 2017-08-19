import numpy as np
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = ("Path to the image"))
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
print("Image Width: ", image.shape[1])
print("Image Height: ", image.shape[0])

r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)


r = 50 / image.shape[0]
dim = (int(image.shape[1] * r), 50)
print(r)
print(dim)

resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)

resized = imutils.resize(image, width = 100)
cv2.imshow("Resized via function", resized)

resized = imutils.resize(image, width = None, height = None)
cv2.imshow("Original displayed with function", resized)
cv2.waitKey(0)
