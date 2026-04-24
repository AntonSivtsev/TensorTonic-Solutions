import numpy as np

def reshape_array(data, operation):
    """
    Returns: ndarray of float64 with shape determined by the operation
    """
    a = np.array(data, dtype='float64')
    if operation =='flatten':
        return a.flatten()
    if operation == 'transpose': 
        return a.T
    if operation == 'add_batch':
        return np.expand_dims(a, axis=0)