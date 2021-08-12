import cv2,time

video=cv2.VideoCapture(0)

a=1
#Creating a CascadeClassifier Object
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
	a=a+1
	check,frame=video.read()
	# frame=cv2.GaussianBlur(frame,(21,21),0)
	
	# if first_frame is None:
	# 	first_frame=frame
	# 	continue

	faces=face_cascade.detectMultiScale(frame,scaleFactor=1.05,minNeighbors=5)

# print(check)
	print(frame)
# time.sleep(3)
	# gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	for x,y,w,h in faces:
		frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)

	cv2.imshow('Capturing',frame)
	key=cv2.waitKey(1)
	if key==ord('q'):
		break

print(a) #No of frames captured
video.release()
cv2.destroyAllWindows()