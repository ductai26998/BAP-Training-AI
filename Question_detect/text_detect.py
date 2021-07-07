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

    def resize(self, width=600, height=500):
        """
        resize image follow width and height size
        """
        x = self.get_shape()
        return cv.resize(self.img, (x[0] // 3, x[1] // 3))

    def copy_img(self):
        """
        copy image
        """
        return np.copy(self.img)

    def show_img(self):
        """
        Show self.img as image on your screen
        """
        cv.imshow('result', self.resize())
        # cv.imshow('result', self.img)
        cv.waitKey()

    def get_shape(self):
        """
        Return a tuple (height, width) size of img vector
        """
        return self.img.shape

    def convert_image(self, fun):
        """
        convert BGR image to other type image by fun
        """
        return cv.cvtColor(self.img, fun)

    def detect_edge(self):
        """
        detect all edges on image
        """
        return cv.Canny(self.img, 100, 200)

    def dilate_img(self, iterations: int = 2):
        """
        dilates the image
        """
        return cv.dilate(self.detect_edge(), self.kernel, iterations=iterations)

    def erode_img(self, iterations: int = 1):
        """
        erodes the image
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


class Text(Image):
    def __init__(self, img):
        super(Text, self).__init__(img)

    def find_contours(self):
        """
        find and return all contours with iterations = 6 and iterations = 1
        """
        # iterations = 6
        contours_big, hierarchy = cv.findContours(self.dilate_img(6), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        #iterations = 1
        contours_small, _ = cv.findContours(self.dilate_img(1), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

        return contours_big, contours_small

    def draw_rect(self):
        """
        draw the rectangle around each contour in a copy img
        """
        contours_big, contours_small = self.find_contours()
        for cnt_b in contours_big:
            x_b, y_b, w_b, h_b = cv.boundingRect(cnt_b)
            x_b2, y_b2 = x_b + w_b, y_b + h_b
            for cnt_s in contours_small:
                if h_b < 60:
                    cv.rectangle(self.img, (x_b, y_b), (x_b2, y_b2), (0, 0, 255), 3)
                    x_s, y_s, w_s, h_s = cv.boundingRect(cnt_s)
                    if h_s < 60 and x_b + 600 < x_s and y_b + 600 < y_s:
                        x_s2, y_s2 = x_s + w_s, y_s + h_s
                        cv.rectangle(self.img, (x_s, y_s), (x_s2, y_s2), (0, 0, 255), 3)


    # def detect_text(self):
    #     for cnt in self.find_contours():
    #         x, y, w, h = cv.boundingRect(cnt)
    #         x2, y2 = x + w, y + h
    #         cv.rectangle(self.img, (x, y), (x2, y2), (0, 0, 255), 3)


class Answer_box(Image):
    def __init__(self):
        super()


image_1 = Text('./data/images/0.png')

image_1.draw_rect()
image_1.show_img()

