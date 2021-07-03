import numpy as np
import cv2 as cv

def detect_color(img, lower_color, upper_color):
    """
        detect color and return (x,y) coordinate of that point
        params:
            img: image_input
            lower_color: lower threshold of color

    """
    # covert img to hsv image
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv_img, lower_color, upper_color)

    # get position of point
    x, y = get_position(mask)
    return (x, y)

def draw(points, color):
    for point in points:
        cv.circle(img, (point[0], point[1]), 10, color, -1)

def get_position(img):
    # find all contours in image
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for contour in contours:
        area = cv.contourArea(contour) # return numbers of pixel not 0
        if area > 500:
            p = cv.arcLength(contour, True) # calculates a contour perimeter is closed
            approx = cv.approxPolyDP(contour, 0.1 * p, True) # Approximates a polygonal curve(s) with the specified precision
            x, y , w, h = cv.boundingRect(approx) # Calculates the up-right bounding rectangle of a point set or non-zero pixels of gray-scale image.

    return x + w // 2, y

# set and load video from camera
frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
# img = cv.imread('but.jpg')

points = []

while True:
    _, img = cap.read()

    # define range of red color in HSV
    lower_red = np.array([0, 100, 20])
    upper_red = np.array([10, 255, 255])
    red = [0, 0, 255]

    # define range of green color in HSV
    lower_green = np.array([40, 70, 72])
    upper_green = np.array([80, 255, 255])
    green = [0, 255, 0]

    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    blue = [255, 0, 0]

    point = detect_color(img, lower_green, upper_green)

    points.append(point)
    if len(points) != 0:
        draw(points, green)
    # Show result
    cv.imshow('img', img)
    if cv.waitKey(1) & 0xFF == ord(' '):
        break
