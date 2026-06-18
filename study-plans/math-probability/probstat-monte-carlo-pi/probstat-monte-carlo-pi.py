import numpy as np

def monte_carlo_pi(n_points, seed):
    """
    Returns: dict with 'pi_estimate' (float), 'points_inside' (int), 'total_points' (int).
    """
    r = np.random.default_rng(seed)
    x = r.uniform(0, 1, n_points)
    y = r.uniform(0, 1, n_points)
    arr = np.stack([x, y], axis=1)
    mask = arr[:,0] ** 2 + arr[:,1] ** 2 <= 1
    inside = len(arr[mask])
    e = round(4 * inside / n_points, 4)
    mae = round(abs(e - np.pi), 4)
    return {"estimate": e, "error": mae}