"""Utility functions for dealing with source files, 2D binary arrays, and 1D
bipolar patterns.
"""

import os
import numpy as np
from PIL import Image


def load_images(images_dir, file_names, shape=(32, 32), threshold=100):
    """Return a list of binary image arrays for the given image directory and
    list of file names.
    """

    def _load(path):
        im = np.array(Image.open(path).convert("LA").resize(shape))[:, :, 0]
        return np.where(im < threshold, 0.0, 1.0)

    return [_load(os.path.join(images_dir, f)) for f in file_names]


def display_image(im, shape=(256, 256)):
    """Given a binary array, return a Pillow image object for further
    manipulation or display.
    """
    return Image.fromarray(im.astype(bool)).resize(shape)


def flip_bits(a, nflip):
    """Flip `nflip` randomly chosen elements in the given binary array.
    """
    a_flat = a.copy().ravel()
    idx = np.random.choice(a_flat.size, nflip, replace=False)
    a_flat[idx] = np.logical_not(a_flat[idx])
    return a_flat.reshape(a.shape)
