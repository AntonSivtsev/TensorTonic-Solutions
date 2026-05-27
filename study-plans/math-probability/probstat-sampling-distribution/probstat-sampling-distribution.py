from scipy import stats

def sampling_distribution(mu, sigma, n, threshold):
    """
    Returns: dict with 'mean', 'std_error', 'tail_probability' as floats.
    """
    std_error = round(sigma / (n ** 0.5), 4)
    prob = round(stats.norm.cdf((threshold - mu)/ (sigma / (n ** 0.5))), 4)
    return {'sampling_mean': mu, 'sampling_std': std_error, 'prob_below_threshold': prob}