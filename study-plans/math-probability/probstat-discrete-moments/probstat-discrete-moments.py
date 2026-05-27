def discrete_moments(values, probabilities):
    """
    Returns: [E_X, E_X2, variance, std_dev] as a list.
    """
    E_X = 0
    E_X2 = 0
    ran = range(0, len(values))
    for k in ran:
        s = values[k] * probabilities[k]
        q = (values[k] ** 2) * probabilities[k]
        E_X = E_X + s
        E_X2 = E_X2 + q
    
    variance = E_X2 - E_X ** 2
    std_dev = variance ** 0.5
    return [round(E_X, 4), round(E_X2, 4), round(variance, 4), round(std_dev, 4)]