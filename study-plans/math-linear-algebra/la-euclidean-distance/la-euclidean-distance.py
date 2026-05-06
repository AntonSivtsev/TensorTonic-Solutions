import numpy as np

def euclidean_distance(x, y):
    """
    Returns: float, the Euclidean distance between x and y.
    """
    x = np.array(x, dtype=np.float64)
    y = np.array(y, dtype=np.float64)
    z = x - y
    z = z ** 2
    z = sum(z)
    return z ** (0.5)
    
    

    