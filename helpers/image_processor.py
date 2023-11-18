import cv2
import numpy as np
from pytesseract import image_to_data, Output

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

