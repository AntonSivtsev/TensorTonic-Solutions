import pandas as pd

def reset_index_demo(data, index_col):
    """
    Returns: list [columns_before_reset, columns_after_reset]
    """
    df = pd.DataFrame(data)
    df = df.set_index(index_col)
    cbr = []
    cbr.append(df.index.name)
    for i in df.columns.tolist():
        cbr.append(i)
    df = df.reset_index(drop=True)
    car = df.columns.tolist()
    return [car, cbr]