import numpy as np 
import cv2

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'DIVX')
out=cv2.VideoWriter('ouput.avi', fourcc,20.0,(640,480))

while(True):
	ret, frame=cap.read()

	# gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	out.write(frame)
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()