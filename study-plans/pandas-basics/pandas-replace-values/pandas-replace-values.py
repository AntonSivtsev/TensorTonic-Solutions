import pandas as pd

def replace_values(data, column, old_val, new_val):
    """
    Returns: dict with 'data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)
    cnt = df[df[column] == old_val][column].count()
    df[column] = df[column].replace(old_val, new_val)

    res = {
        'data': df.to_dict('list'),
        'count': cnt
    }
    return res