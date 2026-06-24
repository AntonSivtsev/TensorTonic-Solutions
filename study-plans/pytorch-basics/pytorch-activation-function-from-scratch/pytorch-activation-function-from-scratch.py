import torch

def activate(x, method="relu"):
    """
    Returns: list (activated tensor converted via .tolist())
    """
    x = torch.tensor(x, dtype=torch.float64)
    if method =="relu":
        result = torch.where(x > 0, x, 0)
    elif method =="sigmoid":
        result = 1 / (1 + torch.exp(-x))
    elif method =="tanh":
        result = (torch.exp(x) - torch.exp(-x)) / (torch.exp(x) + torch.exp(-x))
    elif method == "leaky_relu":
        result = torch.where(x > 0, x, 0.01 * x)

    return result