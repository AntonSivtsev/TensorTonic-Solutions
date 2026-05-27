from scipy import stats

def normal_distribution(mu, sigma, x):
    """
    Returns: dict with 'z_score', 'cdf', 'pdf', 'prob_within_1std' as floats.
    """
    z_score = (x - mu) / sigma
    cdf = stats.norm.cdf(x, loc=mu, scale=sigma)
    pdf = stats.norm.pdf(x, loc=mu, scale=sigma)
    prob_within_1_std = stats.norm.cdf(mu+sigma, loc=mu, scale=sigma) - stats.norm.cdf(mu-sigma, loc=mu, scale=sigma)
    return {"z_score": round(z_score, 4), "cdf": round(cdf, 4), "pdf": round(pdf, 4), "prob_within_1_std": round(prob_within_1_std, 4)}