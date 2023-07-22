import torch
from einops import rearrange


def linear_flow(F0n1: torch.Tensor, gamma: float, tau: float) -> torch.Tensor:
    """solve the linear motion matrix and predict the correction feild.
    Args:
        F01: torch.Tensor (b,h,w,2), flow 0 -> -1
        gamma: float, the readout reatio
        tau: float, the timestamp warping to
    Returns:
        torch.Tensor: the correction feild to tau.
    """
    h, w = F0n1.shape[1:3]
    t0n1 = -1 + gamma / h * F0n1[:, :, :, 1]  # * (b, h, w)

    # solve the linear motion matrix
    M = F0n1 / rearrange(t0n1, "b h w -> b h w 1")  # * (b, h, w, 2)

    # predict the correction feild
    grid_y, _ = torch.meshgrid(
        torch.arange(0, h, device=F0n1.device, requires_grad=False),
        torch.arange(0, w, device=F0n1.device, requires_grad=False),
    )  # * (h, w)

    t0tau = tau - gamma / h * grid_y  # * (h, w)
    F0tau = rearrange(t0tau, "h w -> h w 1") * M  # * (b, h, w, 2)

    return F0tau


def quadratic_flow(F0n1: torch.Tensor, F01: torch.Tensor, gamma: float, tau: float) -> torch.Tensor:
    """solve the quadratic motion matrix and predict the correction feild.
    Args:
        F0n1: torch.Tensor (b,h,w,2), flow 0 -> -1
        F01: torch.Tensor (b,h,w,2), flow 0 -> 1
        gamma (float): the readout reatio
        tau (float): the timestamp warping to
    Returns:
        torch.Tensor: the correction feild to tau.
    """
    h, w = F0n1.shape[1:3]
    t0n1 = -1 + gamma / h * F0n1[:, :, :, 1]  # * (b, h, w)
    t01 = 1 + gamma / h * F01[:, :, :, 1]  # * (b, h, w)

    # solve the quadratic motion matrix
    A = rearrange(
        torch.stack([t0n1, 0.5 * t0n1**2, t01, 0.5 * t01**2], dim=-1),
        "b h w (m n) -> b h w m n",
        m=2,
        n=2,
    )  # * (b, h, w, 2, 2)

    B = torch.stack([F0n1, F01], dim=-2)  # * (b, h, w, 2, 2)
    M = torch.linalg.solve(A, B)  # * (b, h, w, 2, 2)

    # predict the correction feild
    grid_y, _ = torch.meshgrid(
        torch.arange(0, h, device=F0n1.device, requires_grad=False),
        torch.arange(0, w, device=F0n1.device, requires_grad=False),
    )
    t0tau = tau - gamma / h * grid_y  # * (h, w)

    Atau = rearrange(torch.stack([t0tau, 0.5 * t0tau**2], dim=-1), "h w m -> h w 1 m")  # * (h, w, 1, 2)
    F0tau = rearrange(Atau @ M, "b h w 1 n -> b h w n")  # * (b, h, w, 2)

    return F0tau


def cubic_flow(F0n2: torch.Tensor, F0n1: torch.Tensor, F01: torch.Tensor, gamma: float, tau: float) -> torch.Tensor:
    """solve the cubic motion matrix and predict the correction feild.
    Args:
        F0n1: torch.Tensor (b,h,w,2): flow 0 -> -1
        F01: torch.Tensor (b,h,w,2): flow 0 -> 1
        F02: torch.Tensor (b,h,w,2): flow 0 -> 2
        gamma: (float): the readout reatio
        tau: (float): the timestamp warping to
    Returns:
        torch.Tensor: the correction feild to tau.
    """
    h, w = F0n1.shape[1:3]
    t0n2 = -2 + gamma / h * F0n2[:, :, :, 1]
    t0n1 = -1 + gamma / h * F0n1[:, :, :, 1]
    t01 = 1 + gamma / h * F01[:, :, :, 1]

    # solve the cubic motion matrix
    A = rearrange(
        torch.stack(
            [
                t0n2,
                0.5 * t0n2**2,
                1 / 6 * t0n2**3,
                t0n1,
                0.5 * t0n1**2,
                1 / 6 * t0n1**3,
                t01,
                0.5 * t01**2,
                1 / 6 * t01**3,
            ],
            dim=-1,
        ),
        "b h w (m n) -> b h w m n",
        m=3,
        n=3,
    )  # * (b, h, w, 3, 3)
    B = torch.stack([F0n2, F0n1, F01], dim=-2)  # * (b, h, w, 3, 2)
    M = torch.linalg.solve(A, B)  # * (b, h, w, 3, 2)

    # predict the correction feild
    grid_y, _ = torch.meshgrid(
        torch.arange(0, h, device=F0n1.device, requires_grad=False),
        torch.arange(0, w, device=F0n1.device, requires_grad=False),
    )
    t0tau = tau - gamma / h * grid_y  # * (h, w)

    Atau = rearrange(torch.stack([t0tau, 0.5 * t0tau**2, 1 / 6 * t0tau**3], dim=-1), "h w m -> h w 1 m")
    F0tau = rearrange(Atau @ M, "b h w 1 n -> b h w n")  # * (b, h, w, 2)

    return F0tau
