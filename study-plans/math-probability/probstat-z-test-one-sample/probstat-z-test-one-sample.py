from scipy import stats

def z_test_one_sample(x_bar, mu_0, sigma, n, alpha):
    """
    Returns: [z_stat, p_value, reject] as a list.
    """
    z_stat = round((x_bar - mu_0) * n ** 0.5 / sigma, 4)
    cdf = stats.norm.cdf(-abs(z_stat))
    p_value = round(2 * cdf, 4)
    if p_value < alpha:
        reject = True
    else:
        reject = False
    return [z_stat, p_value, reject]