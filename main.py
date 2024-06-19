import cv2

# to load the xml file
a= cv2.CascadeClassifier("haarcascade_frontalface-default1.xml")

# allowing the access to the camera
b= cv2.VideoCapture(0)

while True:
  c_rect , d_img = b.read()
# converting the color
  e = cv2.cvtColor(d_img , cv2.COLOR_BGR2GRAY)
  
  f = a. detectMultiScale(e,1.3,6,(100,100))
  
  for (x,y,w,h) in f:
# a rectangular shape is shown on the face
    cv2.rectangle(d_img, (x,y), (x+w, y+h), (255.0,0))
    
  cv2.imshow('image', d_img)
#waiting up for particular second

  h= cv2.waitKey(30) & 0xff
  if h== 30:
    break
  
# shutting off the camera
b.release()
# closing all the windows
cv2.destroyAllWindows()
    
    
  





