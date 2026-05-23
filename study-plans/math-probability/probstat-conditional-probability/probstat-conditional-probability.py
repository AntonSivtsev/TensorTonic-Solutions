def conditional_probability(p_a, p_b, p_a_and_b):
    """
    Returns: [p_a_given_b, p_b_given_a] as a list.
    """
    p_a_given_b = p_a_and_b / p_b
    p_b_given_a = p_a_and_b / p_a
    return [round(p_a_given_b, 4), round(p_b_given_a, 4)]
    