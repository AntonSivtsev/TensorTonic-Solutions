def stratified_sample(strata_means, strata_stds, strata_sizes, total_sample):
    """
    Returns: dict with 'allocations' (list), 'stratified_mean', 'stratified_se' as floats.
    """
    a = []
    stratified_mean = 0
    se2 = 0
    for i in range(0, len(strata_means)):
        w = strata_sizes[i] / sum(strata_sizes)
        n = round(w * total_sample, 0)
        
        x = strata_means[i] * w
        y = (w ** 2) * (strata_stds[i] ** 2) / n
        
        a.append(n)
        stratified_mean = stratified_mean + x
        se2 = se2 + y
    return {'allocations': a, 'stratified_mean': round(stratified_mean, 4), 'stratified_se': round(se2 ** 0.5, 4)}