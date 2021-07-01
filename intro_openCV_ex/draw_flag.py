import numpy as np
import cv2 as cv
import math

# draw the black image
img = np.zeros((1000, 1000, 3), np.uint8)

## Draw italya flag
cv.rectangle(img,(10,10),(110,250),(68,141,0), -1)
cv.rectangle(img,(110,10),(210,250),(255,255,255), -1)
cv.rectangle(img,(210,10),(310,250),(53,42,200), -1)

## Draw Vietnamese Flag
# draw the red background
cv.rectangle(img,(400, 10),(700,250),(0,0,255), -1)

# draw star
x = 70
g = math.pi/5
x1 = x * math.sin(g)
x2 = x + x * math.cos(g)
x3 = x * math.sin(2 * g)
x4 = x - x * math.cos(2 * g)
x5 = x1 * math.tan(g)
# height = edge * math.sin(math.pi/3)

pts = np.array([[641, 240],
               [641 - x1, 240 - x2],
               [641 + x3, 240 - x4],
               [641 - x3, 240 - x4],
               [641 + x1, 240 - x2],
               [641, 240]], np.int32)
pts = np.array([[550, 70],
               [550 - x1, 70 + x2],
               [550 + x3, 70 + x4],
               [550 - x3, 70 + x4],
               [550 + x1, 70 + x2],
               [550, 70]], np.int32)
pts = pts.reshape((-1,1,2))
cv.fillPoly(img,pts=[pts],color=(0,247,247))
pts = np.array([[550 + x3, 70 + x4],
               [550 - x3, 70 + x4],
               [550, 70 + x2 - x5]], np.int32)
pts = pts.reshape((-1,1,2))
cv.fillPoly(img,pts=[pts],color=(0,247,247))

## Draw japan flag
cv.rectangle(img,(10,300),(310,550),(255,255,255), -1)
cv.circle(img,(160,425), 60, (32,32,214), -1)

# Show image
cv.imshow("img", img)
cv.waitKey()