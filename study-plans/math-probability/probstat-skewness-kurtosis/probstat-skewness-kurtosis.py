import numpy as np

def skewness_kurtosis(data):
    """
    Returns: dict with 'skewness', 'kurtosis', and interpretation strings.
    """
    x = np.array(data)
    me = np.mean(x)
    st = np.std(x, ddof=1)
    n = len(data)
    sum1 = 0
    sum2 = 0
    if st == 0:
        g1 = np.nan
        g2 = np.nan
    else:
        for i in data:
            dif = ((i - me) / st) ** 3
            k = ((i - me) / st) ** 4
            sum1 = sum1 + dif
            sum2 = sum2 + k        
    
        g1 = n/((n-1)*(n-2))*sum1
        g2 = n * (n+1) /((n-1) * (n-2) * (n-3)) * sum2 - (3 * (n-1) **2) / ((n - 2) * (n - 3))
    if g1 > 0.5:
        g3 = "right-skewed"
    elif g1 < -0.5:
        g3 = "left-skewed"
    else:
        g3 = "approximately symmetric"
        
    if g2 > 1:
        g4 = "leptokurtic"
    elif g2 < -1:
        g4 = "platykurtic"
    else:
        g4 = "mesokurtic"
    return {"skewness": round(g1, 4), "kurtosis": round(g2, 4), "skew_interpretation": g3, "kurtosis_interpretation": g4}