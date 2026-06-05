import numpy as np

def mle_normal(data):
    """
    Returns: dict with 'mu_hat' and 'sigma_hat' as floats (MLE estimates).
    """
    a = np.array(data)
    mu = round(np.sum(data) / len(a), 4)
    su = 0
    for i in range(len(data)):
        x = (data[i] - mu) ** 2
        su = su + x
    sigma = round((su / len(a)) ** 0.5, 4)

    return {"mu_mle": mu, "sigma_mle": sigma}