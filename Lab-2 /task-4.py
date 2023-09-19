
import cv2
import numpy as np
img = cv2.imread('a.jpeg',1)
def draw(event,x,y,flags,params):
    print("hii")
cv2.namedWindow(winname="munni")
cv2.setMouseCallback("munni",draw)
while True:
    cv2.imshow("img",img)
    if cv2.waitKey(1) & 0xFF== ord('x'):
        break

cv2.destroyAllWindows()
