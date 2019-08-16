"""
@author: Ramiro Ramirez

Process each image in a directory and outputs a new dataset with the selected transformations.
"""

import os
import Augmentor
import argparse

# Add CLI argument parser
parser = argparse.ArgumentParser(description='Process each image in a directory and outputs a new dataset with the transformations.')
parser.add_argument("--input_dir", default="./dataset/input", help="path to directory containing the images")
# parser.add_argument("--output_dir", default="./dataset/output", help="path to directory to save new images")

# TODO Add argument to use image pairs as input (to process cGAN datasets)

a = parser.parse_args()

# Build local OS directory path
# in_path = os.path.dirname(a.input_dir)
# out_path = os.path.dirname(a.output_dir)

# Create output path if doesn't exist
# if os.path.exists(out_path) == False:
#     os.makedirs(out_path)

# Create an augmentation pipeline
p = Augmentor.Pipeline(a.input_dir)

# Define the transformations
p.rotate90(probability=0.5)
p.rotate270(probability=0.5)
p.flip_left_right(probability=1)
p.flip_top_bottom(probability=1)
p.crop_random(probability=.8, percentage_area=0.8)
p.resize(probability=1, width=512, height=512)

# Generate new augmented images
p.status()
p.sample(500)