import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    arr = np.array(data, dtype=np.float64)
    a1 = np.where(arr > threshold, 1, 0)
    a2 = np.where(np.any(arr > threshold, axis=1)[:, None], arr, 0)
    a3 = np.where(np.all(arr > threshold, axis=1)[:, None], arr, 0)

    return [a1, a2, a3]