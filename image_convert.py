#!/usr/bin/env python3

import os, sys
from pathlib import Path
from PIL import Image

# take input dir and output dir as sys arguments

indir = Path(sys.argv[1])
outdir = Path(sys.argv[2])

glob_path = indir.glob('*')
for infile in glob_path:
    try:
        with Image.open(infile) as im:
            outfile = str(infile).replace('images/', '') + '.jpeg'
            im_rotated = im.rotate(-90)
            im_resized = im_rotated.resize((128, 128))
            im_rgb = im_resized.convert('RGB')
            im_rgb.save(str(outdir) + '/' + outfile)
    except IOError:
        print(str(infile) + " is not an image file.")