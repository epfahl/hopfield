"""Utility functions for dealing with source files, 2D binary arrays, and 1D
bipolar patterns.
"""

import numpy as np
from PIL import Image


def load_binary_image(path, shape, threshold):
    """Load an image file with the given path as a binary array with the given
    shape. Binarization is accomplished by using the given 8-bit threshold.
    """
    im = np.array(Image.open(path).convert("LA").resize(shape))[:, :, 0]
    return np.where(im < threshold, 0.0, 1.0)


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
