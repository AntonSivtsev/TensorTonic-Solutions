import numpy as np

def bootstrap_ci(data, n_bootstraps, confidence, seed):
    """
    Returns: [mean, ci_lower, ci_upper] as a list.
    """
    rd = np.random.RandomState(seed)
    ran = range(0, n_bootstraps, 1)
    new_list = []
    for i in ran:
        random_numbers = rd.choice(data, len(data), replace=True)
        me = float(np.mean(random_numbers))
        new_list.append(me)
    new_list = sorted(new_list)
    a = np.array(new_list)
    me = round(float(np.mean(a)), 4)
    low_idx = int(np.floor((1 - confidence) / 2 * len(new_list)))
    up_idx = int(((1 - confidence) / 2 + confidence) * len(new_list)) - 1
    ci_lower = round(new_list[low_idx], 4)
    ci_upper = round(new_list[up_idx], 4)

    return [me, ci_lower, ci_upper]
    