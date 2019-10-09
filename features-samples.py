import argparse

import cv2

from alcm.method import get_text_components, get_avg_text_height

if __name__ == '__main__':
    # img = cv2.imread('demo/local/rotated.jpg', cv2.IMREAD_GRAYSCALE)
    # img = cv2.imread('demo/local/slanted.png', cv2.IMREAD_GRAYSCALE)

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image", help="use specific image in data path", type=str, default=None, required=True)
    args = parser.parse_args()
    # show overdraw components
    input_image = cv2.imread(args.image, cv2.IMREAD_GRAYSCALE)
    alcm_th = get_text_components(input_image)
    # global avg, doesn't recognize if there's a midzone or not
    height = get_avg_text_height(alcm_th)
    print("Detected average height of text line in pixels: {}".format(height))
