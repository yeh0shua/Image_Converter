# Image Converter

Image Converter is a Python program that transforms images according to 
certain specifications.

The program requires the following modules:
os
sys
Path
Image

# Usage

Call ./image_convert [source dir] [destination dir]

The program will make the following transformations to the image files in 
the source dir:

Rotate each image -90 degrees
Resize each image to 128 x 128
Convert each image to RGB
Save each image with file ext .jpeg
