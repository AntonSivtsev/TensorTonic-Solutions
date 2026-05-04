import numpy as np

def scale_cols(data, weights):
    """Returns: np.ndarray of shape (m, n), each column scaled by corresponding weight"""
    a = np.array(data, dtype="float64")
    w = np.array(weights, dtype="float64")
    return a * w