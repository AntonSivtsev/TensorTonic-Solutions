import numpy as np

def sample_var_std(x):
    """
    Returns: dict with 'variance' and 'std_dev' as floats.
    """
    x = np.array(x, dtype=float)
    return {'variance': np.var(x, ddof=1), 'std_dev': np.std(x, ddof=1)}