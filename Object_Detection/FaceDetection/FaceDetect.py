import cv2

# img=cv2.imread("zoro.jpg",1)
# # print(img.shape)
# resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
# cv2.imshow("Roronoa",resized)
# cv2.waitKey(2000)
# cv2.destroyAllWindows()

#Creating a CascadeClassifier Object
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#Reading the image
img=cv2.imread("zoro.jpg")

#Reading the image as gray scale
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Search the co-ordinates of the image
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05,minNeighbors=5)

for x,y,w,h in faces:
	img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)

resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Zoro",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
