import numpy as np

def pearson_correlation(X):
    """
    Returns: ndarray, the Pearson correlation matrix.
    """
    x = np.array(X)
    cor = np.corrcoef(X, rowvar=False)

    return cor
    