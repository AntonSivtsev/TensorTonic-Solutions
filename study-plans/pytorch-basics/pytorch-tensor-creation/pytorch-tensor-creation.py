import torch

def create_tensor(method, shape, value=0.0):
    """
    Returns: list
    """
    if method == 'zeros':
        t = torch.zeros((shape))
    elif method == 'ones':
        t = torch.ones((shape))
    else:
        t = value * torch.ones((shape))

    return t