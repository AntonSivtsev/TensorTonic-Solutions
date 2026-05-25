from math import factorial, perm, comb

def perms_and_combs(n, r):
    """
    Returns: [permutations, combinations, factorial] as a list.
    """
    P = perm(n, r)
    C = comb(n, r)
    n = factorial(n)
    return [P, C, n]