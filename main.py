import os
import glob

from src import process_image


if __name__ == '__main__':
    os.chdir('.\input')
    for original_image_name in glob.glob('*.jpg'):
        process_image.generate_image_with_border(
            original_image_name=original_image_name, mode=None, border_color=None)
