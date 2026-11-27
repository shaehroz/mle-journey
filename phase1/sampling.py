import numpy as np
from scipy.stats import skew

rng = np.random.default_rng(0)

for n in [2, 10, 100]:
    samples = rng.exponential(scale = 2.0, size = (100000, n))
    means = samples.mean(axis = 1)

    print("n = " + str(n))
    print("SD of means: " + str(np.std(means)))
    print("Predicted:   " + str(2.0 / np.sqrt(n)))
    print("Skewness:    " + str(skew(means)))