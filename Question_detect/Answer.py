import cv2 as cv
import imutils
from Image import Image
import math


class Answer(Image):
    def __init__(self, path):
        super(Answer, self).__init__(path)
        self.points = []

    def find_contours(self):
        """
        return all contours of answer box with dilate iterations = 2
        """
        contours, _ = cv.findContours(self.dilate_img(1), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

        answer_box_cnts = []
        for cnt in contours:
            x, y, w, h = cv.boundingRect(cnt)
            if h > 100 and 800 < w < 1600:
                answer_box_cnts.append(cnt)
        return answer_box_cnts

    # def get_contours(self):
    #     contours, hierarchy = cv.findContours(self.dilate_img(1), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    #     for i in range(len(contours)):
    #         x, y, w, h = cv.boundingRect(contours[i])
    #         if h > 100 and 800 < w < 1600:
    #             # cv.drawContours(self.img, cnt, -1, (0, 0, 255), 3)
    #             x = tuple((contours[i], hierarchy[0][i]))
    #             c = imutils.grab_contours(x)
    #             # c = max(cnt, key=cv.contourArea)
    #             # c1 = min(cnt, key=cv.contourArea)
    #
    #             # determine the most extreme points along the contour
    #             ext_left = tuple(c[c[:, :, 0].argmin()][0])
    #             ext_right = tuple(c[c[:, :, 0].argmax()][0])
    #             ext_top = tuple(c[c[:, :, 1].argmin()][0])
    #             ext_bottom = tuple(c[c[:, :, 1].argmax()][0])
    #
    #             cv.drawContours(self.img, [c], -1, (0, 255, 255), 2)
    #             cv.circle(self.img, ext_left, 8, (0, 0, 255), -1)
    #             cv.circle(self.img, ext_right, 8, (0, 255, 0), -1)
    #             cv.circle(self.img, ext_top, 8, (255, 0, 0), -1)
    #             cv.circle(self.img, ext_bottom, 8, (255, 255, 0), -1)

    def draw_rect(self):
        """
        draw bounding boxes contain the contours were found by dilate iterations = 2
        """
        contours = self.find_contours()
        for cnt in contours:
            x, y, w, h = cv.boundingRect(cnt)
            x2, y2 = x + w, y + h
            cv.rectangle(self.img, (x, y), (x2, y2), (0, 0, 255), 3)

    def draw_contours(self, contours: list):
        """
        draw all contours were found by dilate iterations = 2
        params:
            - contours: list, the contours which you want to draw
        """

        for cnt in contours:
            cv.drawContours(self.img, cnt, -1, (0, 0, 255), 3)

    def draw_tick(self):
        """
        draw ticks with the known coordinates
        """
        points = [(600, 1750),
                  (600, 1220),
                  (600, 900),
                  (600, 700),
                  (600, 500),
                  (1000, 500),
                  (1000, 700),
                  (1000, 900),
                  (1000, 1250),
                  (1000, 1750)]
        for point in points:
            cv.circle(self.img, point, radius=15, color=(0, 0, 255), thickness=-1)
        self.points = points

    def filter_answer_box(self):
        """
        filter all answers box contain ticks
        """

        contours = self.find_contours()
        filtered_contours = []
        for cnt in contours:
            for point in self.points:
                if cv.pointPolygonTest(cnt, point, True) >= 0:
                    filtered_contours.append(cnt)
                    continue

        return filtered_contours


image_1 = Answer('./data/images/2.png')
image_1.draw_tick()
contours_1 = image_1.filter_answer_box()
# contours_1 = image_1.find_contours()
image_1.draw_contours(contours_1)
# image_1.get_contours()
image_1.show_img()
