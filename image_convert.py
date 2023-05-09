#!/usr/bin/env python3

import os
from PIL import Image

# assign directory of images
directory = '/Users/joshuapetry/images/'
export_path = '/Users/joshuapetry/images_new/'

# iterate over files in
# that directory
for file in os.listdir(directory):
    with Image.open(directory + file) as im:
        filename = file + ".jpg"
        im_rotated = im.rotate(-90)
        im_resized = im_rotated.resize((128, 128))
        im_rgb = im_resized.convert('RGB')
        im_rgb.save((export_path) + filename)
