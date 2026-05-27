from math import exp

def exponential_distribution(lam, t):
    """
    Returns: dict with 'pdf', 'cdf', 'survival', 'mean', 'variance' as floats.
    """
    pdf = round(lam * exp(-lam * t), 4)
    cdf = round(1 - exp(-lam * t), 4)
    survival = round(exp(-lam * t), 4)
    mu = round((1 / lam), 4)
    si = round((1 / lam ** 2), 4)
    return {'pdf': pdf, 'cdf': cdf, 'survival': survival, 'mean': mu, 'variance': si}