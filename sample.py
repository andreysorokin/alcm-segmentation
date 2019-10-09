import cv2
import numpy as np

from alcm.method import get_text_components, enumerate_components
from alcm.utils import get_avg_height_sliced


def color_code_enumerated(labeled_img):
    label_hue = np.uint8(200 * enumerated / np.max(enumerated))
    blank_ch = 255 * np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)
    labeled_img[label_hue == 0] = 0
    return labeled_img


if __name__ == '__main__':
    # c = 80 !!!
    # img = cv2.imread('demo/local/slanted.png', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('demo/local/letter0.png', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('demo/local/letter1.png', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('demo/local/rotated.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.imread('demo/p03-033.png', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('demo/p03-080.png', cv2.IMREAD_GRAYSCALE)
    # show overdraw components
    alcm_th = get_text_components(img)
    enumerated = enumerate_components(img, alcm_th)
    code_enumerated = color_code_enumerated(enumerated)
    cv2.imshow('ALCM', code_enumerated)
    cv2.waitKey()