import cv2 as cv
from Image import Image


class Text(Image):
    def __init__(self, path):
        super(Text, self).__init__(path)

    def find_contours(self):
        """
        find and return all contours with iterations = 6 and iterations = 1
        """
        # # iterations = 6
        # contours_big, hierarchy = cv.findContours(self.dilate_img(6), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        # #iterations = 1
        # contours_small, _ = cv.findContours(self.dilate_img(1), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        #
        # return contours_big, contours_small

        contours, _ = cv.findContours(self.dilate_img(6), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
        text_cnts = []
        for cnt in contours:
            x, y, w, h = cv.boundingRect(cnt)
            x2, y2 = x + w, y + h
            if h < 60:
                text_cnts.append(cnt)
        return text_cnts

    def draw_rect(self):
        """
        draw the rectangle around each contour in a copy img
        """
        # contours_big, contours_small = self.find_contours()
        # for cnt_b in contours_big:
        #     x_b, y_b, w_b, h_b = cv.boundingRect(cnt_b)
        #     x_b2, y_b2 = x_b + w_b, y_b + h_b
        #     for cnt_s in contours_small:
        #         if h_b < 60:
        #             cv.rectangle(self.img, (x_b, y_b), (x_b2, y_b2), (0, 0, 255), 3)
        #             x_s, y_s, w_s, h_s = cv.boundingRect(cnt_s)
        #             if h_s < 60 :
        #                 x_s2, y_s2 = x_s + w_s, y_s + h_s
        #                 cv.rectangle(self.img, (x_s, y_s), (x_s2, y_s2), (0, 0, 255), 3)

        contours = self.find_contours()
        for cnt in contours:
            x, y, w, h = cv.boundingRect(cnt)
            x2, y2 = x + w, y + h

            cv.rectangle(self.img, (x, y), (x2, y2), (0, 0, 255), 3)


image_1 = Text('./data/images/0.png')

image_1.draw_rect()
image_1.show_img()

