import numpy as np

def angle_features(angles):
    """Returns: np.ndarray of shape (3, n), rows are sin, cos, tan"""
    arr = np.array(angles, dtype=np.float64)
    sin = np.sin(arr)
    cos = np.cos(arr)
    tan = np.tan(arr)
    a = np.vstack((sin, cos, tan))

    return a