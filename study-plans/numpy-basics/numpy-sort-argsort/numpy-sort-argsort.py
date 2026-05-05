import numpy as np

def sort_with_indices(data, axis):
    """Returns: np.ndarray of shape (2, m, n), stacked sorted values and sort indices"""
    a = np.array(data, dtype=np.float64)
    x = np.sort(a, axis=axis)
    y = np.argsort(a, axis=axis)

    return np.stack((x, y))
    