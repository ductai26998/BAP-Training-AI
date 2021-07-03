import numpy as np
import cv2 as cv
import math

# draw the black image
img = np.zeros((1000, 1000, 3), np.uint8)

def draw_italia(width, height):
    colors = [(68,141,0), (255,255,255), (53,42,200)]

    i_width = width // 3
    p_11 = (10, 10)
    p_12 = (p_11[0] + i_width, p_11[1] + height)

    p_21 = (p_11[0] + i_width, 10)
    p_22 = (p_21[0] + i_width, p_21[1] + height)

    p_31 = (p_11[0] + 2 * i_width, 10)
    p_32 = (p_31[0] + i_width, p_31[1] + height)
    points_italia = {'p11': (10, 10), 'p12': (110, 250),
                     'p21': (110, 10), 'p22': (210, 250),
                     'p31': (210, 10), 'p32': (310, 250)}

    ## Draw italya flag
    cv.rectangle(img, p_11, p_12, colors[0], -1)
    cv.rectangle(img, p_21, p_22, colors[1], -1)
    cv.rectangle(img, p_31, p_32, colors[2], -1)

def draw_vietnam(width, height):
    colors = [(0,0,255), (0,247,247)]

    # vars to compute star points
    x = 70
    g = math.pi / 5
    x1 = x * math.sin(g)
    x2 = x + x * math.cos(g)
    x3 = x * math.sin(2 * g)
    x4 = x - x * math.cos(2 * g)
    x5 = x1 * math.tan(g)

    # points of rectangle
    p1_r = (400, 10)
    p2_r = (p1_r[0] + width, p1_r[1] + height)
    # points of star
    ps1 = [p1_r[0] + width // 2, p1_r[1] + (height - 2 * x) // 2]
    ps2 = [ps1[0] - x1, ps1[1] + x2]
    ps3 = [ps1[0] + x3, ps1[1] + x4]
    ps4 = [ps1[0] - x3, ps1[1] + x4]
    ps5 = [ps1[0] + x1, ps1[1] + x2]
    ps6 = [ps1[0], ps1[1]]
    ps7 = [ps1[0], ps1[1] + x2 - x5]

    ## Draw Vietnamese Flag
    # draw the red background
    cv.rectangle(img, p1_r, p2_r, colors[0], -1)

    # draw star
    pts = np.array([ps1, ps2, ps3, ps4, ps5, ps6], np.int32)
    pts = pts.reshape((-1,1,2))
    cv.fillPoly(img,pts=[pts],color=colors[1])
    pts = np.array([ps3,ps4,ps7], np.int32)
    pts = pts.reshape((-1,1,2))
    cv.fillPoly(img,pts=[pts],color=(0,247,247))

def draw_japan(width, height):

    # points of rectangle
    pr1 = (10, 300)
    pr2 = (pr1[0] + width, pr1[1] + height)

    # center of circle
    pc = (pr1[0] + width // 2, pr1[1] + height // 2)

    # colors of flag
    colors = [(255,255,255), (32,32,214)]
    ## Draw japan flag
    cv.rectangle(img, pr1, pr2, colors[0], -1)
    cv.circle(img, pc, 60, colors[1], -1)


def draw_malay(width, height):
    # points to draw malaysia flag
    x = height // 11
    pr11 = (400,300)
    pr12 = (pr11[0] + width, pr11[1] + height)
    pr21 = (pr11[0],pr11[1] + x)
    pr22 = (pr12[0],pr21[1] + x)
    pr31 = (pr11[0],pr22[1] + x)
    pr32 = (pr12[0],pr31[1] + x)
    pr41 = (pr11[0],pr32[1] + x)
    pr42 = (pr12[0],pr41[1] + x)
    pr51 = (pr11[0],pr42[1] + x)
    pr52 = (pr12[0],pr51[1] + x)
    pr61 = (pr11[0],pr52[1] + x)
    pr62 = (pr12[0],pr61[1] + x)
    pr71 = (pr11[0],300)
    pr72 = (600,440)
    pc1 = (pr11[0] + width // 4,365)
    pc2 = (525,365)
    colors = [(0,0,198), (255,255,255), (0,198,247), (99,0,0)]

    ## Draw Malaysia flag
    cv.rectangle(img,pr11,pr12, colors[0], -1)

    cv.rectangle(img,pr21,pr22,colors[1], -1)
    cv.rectangle(img,pr31,pr32,colors[1], -1)
    cv.rectangle(img,pr41,pr42,colors[1], -1)
    cv.rectangle(img,pr51,pr52,colors[1], -1)
    cv.rectangle(img,pr61,pr62,colors[1], -1)

    cv.rectangle(img,pr71,pr72,(99,0,0), -1)

    cv.circle(img,pc1, 60,colors[2], -1)
    cv.circle(img,pc2, 60,colors[3], -1)

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

draw_italia(300, 250)
draw_vietnam(300, 250)
draw_japan(300, 250)
draw_malay(400, 220)

# Show image
cv.imshow("img", img)
cv.imwrite("flag.png", img)
cv.waitKey()
