import cv2
import numpy as np
from pytesseract import image_to_data, Output
import matplotlib.colors as colors

class ImageProcessor:
    @staticmethod
    def find_by_text(image, keyword):
        img_cv2 = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        text = image_to_data(img_cv2, output_type=Output.DICT, lang='eng')
        indices = [i for i, word in enumerate(text['text']) if keyword in word.lower()]

        if len(indices) == 0:
            return None

        index = indices[0]
        x, y, w, h = text['left'][index], text['top'][index], text['width'][index], text['height'][index]
        return x + w // 2, y + h // 2

    @staticmethod
    def find_pixel(image, line, color):
        img_cv2 = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        pixel_line = img_cv2[line, :]
        indices = np.where((pixel_line == color).all(axis=1))[0]

        if len(indices) == 0:
            return None

        x = indices[0]
        return x, line

    @staticmethod
    def get_pixel_color(image, x, y):
        img_cv2 = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        color = img_cv2[y, x]
        color_rgb = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_BGR2RGB)
        color_hex = colors.rgb2hex(color_rgb[0][0] / 255)
        return color_hex

    @staticmethod
    def get_screen_size(image):
        img_cv2 = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        height, width, _ = img_cv2.shape
        return width, height
