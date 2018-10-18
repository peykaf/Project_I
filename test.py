import numpy as np
from sklearn.decomposition import PCA

max_length = 10
dimension = 2
seed = 2
# np.random.seed(seed)
sequence = np.random.rand(max_length, dimension)

print(sequence)

pca = PCA(n_components=dimension)
sequence = pca.fit_transform(sequence)

print(sequence)
