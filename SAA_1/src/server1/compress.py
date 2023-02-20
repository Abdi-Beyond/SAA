#!/usr/bin/env python3
from PIL import Image
import datetime
# Load the image
def compress_image(file):
    
    output_path = 'compressed/compressed_image' + '.jpg'
    input_image = Image.open(file)


    # Compress the image using JPEG format  
    input_image.save(output_path, optimize=True, quality=65)
