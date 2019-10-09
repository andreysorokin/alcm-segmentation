import cv2

from alcm.method import get_text_components, enumerate_components
from alcm.utils import color_code_enumerated

if __name__ == '__main__':
    # c = 80 !!!
    img = cv2.imread('demo/local/slanted.png', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('demo/local/letter0.png', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('demo/local/letter1.png', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('demo/local/rotated.jpg', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('demo/p03-033.png', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('demo/p03-080.png', cv2.IMREAD_GRAYSCALE)
    # show overdraw components
    alcm_th = get_text_components(img)
    cv2.imshow('ALCM', alcm_th)
    cv2.waitKey()
    enumerated = enumerate_components(img, alcm_th)
    # enumerated = enumerate_components(img, alcm_th, True)

    code_enumerated = color_code_enumerated(enumerated)
    cv2.imshow('ALCM', code_enumerated)
    cv2.waitKey()
