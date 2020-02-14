"""Public interface for training and querying a Hopfield network.
"""

import os

from hopfield import main
from hopfield import utils


def load_images(images_dir, file_names, shape=(32, 32), threshold=100):
    """Return a list of binary image arrays for the given image directory and
    list of file names.
    """
    return [
        utils.load_binary_image(os.path.join(images_dir, f), shape, threshold)
        for f in file_names
    ]


def learn(images):
    """Learn the weight array for the given list of 2D binary images. All the
    input images must have the same dimensions.
    """
    return main.learn(main.images_to_patterns(images))


def recall(image, weights, shape):
    """Recall an image from the given input and learned weights. 
    """
    pattern = main.image_to_pattern(image)
    return main.pattern_to_image(main.recall(pattern, weights), shape)
