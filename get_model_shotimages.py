# -*- coding: utf-8 -*-
# @PROJECT : ref 
# @Time    : 2024/3/13 11:16
# @File    : get_model_shotimages.py
# @Author  : icebbear
# Description:
# --------------------
from ref import RefreshMessions

if __name__ == '__main__':
    ref = RefreshMessions()

    coord_mession1 = (850, 771)
    coord_mession2 = (1302, 771)
    coord_mession3 = (1839, 771)
    shot_size = (61, 62)

    # def get_shot(coord_mession, size, file_path):
    #     mession = ref.integrate_param(coord_mession, size)
    #     ref.shot_images(mession, file_path)

    ref.shot_images(coord_mession3, shot_size, "model_images/blueprint_image.png")
