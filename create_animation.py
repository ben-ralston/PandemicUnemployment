"""
Author: Ben Ralston
Date: 2020-11-20

Description: This script reads nine TIFF files named map_#.tiff (where
# is a number between 1 and 9) and stitches them together to create
Pandemic_Unemployment.gif, an animated GIF.
"""

import imageio


def main():
    filenames = ['map_%d.tiff' % i for i in range(1, 10)]
    images = []

    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave('Pandemic_Unemployment.gif', images, duration=1)


if __name__ == '__main__':
    main()
