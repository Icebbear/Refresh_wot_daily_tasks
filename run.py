# -*- coding: utf-8 -*-
# @PROJECT : ref 
# @Time    : 2024/3/13 11:15
# @File    : run.py
# @Author  : icebbear
# Description:
# --------------------
from ref import RefreshMessions

coord_refresh1 = (1010, 580)
coord_refresh2 = (1454, 580)
coord_refresh3 = (1897, 580)
coord_mession1 = (850, 771)
coord_mession2 = (1302, 771)
coord_mession3 = (1839, 771)
enter_cooord = (1, 1)
shot_size = (61, 62)

coord = [[coord_mession1, coord_refresh1], [coord_mession2, coord_refresh2], [coord_mession3, coord_refresh3]]

re = RefreshMessions()
for param in coord[::-1]:
    print(param)
    shot_path = r"./shot_images/x{}.png".format(coord.index(param))
    re.shot_images(param[0], shot_size, shot_path)
    result = re.comparison_images(blueprint_image_path=r"./model_images/blueprint_image.png",
                                  shot_image_path=shot_path)

    if result:
        continue
    else:
        re.click_refresh(param[1], enter_cooord, 2)
        break
