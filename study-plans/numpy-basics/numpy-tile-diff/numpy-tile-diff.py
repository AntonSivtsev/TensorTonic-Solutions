import numpy as np

def tile_diff(data, reps):
    """Returns: np.ndarray of shape (2, m*reps, n), stacked tiled array and padded differences"""
    arr = np.array(data, dtype=np.float64)
    m = np.shape(arr)[0]
    n = np.shape(arr)[1]
    x = np.tile(arr, (reps, 1))
    y = np.diff(x, axis=0)
    y = np.pad(y, ((0, 1), (0, 0)), mode='constant', constant_values=0)

    return np.stack((x,y))