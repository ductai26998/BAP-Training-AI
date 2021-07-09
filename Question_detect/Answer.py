import cv2 as cv
import numpy as np
from Image import Image


class Answer(Image):
    def __init__(self, path):
        super(Answer, self).__init__(path)
        self.points = []

    def find_contours(self):
        """
        return all contours of answer box with dilate iterations = 2
        """
        contours, _ = cv.findContours(self.dilate_img(2), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        answer_box_cnts = []
        for cnt in contours:
            x, y, w, h = cv.boundingRect(cnt)
            if h > 100 and 800 < w < 1600:
                answer_box_cnts.append(cnt)
        return answer_box_cnts

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
            x, y, w, h = cv.boundingRect(cnt)

            # if h > 100 and 800 < w < 1600:
            cv.drawContours(self.img, cnt, -1, (0, 0, 255), 3)

        # for cnt in contours:
        #     x, y, w, h = cv.boundingRect(cnt)
        #     a, b, c = cnt.shape
        #     std_up = cnt[:(a//2),0,1].mean(axis=0)
        #     min_up = cnt[:(a//2),0,1].min(axis=0)
        #
        #     std_down = cnt[(a//2):,0,1].mean(axis=0)
        #     max_down = cnt[(a//2):,0,1].max(axis=0)
        #     for i in range(a//2):
        #         u = cnt[i, 0, 1]
        #         if cnt[i, 0, 1] > std_up:
        #             cnt[i, 0, 1] = min_up
        #     for i in range(a//2, a):
        #         if cnt[i, 0, 1] < std_down:
        #             cnt[i, 0, 1] = max_down
        #     if h > 100 and 800 < w < 1600:
        #         cv.drawContours(self.img, cnt, -1, (0, 0, 255), 3)

    def draw_tick(self):
        """
        draw ticks with the known coordinates
        """
        points = [(600, 1750),
                  (600, 1300),
                  (600, 900),
                  (600, 700),
                  (600, 600),
                  (1000, 500),
                  (1000, 700),
                  (1000, 900),
                  (1000, 1200),
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
            x, y, w, h = cv.boundingRect(cnt)

            if h > 100 and 800 < w < 1600:
                for point in self.points:
                    if x <= point[0] <= x + w and y <= point[1] <= y + h:
                        filtered_contours.append(cnt)
                        continue

        return filtered_contours


image_1 = Answer('./data/images/7.png')
image_1.draw_tick()
contours_1 = image_1.filter_answer_box()
image_1.draw_contours(contours_1)
image_1.show_img()
