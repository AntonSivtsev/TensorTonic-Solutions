from scipy import stats

def p_value_analysis(test_stat, dist_type, df, tail):
    """
    Returns: dict with 'p_value' (float) and significance level classifications.
    """
    if tail == 'two':
        if dist_type == 'z':
            p_value = round(2 * stats.norm.cdf(-abs(test_stat)), 4)
        elif dist_type == 't':
            p_value = round(2 * stats.t.cdf(-abs(test_stat), df), 4)
    elif tail == 'left':
        if dist_type == 'z':
            p_value = round( stats.norm.cdf(test_stat), 4)
        elif dist_type == 't':
            p_value = round(stats.t.cdf((test_stat), df), 4)
    elif tail == 'right':
        if dist_type == 'z':
            p_value = round(1 - stats.norm.cdf(abs(test_stat)), 4)
        elif dist_type == 't':
            p_value = round(1 - stats.t.cdf(abs(test_stat), df), 4)

    if p_value >= 0.01:
        s1 = False
    else:
        s1 = True
    if p_value >= 0.05:
        s5 = False
    else:
        s5 = True
    if p_value >= 0.1:
        s10 = False
    else:
        s10 = True
    

    return { "p_value": p_value, "significant_at_01": s1, "significant_at_05": s5, "significant_at_10": s10 }