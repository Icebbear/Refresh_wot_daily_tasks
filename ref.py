# -*- coding: utf-8 -*-
# @PROJECT : ref 
# @Time    : 2024/3/12 13:30
# @File    : ref.py
# @Author  : icebbear
# Description:
# --------------------
from datetime import datetime

import cv2
import numpy as np
import pyautogui


class RefreshMessions:
    # def __init__(self):
    #     self.blueprint_image = cv2.imread("./model_images/experienc_image.png")
    #     # self.experienc_image = cv2.imread("./model_images/experienc_image.png")
    #     # self.silvercoin_image = cv2.imread("model_images/silvercoin_image.png")
    #     # self.bond_image = cv2.imread("model_images/bond_image.png")

    @staticmethod
    def shot_images(mession_coord, size, file_path: str):
        pyautogui.screenshot(region=mession_coord + size).save(file_path)

    @staticmethod
    def comparison_images(blueprint_image_path, shot_image_path):
        blueprint_image = cv2.imread(blueprint_image_path)
        shot_image = cv2.imread(shot_image_path)
        diff = cv2.subtract(blueprint_image, shot_image)
        result = not np.any(diff)
        return result

    @staticmethod
    def click_refresh(refresh_cooord, enter_cooord, wait_time):
        pyautogui.click(refresh_cooord[0], refresh_cooord[1], duration=wait_time)
        pyautogui.click(enter_cooord[0], enter_cooord[1], duration=wait_time)

    @staticmethod
    def integrate_param(coord, size):
        return coord + size

    # @staticmethod
    # def get_coord():
    #     s = pyautogui.size()
    #     x = s.width
    #     y = s.height
    #     coord = (x, y)
    #     return coord


if __name__ == '__main__':
    a = [1, 2, 3]
    for i in a[::-1]:
        print(a.index(i))