from math import comb

def binomial_distribution(n, p, threshold):
    """
    Returns: dict with 'pmf' (list), 'mean', 'variance', 'tail_prob' as floats.
    """
    pmf = []
    prob_at_least = 0
    ran = range(0, n + 1)
    for k in ran:
        x = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
        pmf.append(round(x, 4))

    mu = n * p
    si = n * p * (1 - p)
    prob_at_least = sum(pmf[threshold:])

    return {'pmf': pmf, 'mean': round(mu, 4), 'variance': round(si, 4), 'prob_at_least': round(prob_at_least, 4)}