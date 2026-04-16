import pandas as pd

def head_tail(data, n):
    """
    Returns: dict with 'head' and 'tail' (both dicts of column -> list)
    """
    df = pd.DataFrame(data)
    df1 = df.head(n)
    df2 = df.tail(n)
    result = {
        "head": df1.to_dict('list'),
        "tail": df2.to_dict('list')
    }
    return result