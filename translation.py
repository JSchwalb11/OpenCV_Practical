import numpy as np
import argparse
import imutils
import cv2
from pdb import set_trace as st

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
	help = "Path to the image")
ap.add_argument("-t", "--test", required = False)
args = vars(ap.parse_args())
st()

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

#M is the translation Matrix
#np.float32([[1,0,tx], [0,1,ty]])
#[1,0,tx] is the horizontal axis where -(tx) translates the image left and (tx) shifts the image right
#[0,1,ty] is the vertical axis where -(tx) translates the image up and (tx) shifts the image down

M = np.float32([[1,0,25], [0,1,50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

M = np.float32([[1,0,-50], [0,1,-90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

shifted = imutils.translate(image,0,100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)

