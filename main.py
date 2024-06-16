"""
Library: rembg to import remove
    - Popular python library to remove background.
"""
from rembg import remove

"""
The Python Imaging Library (PIL), now maintained under the name Pillow, is a library used for opening, 
manipulating, and saving many different image file formats.
"""
from PIL import Image

image_path = '-path-'
image_path_removebg = '-path-'

taking_image = Image.open(image_path)
giving_image = remove(taking_image)
giving_image.save(image_path_removebg)