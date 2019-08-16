#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ramiro Ramirez

Process each image in a directory and outputs a new dataset with the selected transformations.
"""

import os
import Augmentor
import argparse

# Add CLI argument parser
parser = argparse.ArgumentParser(description="Process each image in a directory and outputs a new dataset with the transformations.")
parser.add_argument("--input_dir", default="../datasets/databetes/gummybears_macro", help="path to directory containing the images")
parser.add_argument("--output_dir", default="../datasets/databetes/gummybears_macro/output", help="path to directory to save new images")
parser.add_argument("--output_format", default="JPEG", choices=["JPEG","BMP","PNG","GIF"], help="output image format (JPEG|BMP|PNG|GIF)")
parser.add_argument("--output_width", default=512, help="output image width in pixels")
parser.add_argument("--output_height", default=512, help="output image height in pixels")
parser.add_argument("--resample_filter", default="BICUBIC", choices=["BICUBIC","BILINEAR","ANTIALIAS","NEAREST"], help="filter to use when resampling (BICUBIC|BILINEAR|ANTIALIAS|NEAREST)")
parser.add_argument("--sample_count", default=100, help="amount of new images to generate")
parser.add_argument("--zoom", action="store_true", help="zoom in randomly")
parser.add_argument("--distortion", action="store_true", help="distort randomly")


# TODO Add argument to use image pairs as input (to process cGAN datasets)

a = parser.parse_args()

# Build local OS directory path
# in_path = os.path.dirname(a.input_dir)
# out_path = os.path.dirname(a.output_dir)

# Create output path if doesn"t exist
# if os.path.exists(out_path) == False:
#     os.makedirs(out_path)

# Create an augmentation pipeline
p = Augmentor.Pipeline(source_directory=a.input_dir, output_directory=a.output_dir, save_format=a.output_format)

# Define the transformations

# p.rotate90(probability=0.5)
# p.rotate270(probability=0.5)
# p.flip_left_right(probability=1)
# p.flip_top_bottom(probability=1)

p.crop_by_size(probability=1, width=a.output_width, height=a.output_height, centre=False)

if a.zoom:
    p.zoom_random(probability=1, percentage_area=0.7, randomise_percentage_area=False)
    # p.zoom(probability=1, min_factor=1.1, max_factor=1.5)

if a.distortion:
    p.random_distortion(probability=1, grid_width=10, grid_height=10, magnitude=12)

# p.resize(probability=1, width=a.output_width, height=a.output_height, resample_filter=a.resample_filter)

# Generate new augmented images
p.status()
p.sample(10)