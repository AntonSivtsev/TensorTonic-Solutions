import pandas as pd

def groupby_basics(data, group_col, value_col):
    """
    Returns: dict with 'sum', 'mean', 'count' (each a dict)
    """
    df = pd.DataFrame(data)

    gr = df.groupby(group_col)[value_col].agg(['sum', 'mean', 'count'])

    return gr.to_dict()