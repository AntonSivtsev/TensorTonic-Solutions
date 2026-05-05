import numpy as np

def summarize(data, axis):
    """Returns: np.ndarray of shape (4, k), rows are mean, std, min, max"""    
    arr = np.array(data, dtype=np.float64)
    me = np.mean(arr, axis=axis)
    st = np.std(arr, axis=axis)
    mi= np.min(arr, axis=axis)
    ma = np.max(arr, axis=axis)

    return np.stack((me, st, mi, ma))