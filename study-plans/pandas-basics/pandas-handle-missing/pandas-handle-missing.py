import pandas as pd

def handle_missing(data, fill_value):
    """
    Returns: dict with 'null_counts' (dict) and 'cleaned_data' (dict)
    """
    df = pd.DataFrame(data)
    nc = df.isna().sum()
    df = df.fillna(fill_value)
    res = {
        'null_counts': nc.to_dict(),
        'cleaned_data': df.to_dict('list')
    }
    return res