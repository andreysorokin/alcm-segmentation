import numpy as np


def get_avg_height(thresholded_img):
    th = thresholded_img.copy()
    h, w = th.shape
    th[th == 0] = 1
    # Convert white spots to zeros
    th[th == 255] = 0

    vertical_profile = np.sum(th, axis=1)
    return get_avg_height_from_profile(vertical_profile)


def get_avg_height_sliced(thresholded_img, slice_count=20):
    """
    analyzes 20 slices per document width and averages profile line height in each of the slides
    :param thresholded_img:
    :param slice_count:
    :return:
    """
    th = thresholded_img.copy()
    h, w = th.shape
    th[th == 0] = 1
    # Convert white spots to zeros
    th[th == 255] = 0

    # Step 1. Split widths in 20 chunks
    width = int(w / slice_count)
    avg_height = 0
    for p in range(0, slice_count):
        left = p * width
        right = (p + 1) * width
        right = min(right, w) - 1
        slice = th[:, left:right]
        vertical_profile = np.sum(slice, axis=1)
        avg_height += get_avg_height_from_profile(vertical_profile)

    return int(avg_height / slice_count)


def get_avg_height_from_profile(hist):
    """
    :deprecated
    :param th:
    :return:
    """
    # todo make zero valley threshold configurable
    zero_valley = np.max(hist) * 0.05
    R = len(hist) - 1
    uppers = [y for y in range(R) if hist[y] <= zero_valley < hist[y + 1]]
    lowers = [y for y in range(R) if hist[y] > zero_valley >= hist[y + 1]]

    while (len(lowers) > len(uppers)):
        lowers.pop(0)

    if len(lowers) != len(uppers) or len(uppers) == 0:
        return 0
    return np.average(np.array(lowers) - np.array(uppers))
