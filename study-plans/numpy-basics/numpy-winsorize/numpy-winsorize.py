import numpy as np

def winsorize(data, lo_q, hi_q):
    """Returns: np.ndarray of shape (3, m, n), stacked clipped values, lo_mask, hi_mask"""
    arr = np.array(data, dtype=np.float64)
    lo_q = np.percentile(arr, lo_q, axis=0)
    hi_q = np.percentile(arr, hi_q, axis=0)
    x = np.clip(arr, lo_q, hi_q)
    y = np.where(arr < lo_q, 1, 0)
    z = np.where(arr > hi_q, 1, 0)

    return np.stack((x,y,z))