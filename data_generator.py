import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.decomposition import PCA


class DataGenerator(object):

    def __init__(self):
        pass

    # generate random TSP instance
    def gen_instance(self, max_length, dimension, seed=0):
        if seed != 0:
            np.random.seed(seed)
        sequence = np.random.rand(max_length, dimension)  # (max_length) cities with (dimension) coordinates in [0,1]
        pca = PCA(n_components=dimension)  # center & rotate coordinates
        sequence = pca.fit_transform(sequence)