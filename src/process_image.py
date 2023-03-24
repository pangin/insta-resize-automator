from PIL import Image

import os


WIDTH_INDEX = 0
HEIGHT_INDEX = 1
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)


def get_bigger_axis_image_size(image_size: tuple):
    width = image_size[WIDTH_INDEX]
    height = image_size[HEIGHT_INDEX]

    if width <= height:
        return height
    elif height < width:
        return width
    else:
        raise Exception(
            '@get_longer_axis_image_size: Can not figure out which axis of image is bigger!')


def get_new_square_image_size(image_size: tuple):
    bigger_image_size = get_bigger_axis_image_size(image_size)

    return (bigger_image_size, bigger_image_size)


def generate_square_image_with_border(original_image_name, border_color: tuple | None):
    if border_color == None:
        border_color = COLOR_WHITE

    original_image = Image.open(original_image_name)

    new_square_image_size = get_new_square_image_size(original_image.size)
    new_square_image = Image.new(
        'RGB', size=new_square_image_size, color=border_color)
    box = tuple((n - o) // 2 for n,
                o in zip(new_square_image_size, original_image.size))
    new_square_image.paste(original_image, box)
    new_square_image.save(f'..\output\{original_image_name}_bordered.jpg')


def generate_image_with_border(original_image_name: str, mode: str | None, border_color: tuple | None):

    if mode == None:
        mode = 'square'

    if mode == 'square':
        generate_square_image_with_border(
            original_image_name=original_image_name, border_color=border_color)
