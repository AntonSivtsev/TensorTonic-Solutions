import numpy as np
from scipy import stats

def correlation_analysis(x, y):
    """
    Returns: dict with 'r', 't_stat', 'p_value' (floats), 'reject' (bool).
    """
    x = np.array(x, dtype=np.float64)
    y = np.array(y, dtype=np.float64)
    r = round(stats.pearsonr(x, y)[0], 4)
    rs = round(r ** 2, 4)
    t = round((r * (len(x) - 2) ** 0.5) / ((1 - r ** 2) ** 0.5), 4)
    p_value = round(2 * stats.t.sf(abs(t), len(x) - 2), 4)
    if p_value < 0.05:
        sign = True
    else:
        sign = False
    return {'r': r, 'r_squared': rs, "t_stat": t, "p_value": p_value, "significant": sign}