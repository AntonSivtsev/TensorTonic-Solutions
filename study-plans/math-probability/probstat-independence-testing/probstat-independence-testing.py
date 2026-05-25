def independence_test(p_a, p_b, p_a_and_b):
    """
    Returns: dict with 'p_a_times_p_b' (float) and 'is_independent' (bool).
    """
    p_a_b = round(p_a * p_b, 4)
    if p_a_b == p_a_and_b:
        ind = True
    else:
        ind = False
    return {"p_a_times_p_b": p_a_b, "is_independent": ind}
