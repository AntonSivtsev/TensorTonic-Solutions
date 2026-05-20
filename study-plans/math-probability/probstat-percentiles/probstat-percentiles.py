import numpy as np

def percentiles(x, q):
    """
    Returns: numpy array of percentile values.
    """
    x = np.array(x)
    list = []
    for i in q:
        per = np.percentile(x, i)
        list.append(per)
    return np.array(list)
        
