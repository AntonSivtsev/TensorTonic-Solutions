import pandas as pd

def concat_dataframes(dfs):
    """
    Returns: list [shape, data] where shape is [rows, cols]
    """
    s = [pd.DataFrame(file) for file in dfs]
    df = pd.concat(s)
    return [df.shape, df.to_dict("list")]