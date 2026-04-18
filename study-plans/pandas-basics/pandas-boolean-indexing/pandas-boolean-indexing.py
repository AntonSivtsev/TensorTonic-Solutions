import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    df = pd.DataFrame(data)
    df = df[df[column] > threshold]
    cnt = df[column].count()

    result = {
        'filtered_data': df.to_dict(orient='list'),
        'count': cnt
    }
    return result