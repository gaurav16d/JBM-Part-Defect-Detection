# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 02:04:05 2021

@author: Gaurav Gosain
"""

import os
import shutil
import pathlib

good_part_directory = r'C:\Users\Gaurav Gosain\Desktop\Important Docs\JBM Assignment\Clubbed Classified Directory\Good'
bad_part_directory = r'C:\Users\Gaurav Gosain\Desktop\Important Docs\JBM Assignment\Clubbed Classified Directory\Bad'

good_image_names = os.listdir(good_part_directory)
bad_image_names = os.listdir(bad_part_directory)

path = bad_part_directory
save_path = r'C:\Users\Gaurav Gosain\Desktop\Important Docs\JBM Assignment\Clubbed Classified Directory - Copy\Bad'

"""
for index, file in enumerate(good_image_names):
    os.rename(os.path.join(path, file), os.path.join(path,file.join(['good', '.jpeg'])))
"""
from PIL import Image
import numpy as np
import re

# Import Image:
for image_name in bad_image_names:
    img = Image.open(os.path.join(bad_part_directory,image_name))
    width, height = img.size
    if height>width:
        img = img.rotate(90, Image.NEAREST, expand = 1) 
    img_small = img.resize((512,512)) 
    image_name = re.sub(r".tif", "",image_name)
    img_small.save(os.path.join(save_path, image_name.join(['Bad', '.jpeg'])))

