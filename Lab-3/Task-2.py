import cv2
import numpy as np
img=cv2.imread('a.jpeg',1)
img=cv2.imread('b.jpeg',1)
flag=False
ix=-1
iy=-1

#new_img=cv2.resize(img(img.shape[1]//5,img.shape[0]//5))

def draw(event,x,y,flags,params):
    global flag,ix,iy
    if event==1:
        #cv2.circle(img,center=(x,y),radius=50,color=(0,0,0),thickness=3)
        #cv2.rectangle(img, pt1=(x,y), pt2=(x+10,y+34), color=(0,0,0),thickness=2)
        flag=True
        ix=x
        iy=y
    if event==4:
        cv2.rectangle(img,pt1=(ix,iy), pt2=(x+10,y+34), color=(0,0,0),thickness=2)
cv2.namedWindow(winname="munni")
cv2.setMouseCallback("munni",draw)
while True:
    cv2.imshow("munni", img)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

