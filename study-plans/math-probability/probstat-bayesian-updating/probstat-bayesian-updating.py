def bayesian_update(prior_alpha, prior_beta, successes, failures):
    """
    Returns: dict with 'posterior_alpha', 'posterior_beta', 'prior_mean', 'posterior_mean' as floats.
    """
    pa = prior_alpha + successes
    pb = prior_beta + failures
    prior_mean = round(prior_alpha / (prior_alpha + prior_beta), 4)
    post_mean = round(pa / (pa + pb),4)

    return {'posterior_alpha': pa, 'posterior_beta': pb, 'prior_mean': prior_mean, 'posterior_mean': post_mean}