"""Utility functions for dealing with source files, 2D binary arrays, and 1D
bipolar patterns.
"""

import numpy as np
from PIL import Image


def sign(a):
    """Appy the bipolar step function to the given array.
    """
    return np.where(a >= 0.0, 1.0, -1.0)


def binary_to_bipolar(a):
    """Return the bipolar array corresponding to the given binary array.
    """
    return np.where(a == 0, -1, 1)


def bipolar_to_binary(a):
    """Return the binary array corresponding to the given bipolar array.
    """
    return np.where(a == -1, 0, 1)


def image_to_pattern(image):
    """Given a single binary image array, return a flat bipolar array.
    """
    return np.ravel(binary_to_bipolar(image))


def images_to_patterns(images):
    """Given a list of M NXN binary image arrays, return a MxN^2 array of
    bipolar patterns.
    """
    return np.array([image_to_pattern(im) for im in images])


def pattern_to_image(pattern, shape):
    """Convert a 1D bipolar pattern to a 2D binary image with the given shape.
    """
    return bipolar_to_binary(pattern).reshape(shape)


def load_binary_image(path, shape, threshold):
    """Load an image file with the given path as a binary array with the given
    shape. Binarization is accomplished by using the given 8-bit threshold.
    """
    im = np.array(Image.open(path).convert("LA").resize(shape))[:, :, 0]
    return np.where(im < threshold, 0.0, 1.0)
