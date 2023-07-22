import numpy as np
import torch
import torch.nn.functional as F


def feats_sampling(
    x,
    flow,
    interpolation="bilinear",
    padding_mode="zeros",
    align_corners=True,
):
    """return warped images with flows in shape(B, C, H, W)
    Args:
        x: shape(B, C, H, W)
        flow: shape(B, H, W, 2)
    """
    if x.size()[-2:] != flow.size()[1:3]:
        raise ValueError(
            f"The spatial sizes of input ({x.size()[-2:]}) and " f"flow ({flow.size()[1:3]}) are not the same."
        )
    h, w = x.shape[-2:]

    # create mesh grid
    grid_y, grid_x = torch.meshgrid(torch.arange(0, h), torch.arange(0, w))
    grid = torch.stack((grid_x, grid_y), 2).type_as(x)  #! (h, w, 2)
    grid.requires_grad = False
    grid_flow = grid + flow

    # scale grid_flow to [-1,1]
    grid_flow_x = 2.0 * grid_flow[:, :, :, 0] / max(w - 1, 1) - 1.0
    grid_flow_y = 2.0 * grid_flow[:, :, :, 1] / max(h - 1, 1) - 1.0
    grid_flow = torch.stack((grid_flow_x, grid_flow_y), dim=3)
    output = F.grid_sample(
        x,
        grid_flow,
        mode=interpolation,
        padding_mode=padding_mode,
        align_corners=align_corners,
    )
    return output
