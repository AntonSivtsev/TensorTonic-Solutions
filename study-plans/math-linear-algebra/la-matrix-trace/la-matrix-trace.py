import numpy as np

def matrix_trace(A):
    """
    Returns: float, the trace (sum of diagonal elements) of A.
    """
    a = np.array(A)
    d = np.diag(a)
    return sum(d)