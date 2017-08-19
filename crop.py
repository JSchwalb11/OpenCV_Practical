import numpy as np
import cv2
import argparse
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to image")
args = vars(ap.parse_args())
#print(vars)
#print(type(vars))

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#image cropping starts at 30,240(h,w) and ends at 120,335(h,w)
cropped = image[30:120, 240:335]
cv2.imshow("T-Rex Face", cropped)
print("Testing github push successful")

cv2.waitKey(0)
