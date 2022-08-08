"""
    A simple script to transform an image to ANSI art
"""

from PIL import Image
import numpy as np
import argparse

# list of characters used, they represend a greyscale of 40 values
chars = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft"[::-1])

def parse_arguments():
    """
        Parsing the command-line arguments of the script
    """
    parser = argparse.ArgumentParser(description="Converting images to ANSI art")
    parser.add_argument('-i', dest='image_path', help="The image file to be displayed", default=None)
    parser.add_argument('-w', dest='width', help="The width of the ANSI image", default=100)
    parser.add_argument('-f', dest='full', help="Wheter or not the foreground of a character is formated", default=False)

    args = parser.parse_args()
    if args.image_path is None:
        print("The path is required!")
        exit(0)

    return args.image_path, args.width, args.full

def char_to_esc_seq(char, bg, fg, full):
    """
        Formating a character to correspond to a given pixel
    """
    esc = "\x1b["

    if full:
        out = f'{esc}48;2;{bg[0]};{bg[1]};{bg[2]}m{esc}38;2;{fg[0]};{fg[1]};{fg[2]}m{char}\x1b[0m'
    else:
        out = f'{esc}48;2;{bg[0]};{bg[1]};{bg[2]}m{char}\x1b[0m'

    return out

def rezise_image(image, new_width):
    """
        Resize the image while maintaining the aspect ratio
    """
    ratio = image.size[1] / image.size[0] / 1.65
    new_height = int(float(new_width) * ratio)
    new_image = image.resize((int(new_width), new_height))

    return new_image

def image_to_ascii(image, full):
    """
        Convert the image to an ASCII representation
    """
    pixels = np.array(image.getdata())
    text = ""
    for y in range(image.size[1]):
        for x in range(image.size[0]):
            idx = y*image.size[0]+x
            if idx < pixels.shape[0]:
                # getting the pixel color data
                pixel = pixels[idx]

                # get the character which most closely ressembles the pixel's mean color data
                text += char_to_esc_seq(chars[int(pixel.mean()//6.4)], pixel, pixel, full)
        text += '\n'

    return text

def main():
    """
        Main entry point of application
    """
    image_path, width, full = parse_arguments()
    image = Image.open(image_path)

    new_image = image_to_ascii(rezise_image(image, width), full).strip()

    with open("ascii_im.txt", "w") as f:
        f.write(new_image)

    print(new_image)

if __name__ == "__main__":
    main()