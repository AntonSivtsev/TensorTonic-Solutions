import pandas as pd

def apply_transform(data, column, operation):
    """
    Returns: dict with original columns plus column_transformed
    """
    df = pd.DataFrame(data)
    if operation == 'normalize':
        df[f'{column}_transformed'] = round((df[column] - min(df[column])) /(max(df[column]) - min(df[column])), 4)
    elif operation == 'rank':
        df[f'{column}_transformed'] = df[column].rank()
    elif operation == 'cumsum':
        df[f'{column}_transformed'] = df[column].cumsum()
    elif operation == 'double':
        df[f'{column}_transformed'] = df[column]*2   
    return df.to_dict('list')