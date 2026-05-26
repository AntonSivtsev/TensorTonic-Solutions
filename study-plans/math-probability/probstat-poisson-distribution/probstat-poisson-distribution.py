from math import factorial, exp

def poisson_distribution(lam, max_k):
    """
    Returns: [pmf_list, cdf_at_max_k, p_zero] as a list.
    """
    pmf_list = []
    ran = range(0, max_k + 1)
    for k in ran:
        p = (lam ** k) * exp(-lam) / factorial(k)
        pmf_list.append(round(p, 4))
        cdf_at_max_k = round(sum(pmf_list[:max_k + 1]), 4)
        p_zero = round(exp(-lam), 4)
    return [pmf_list, cdf_at_max_k, p_zero]
    