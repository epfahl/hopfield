"""Public interface for training and querying a Hopfield network.
"""

from hopfield import core as c


def learn(images):
    """Learn the weight array for the given list of 2D binary images. All the
    input images must have the same dimensions.
    """
    return c.learn(c.images_to_patterns(images))


def recall(image, weights, shape):
    """Recall an image from the given input and learned weights. 
    """
    pattern = c.image_to_pattern(image)
    return c.pattern_to_image(c.recall(pattern, weights), shape)
