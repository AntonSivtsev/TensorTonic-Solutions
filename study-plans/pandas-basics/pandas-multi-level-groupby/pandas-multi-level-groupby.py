import pandas as pd

def multi_groupby(data, group_cols, value_col, aggfunc):
    """
    Returns: dict of lists (flat table with group columns + value column)
    """
    m = value_col
    df = pd.DataFrame(data)
    gr = df.groupby(group_cols).agg({value_col : aggfunc}).reset_index()

    return gr.to_dict('list')