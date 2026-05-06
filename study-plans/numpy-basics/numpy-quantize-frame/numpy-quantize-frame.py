import numpy as np

def quantize_and_frame(data, decimals, pad_width):
    """Returns: np.ndarray of shape (3, m+2p, n+2p), stacked rounded, floored, ceiled with zero-padding"""
    arr = np.array(data, dtype=np.float64)
    l0 = np.round(arr, decimals)
    l0 = np.pad(l0, pad_width, mode='constant')
    l1 = np.floor(arr)
    l1 = np.pad(l1, pad_width, mode='constant')

    
    l2 = np.ceil(arr)
    l2 = np.pad(l2, pad_width, mode='constant')

    return np.stack((l0, l1, l2))
    