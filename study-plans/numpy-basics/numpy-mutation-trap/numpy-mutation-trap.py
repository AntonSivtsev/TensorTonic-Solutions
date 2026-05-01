import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    arr = np.array(data, dtype=np.float64)
    a  = arr[row_idx]
    b = np.where(a < lo, lo, a)
    c = np.where(b > hi, hi, b)
    return np.vstack((a, c))