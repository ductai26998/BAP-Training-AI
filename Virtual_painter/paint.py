import numpy as np
import cv2 as cv

def detect_color(img, thresholds):
    """
        detect color and return (x,y) coordinate of that point
        params:
            img: image_input
            lower_color: lower threshold of color
    """
    points = []
    # covert img to hsv image
    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    for i in range(len(thresholds)):
        # Threshold the HSV image to get only blue colors
        mask = cv.inRange(hsv_img, thresholds[i][0], thresholds[i][1])

        # get position of point
        x, y = get_position(mask)
        point = (x, y, i)
        points.append((point))
    return points

def draw(points, colors):
    for point in points:
        cv.circle(img, (point[0], point[1]), 10, colors[point[2]], -1)

def get_position(img):
    # find all contours in image
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for contour in contours:
        area = cv.contourArea(contour) # return numbers of pixel not 0
        if area > 500:
            # calculates a contour perimeter is closed
            p = cv.arcLength(contour, True)

            # Approximates a polygonal curve(s) with the specified precision
            approx = cv.approxPolyDP(contour, 0.1 * p, True)

            # Calculates the up-right bounding rectangle of a point set or non-zero pixels of gray-scale image.
            x, y , w, h = cv.boundingRect(approx)

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

# define range of red color in HSV
lower_red = np.array([0, 10, 100])
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

thresholds = [[lower_red, upper_red],
              [lower_green, upper_green],
              [lower_blue, upper_blue]]
colors = [red, green, blue]

while True:
    _, img = cap.read()

    # get points of 1 iterator
    item_points = detect_color(img, thresholds)

    if len(item_points) != 0:
        for new_point in item_points:
            points.append(new_point)
    if len(points) != 0:
        draw(points, colors)
    # Show result
    cv.imshow('img', img)
    if cv.waitKey(1) & 0xFF == ord(' '):
        break
