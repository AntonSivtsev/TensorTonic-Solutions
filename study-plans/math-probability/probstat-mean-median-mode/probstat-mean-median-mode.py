import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    y = np.array(x, dtype=np.float64)
    mean = np.mean(y)
    median = np.median(y)
    mo = Counter(y).most_common(1)[0][0]
    return {"mean": mean, "median": median, "mode": mo}