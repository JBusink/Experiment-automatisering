import numpy as np
def stdev_of_mean(values):
# Calculate the standard deviation of the mean
    return np.std(values) / np.sqrt(len(values))