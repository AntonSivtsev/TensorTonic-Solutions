import pandas as pd

def set_index_column(data, index_col):
    """
    Returns: dict with 'index_values', 'columns', 'data'
    """
    df = pd.DataFrame(data)
    df = df.set_index(index_col)
    result = {
        'index_values': df.index,
        'columns': df.columns,
        'data': df.to_dict('list')   
    }
    return result