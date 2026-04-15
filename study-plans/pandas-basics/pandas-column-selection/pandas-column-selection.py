import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    df = pd.DataFrame(data)
    result = {
        'values': df[column].to_list(),
        'length': df[column].value_counts().sum()
    }
    return result