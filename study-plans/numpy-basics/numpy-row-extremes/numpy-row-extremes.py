import numpy as np

def row_extremes(data):
    """Returns: np.ndarray of shape (4, m), rows are max_val, max_col, min_val, min_col"""
    arr = np.array(data, dtype=np.float64)
    max_val = arr.max(axis=1)
    max_col = arr.argmax(axis=1)
    min_val = arr.min(axis=1)
    min_col = arr.argmin(axis=1)

    return np.stack((max_val, max_col, min_val, min_col))