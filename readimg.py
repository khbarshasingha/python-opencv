import numpy as np 
import cv2
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
img=cv2.imread("vn.jpeg",0)
cv2.imshow('image',img)
k=cv2.waitKey(0) & 0xFF
if k==ord('s'):
	# x=input("Enter the file name")
	cv2.imwrite('vn2.png',img)
	cv2.destroyAllWindows()
