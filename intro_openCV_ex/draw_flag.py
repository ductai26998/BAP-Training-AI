import numpy as np
import cv2 as cv
import math

# draw the black image
img = np.zeros((1000, 1000, 3), np.uint8)

points_italia = {'p11': (10,10), 'p12': (110,250),
                 'p21': (110,10), 'p22': (210,250),
                 'p31': (210,10), 'p32': (310,250)}
colors_italia = [(68,141,0), (255,255,255), (53,42,200)]

# star point of vietnam
x = 70
g = math.pi/5
x1 = x * math.sin(g)
x2 = x + x * math.cos(g)
x3 = x * math.sin(2 * g)
x4 = x - x * math.cos(2 * g)
x5 = x1 * math.tan(g)

points_vn = {'xr': (400, 10),
             'yr': (700,250),
             'ps1': [550, 70],
             'ps2': [550 - x1, 70 + x2],
             'ps3': [550 + x3, 70 + x4],
             'ps4': [550 - x3, 70 + x4],
             'ps5': [550 + x1, 70 + x2],
             'ps6': [550, 70],
             'ps7': [550, 70 + x2 - x5]}
colors_vn = [(0,0,255), (0,247,247)]

points_jp = {'pr1': (10,300),
             'pr2': (310,550),
             'pc': (160,425)}
colors_jp = [(255,255,255), (32,32,214)]

points_ml = {'pr11': (400,300),'pr12': (800,520),
             'pr21': (400,320),'pr22': (800,340),
             'pr31': (400,360),'pr32': (800,380),
             'pr41': (400,400),'pr42': (800,420),
             'pr51': (400,440),'pr52': (800,460),
             'pr61': (400,480),'pr62': (800,500),
             'pr71': (400,300),'pr72': (600,440),
             'pc1': (500,365), 'pc2': (525,365)}
colors_ml = [(0,0,198), (255,255,255), (0,198,247), (99,0,0)]

def draw_italia(points, colors):
    ## Draw italya flag
    # cv.rectangle(img, points[0][1], colors[0], -1)
    # cv.rectangle(img, points[1], colors[1], -1)
    # cv.rectangle(img, points[2], colors[2], -1)
    cv.rectangle(img, points['p11'], points['p12'], colors[0], -1)
    cv.rectangle(img, points['p21'], points['p22'], colors[1], -1)
    cv.rectangle(img, points['p31'], points['p32'], colors[2], -1)

def draw_vietnam(points, colors):
    ## Draw Vietnamese Flag
    # draw the red background
    cv.rectangle(img, points['xr'], points['yr'], colors[0], -1)

    # draw star
    pts = np.array([points['ps1'],
                    points['ps2'],
                    points['ps3'],
                    points['ps4'],
                    points['ps5'],
                    points['ps6']], np.int32)
    pts = pts.reshape((-1,1,2))
    cv.fillPoly(img,pts=[pts],color=colors[1])
    pts = np.array([points['ps3'],
               points['ps4'],
               points['ps7']], np.int32)
    pts = pts.reshape((-1,1,2))
    cv.fillPoly(img,pts=[pts],color=(0,247,247))

def draw_japan(points, colors):
    ## Draw japan flag
    cv.rectangle(img,points['pr1'],points['pr2'], colors[0], -1)
    cv.circle(img,points['pc'], 60, colors[1], -1)


def draw_malay(points, colors):
    ## Draw Malaysia flag
    cv.rectangle(img,points['pr11'],points['pr12'],colors[0], -1)

    cv.rectangle(img,points['pr21'], points['pr22'],colors[1], -1)
    cv.rectangle(img,points['pr31'], points['pr32'],colors[1], -1)
    cv.rectangle(img,points['pr41'], points['pr42'],colors[1], -1)
    cv.rectangle(img,points['pr51'], points['pr52'],colors[1], -1)
    cv.rectangle(img,points['pr61'], points['pr62'],colors[1], -1)

    cv.rectangle(img,points['pr71'], points['pr72'],(99,0,0), -1)

    cv.circle(img,points['pc1'], 60, colors[2], -1)
    cv.circle(img,points['pc2'], 60, colors[3], -1)

    pts = np.array([[535,335],
                [490,385],
                [560,365],
                [495,345],
                [535,395]], np.int32)

    pts = pts.reshape((-1,1,2))
    cv.fillPoly(img,pts=[pts],color=(0,198,247))
    pts = np.array([[560,365],
               [495,345],
               [520,377]], np.int32)
    pts = pts.reshape((-1,1,2))
    cv.fillPoly(img,pts=[pts],color=(0,198,247))
    # cv.polylines(img,[pts],True,(32,32,214))

draw_italia(points_italia, colors_italia)
draw_vietnam(points_vn, colors_vn)
draw_japan(points_jp, colors_jp)
draw_malay(points_ml,colors_ml)
# Show image
cv.imshow("img", img)
cv.imwrite("flag.png", img)
cv.waitKey()
