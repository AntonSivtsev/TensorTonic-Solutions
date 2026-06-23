import torch

def compute_gradient(values):
    """
    Returns: list of float gradient values dy/dx
    """
    x = torch.tensor(values, requires_grad=True, dtype=torch.float64)
    y = x ** 3 + 2 * x
    y = y.sum()
    y.backward()
    result = x.grad.tolist()
    return result