import pandas as pd

def create_dataframe(data):
    """
    Returns: dict with 'data', 'shape', 'columns'
    """
    result = {}
    df = pd.DataFrame(data)
    result['data'] = data
    result['shape'] = list(df.shape)
    result['columns'] = list(df.columns)
    return result


# data = {"age":[25,30],"name":["Alice","Bob"]}
# create_dataframe(data)