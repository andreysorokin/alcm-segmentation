import cv2
import numpy as np

from .utils import get_avg_height_sliced

def get_text_components(img_orig):
    """
    :param img_orig: must be a 300dpi image in any format compatible with opencv, black text on white background!
    :return: binary thresholded (alcm) image of the same size as input, which outlines connected components (words or lines)
    """
    h_orig, w_orig = img_orig.shape

    # Step 1 - resize 1/4 (1/2) on each size (in case input is 200-300 dpi) todo - interpolate!!!
    # todo do we really need scaling as per the paper?
    img = cv2.resize(img_orig, (int(w_orig / 2), int(h_orig / 2)))
    h, w = img.shape

    # Step 2 - Analyze string profile (estimate avg height of the line)
    ret, th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # th - is a source thresholded image, build a profile for it
    c = get_avg_height_sliced(th)

    # Step 3 - convolve with an impulse of length 2*c - this will propagate the intensity of the neighbouring pixels
    impulse_width = c * 2
    impulse = np.repeat(1, impulse_width)
    conv_img = np.empty((h, w))
    for y in range(0, h):
        padded = np.pad(img[y], impulse_width, 'constant', constant_values=255)
        conv_img[y] = np.convolve(padded, impulse, mode='same')[impulse_width: -impulse_width]

    max_value = np.max(conv_img)
    # normalize conv image
    conv_img = (255 * conv_img / max_value).astype(dtype=np.uint8)

    # Step 4 - Otsu binarization which can be applied to ALCM as it is a bi-modal image
    ret2, th2 = cv2.threshold(conv_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    th2 = cv2.bitwise_not(th2)
    connected_components = cv2.resize(th2, (w_orig, h_orig))
    return connected_components

    # # Step 5 - Analyze connected components
    # # show overdraw components
    # overlay = cv2.addWeighted(th, 0.8, th2, 0.2, 0)
    # cv2.imshow('ALCM', overlay)


def enumerate_components(img_orig, thresholded_alcm):
    """
    This will threshold the original image, use connected components of thresholded alcm as seed points and add all connected points of original image
    :param img_orig: original image, black text on white background
    :param thresholded_alcm: thresholded alcm
    :return: int map of the same size as original image where word components are enumerated with numbers 1 to N
    """
    _, th = cv2.threshold(img_orig, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    th = cv2.bitwise_not(th)
    _, labels_orig = cv2.connectedComponents(th)
    _, labels_alcm = cv2.connectedComponents(thresholded_alcm)
    N = np.max(labels_alcm)
    output_map = np.zeros(img_orig.shape, dtype=int)
    merged_original_labels = set()
    current_component_id = 1
    for label_idx in range(1, N+1):
        # Step 1: select all non-zero pixels of original image
        unique_labels = np.unique(labels_orig[labels_alcm == label_idx])

        before_size = len(merged_original_labels)
        for ul in unique_labels:
            if ul > 0 and not ul in merged_original_labels:
                merged_original_labels.add(ul)
                output_map[np.where(labels_orig == ul)] = current_component_id

        if len(merged_original_labels) > before_size:
            current_component_id += 1

    return output_map