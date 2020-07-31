# Author: sihan
# Date: 2019-12-24

import cv2
import numpy as np


def cut_shuffle_img(img, cut_size):
    #     img = cv2.cvtColor(origin, cv2.COLOR_BGR2RGB)
    h, w = img.shape[:2]

    re_w = (w // 10) * 10
    re_h = (h // 10) * 10

    img = cv2.resize(img, (re_w, re_h))

    row_loop = int(img.shape[0] / cut_size)
    column_loop = int(img.shape[1] / cut_size)

    # horizontal split
    hcuted = []
    for i in range(cut_size):
        hcuted.append(img[i * row_loop:i * row_loop + row_loop, :])

    # horizontal split merge
    hcut = []
    for i in range(0, cut_size, 2):
        hcut.extend(hcuted[i])

    for i in range(1, cut_size, 2):
        hcut.extend(hcuted[i])

    hcut.extend(hcuted[-1])

    # rotate img 90 degree
    hcut = np.asarray(hcut)

    dst = cv2.transpose(hcut)  # 행렬 변경
    dst = cv2.flip(dst, 1)

    # vertical split
    vcuted = []
    for i in range(cut_size):
        vcuted.append(dst[i * column_loop:i * column_loop + column_loop, :])

    # vertical merge
    vcut = []
    for i in range(0, cut_size, 2):
        vcut.extend(vcuted[i])

    for i in range(1, cut_size, 2):
        vcut.extend(vcuted[i])

    vcut.extend(vcuted[-1])

    # rotate img to origin shape
    vcut = np.asarray(vcut)

    dst = cv2.transpose(vcut)  # 행렬 변경
    result = cv2.flip(dst, 0)

    return result

