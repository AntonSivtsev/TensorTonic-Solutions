import numpy as np

def compare_correlations(a, b):
    """Returns: np.ndarray of shape (3, n, n), stacked correlation matrices"""
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    combined = np.concatenate([a, b], axis=0)
    c1 = np.corrcoef(a.T)
    c2 = np.corrcoef(b.T)
    c3 = np.corrcoef(combined.T)

    return np.stack((c1, c2, c3))