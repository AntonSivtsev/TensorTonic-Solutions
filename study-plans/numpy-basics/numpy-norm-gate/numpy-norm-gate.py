import numpy as np

def norm_gate(X, W, threshold):
    """Returns: np.ndarray of shape (n, k), gated projection where rows below threshold are zeroed"""
    X = np.array(X) 
    W = np.array(W) 
    Z = X @ W
    norms = np.linalg.norm(Z, axis=1)
    gate = (norms >= threshold).astype(Z.dtype)


    return Z * gate[:, np.newaxis]