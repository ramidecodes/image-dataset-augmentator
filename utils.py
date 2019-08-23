from PIL import Image
import os

def get_image_size(image_path):
    return Image.open(image_path).size

def calculate_ajusted_width(output_height, image_path):
    original_width, original_height = get_image_size(image_path)
    adjusted_width = output_height * original_width / original_height
    return int(adjusted_width)

def rename_files(prefix, dir_path, file_extension="jpeg"):
    filenames = os.listdir(dir_path)

    for index, filename in enumerate(filenames, start=1):
        # Build the filename string
        dst = prefix + '_' + str(index) + '.' + file_extension.lower()
        src = dir_path + '/' + filename 
        dst = dir_path + '/' + dst  
        os.rename(src, dst)

    return len(filenames)