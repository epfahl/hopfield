"""Learning and recall functions for 1D bipolar patterns.
"""

import numpy as np

from hopfield import utils


def learn(patterns):
    """Compute the weight array for the given array of bipolar input patterns.
    """
    m, n = patterns.shape
    return np.dot(patterns.T, patterns) / m - np.diag(np.ones(n))


def recall(pattern, weights):
    """Using the synchronous recall algorithm, recall the bipolar pattern for
    the given input pattern and weights.
    """
    return utils.sign(np.dot(weights, pattern))
