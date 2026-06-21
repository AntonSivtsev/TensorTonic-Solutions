import torch

def tensor_op(x, y, op):
    """
    Returns: list (result tensor converted via .tolist())
    """
    x = torch.tensor(x)
    y = torch.tensor(y)
    if op == "add":
        r = torch.add(x, y)
    elif op == "multiply":
        r = torch.multiply(x, y)
    elif op == "matmul":
        r = torch.matmul(x, y)
    elif op == "power":
        r = torch.pow(x, y)
    if op == "max":
        r = torch.max(x, y)

    return r