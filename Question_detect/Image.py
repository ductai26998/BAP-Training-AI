import cv2 as cv
import numpy as np


class Image:
    def __init__(self, path):
        self.path = path
        self.img = self.read_img()
        self.kernel = np.ones((3, 3), dtype=np.uint8)

    def read_img(self):
        """
        Read image from self.path and return a vector
        """
        return cv.imread(self.path)  # default: BGR image

    def resize(self, width: int = 600, height: int = 500):
        """
        resize image follow width and height size
        params:
            - width: int, width of image which you want to resize
            - height int, height of image which you want to resize
        """
        x = self.get_shape()
        return cv.resize(self.img, (width, height))

    def copy_img(self):
        """
        copy image
        """
        return np.copy(self.img)

    def show_img(self):
        """
        Show self.img as image on your screen
        """
        cv.imshow('result', self.resize(800, 800))
        cv.waitKey()

    def get_shape(self):
        """
        Return a tuple (height, width) size of img vector
        """
        return self.img.shape

    def convert_image(self, function):
        """
        convert BGR image to other type image by function
        """
        return cv.cvtColor(self.img, function)

    def detect_edge(self):
        """
        detect all edges on image
        """
        return cv.Canny(self.img, 100, 200)

    def dilate_img(self, iterations: int = 2):
        """
        dilates the image
        params:
            - iterations: int, numbers of iteration put into dilate function
        """
        return cv.dilate(self.detect_edge(), self.kernel, iterations=iterations)

    def erode_img(self, iterations: int = 1):
        """
        erodes the image
        params:
            - iterations: int, numbers of iteration put into erode function
        """
        return cv.erode(self.dilate_img(), self.kernel, iterations=iterations)

    def find_contours(self):
        """
        find all contours in image was detected edge
        """
        contours, hierarchy = cv.findContours(self.detect_edge(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        return contours

    def draw_rect(self):
        """
        draw the rectangle around each contour in a copy img
        """
        for cnt in self.find_contours():
            x, y, w, h = cv.boundingRect(cnt)
            x2, y2 = x + w, y + h
            cv.rectangle(self.img, (x, y), (x2, y2), (0, 0, 255), 3)