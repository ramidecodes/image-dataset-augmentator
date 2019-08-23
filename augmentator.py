#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Ramiro Ramirez

Process each image in a directory and outputs a new dataset with the selected transformations.
"""

import os, os.path
import Augmentor
import argparse
import pprint
from utils import calculate_ajusted_width, rename_files

# Add CLI argument parser
parser = argparse.ArgumentParser(description="Process each image in a directory and outputs a new dataset with the transformations.")
parser.add_argument("--input_dir", default="../datasets/databetes/gummybears_macro", help="path to directory containing the images")
parser.add_argument("--output_dir", default="../datasets/databetes/gummybears_macro/output", help="path to directory to save new images")
parser.add_argument("--output_format", default="JPEG", choices=["JPEG","BMP","PNG","GIF"], help="output image format")
parser.add_argument("--output_width", default=512, help="output image width in pixels")
parser.add_argument("--output_height", default=512, help="output image height in pixels")
parser.add_argument("--resample_filter", default="BICUBIC", choices=["BICUBIC","BILINEAR","ANTIALIAS","NEAREST"], help="filter to use when resampling")
parser.add_argument("--zoom", action="store_true", help="zoom in randomly")
parser.add_argument("--distortion", action="store_true", help="distort randomly")
parser.add_argument("--sample_count", default=100, help="amount of new images to generate")
parser.add_argument("--output_prefix", default="augmented", help="A prefix to be added to all the images with the format 'prefix_00001")


# TODO Add argument to use image pairs as input (to process cGAN datasets)

a = parser.parse_args()

# Get image count
# image_count = len([name for name in os.listdir(a.input_dir) if os.path.isfile(name)])

# Create pipeline to resize original images and add them to the newly created augmented images
resize_pipe = Augmentor.Pipeline(source_directory=a.input_dir, output_directory=a.output_dir, save_format=a.output_format)

# Calculate the resized with based on the original size and desired image height output
adjusted_width = calculate_ajusted_width(a.output_height, resize_pipe.augmentor_images[0].image_path)
# Resize to desired Heigh preserving original aspect ratio
resize_pipe.resize(probability=1, width=adjusted_width, height=a.output_height, resample_filter=a.resample_filter)

# Crop to the desired with and hight from the center
resize_pipe.crop_by_size(probability=1, width=a.output_width, height=a.output_height, centre=False)

# Print changes and status
resize_pipe.status()

# Generate the exact amount of original images resized to the given withd and size
resize_pipe.sample(len(resize_pipe.augmentor_images))

# Create pipeline to generate the modifided images
augment_pipe = Augmentor.Pipeline(source_directory=a.input_dir, output_directory=a.output_dir, save_format=a.output_format)


# Define the transformations

# augment_pipe.rotate90(probability=0.5)
# augment_pipe.rotate270(probability=0.5)
# augment_pipe.flip_left_right(probability=1)
# augment_pipe.flip_top_bottom(probability=1)


if a.zoom:
    augment_pipe.zoom_random(probability=1, percentage_area=0.6, randomise_percentage_area=False)
    # augment_pipe.zoom(probability=1, min_factor=1.1, max_factor=1.5)

if a.distortion:
    augment_pipe.random_distortion(probability=1, grid_width=10, grid_height=10, magnitude=12)

augment_pipe.resize(probability=1, width=adjusted_width, height=a.output_height, resample_filter=a.resample_filter)
augment_pipe.crop_by_size(probability=1, width=a.output_width, height=a.output_height, centre=False)

# Generate new augmented images
augment_pipe.status()
augment_pipe.sample(int(a.sample_count))

print("Renaming augmented files using the prefix ", a.output_prefix)
rename_files(a.output_prefix, a.output_dir, a.output_format)