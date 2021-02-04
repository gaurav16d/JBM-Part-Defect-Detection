# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 19:41:40 2021

@author: Gaurav Gosain
"""


from PIL import Image
import numpy as np

import pathlib
import PIL
import PIL.Image
data_dir = r"C:\Users\Gaurav Gosain\Desktop\Important Docs\JBM Assignment\J2 Images New Set up At 230 mm Height"
data_dir = pathlib.Path(data_dir)
part_numbers = [part_numbers for part_numbers in data_dir.iterdir() if part_numbers.is_dir()]

good_parts = ['']*500
bad_parts = ['']*500
good_part_counter = 0
bad_part_counter = 0

for part in part_numbers:
    good_images = len(list(part.glob('Good/*')))
    good_parts[good_part_counter:good_part_counter+good_images-1] = list(part.glob('Good/*'))
    good_part_counter = good_part_counter + good_images
    
    bad_images = len(list(part.glob('Bad/*')))
    bad_parts[bad_part_counter:bad_part_counter+bad_images-1] = list(part.glob('Bad/*'))
    bad_part_counter = bad_part_counter + bad_images    


good_parts = good_parts[0:good_part_counter-1]
bad_parts = bad_parts[0:bad_part_counter-1]

### Move Good and Bad Images to one folder for Tensorflow
import os
import shutil
good_part_directory = r"C:\Users\Gaurav Gosain\Desktop\Important Docs\JBM Assignment\Clubbed Classified Directory\Good"
bad_part_directory = r"C:\Users\Gaurav Gosain\Desktop\Important Docs\JBM Assignment\Clubbed Classified Directory\Bad"

for image in good_parts:
    image_path = os.path.join(image)
    shutil.copy(image_path,good_part_directory)
 
for image in bad_parts:
    image_path = os.path.join(image)
    shutil.copy(image_path,bad_part_directory)




