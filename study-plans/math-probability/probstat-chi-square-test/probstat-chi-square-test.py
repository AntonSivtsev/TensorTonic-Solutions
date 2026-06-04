import numpy as np
from scipy import stats

def chi_square_test(observed, expected):
    """
    Returns: [chi2_stat, df, p_value, reject] as a list.
    """
    chi2_stat = 0
    for i in range(0, len(observed)):
        chi2 = (observed[i] - expected[i]) ** 2 / expected[i]
        chi2_stat = chi2_stat + chi2
    df = len(observed) - 1
    p_value = round(stats.chi2.sf(chi2_stat, df), 4)
    if p_value >= 0.05:
        reject = False
    else:
        reject = True

    return [round(chi2_stat, 4), df, p_value, reject]
    