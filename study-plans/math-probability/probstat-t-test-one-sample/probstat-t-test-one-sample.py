import numpy as np
from scipy import stats

def t_test_one_sample(data, mu_0, alpha):
    """
    Returns: dict with 't_stat', 'p_value', 'df' (floats), 'reject' (bool), 'ci_lower', 'ci_upper'.
    """
    a = np.array(data)
    s = np.std(a, ddof=1)
    me = np.mean(a)
    if s != 0:
        t = round((me - mu_0) / s * len(data) ** 0.5, 4)
    else:
        t = 0
    n = len(a) - 1

    p_value = round(2 * (1 - stats.t.cdf(abs(t), n)), 4)

    if p_value < alpha:
        r = True
    else:
        r = False


    return {"t_statistic": t, "degrees_of_freedom": n, "p_value": p_value, "reject_null": r}