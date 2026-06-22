import torch

def reshape_tensor(x, op):
    """
    Returns: list
    """
    x = torch.tensor(x, dtype=torch.float64)
    if op == "flatten":
        r = x.flatten()
    if op == "squeeze":
        r = x.squeeze()
    if op == "transpose":
        r = x.permute(1, 0)

    return r.tolist()

