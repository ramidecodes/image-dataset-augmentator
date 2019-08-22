from PIL import Image

def get_image_size(image_path):
    return Image.open(image_path).size

def calculate_ajusted_width(output_height, image_path):
    original_width, original_height = get_image_size(image_path)
    adjusted_width = output_height * original_width / original_height
    return int(adjusted_width)