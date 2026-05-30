import numpy as np

def standard_errors(samples):
    """
    Returns: dict with 'standard_errors' (list of floats) and 'comparison'.
    """
    se = []
    for i in samples:
        arr = np.array(i)
        n = len(i)
        s = float(np.std(arr, ddof=1))
        se.append(round(s / n ** 0.5, 4))
    a = np.array(se)
    me = round(float(np.mean(a)), 4)

    return {"standard_errors": se, "mean_se": me}