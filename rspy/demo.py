import argparse
from pathlib import Path

import torch
from mmflow.apis import inference_model, init_model
from mmflow.datasets import visualize_flow
from PIL import Image
from torchvision import transforms
from torchvision.utils import save_image

from rspy.solver import cubic_flow, linear_flow, quadratic_flow
from rspy.utils import feats_sampling

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str, help="input file or directory")
parser.add_argument("--output", type=str, help="output directory")
parser.add_argument("--model", type=str, default="linear", help="linear | quadratic | cubic")
parser.add_argument("--gamma", type=float, default=0.9, help="the readout reatio")
parser.add_argument("--tau", type=int, default=0, help="the timestamp warping to")
parser.add_argument("--fconfig", type=str, default="raft_8x2_100k_mixed_368x768", help="mmflow config file")
parser.add_argument("--device", type=str, default="cuda:0", help="cpu | cuda:0")
args = parser.parse_args()


def main():
    assert args.model in ["linear", "quadratic", "cubic"]
    input, output = Path(args.input), Path(args.output)
    image_paths = sorted(list(input.iterdir()))

    # init a optical-flow model
    config_file, checkpoint_file = f"{args.fconfig}.py", f"{args.fconfig}.pth"
    model = init_model(config_file, checkpoint_file, device=args.device)

    # * inference flow
    num = {"linear": 2, "quadratic": 3, "cubic": 4}[args.model]
    flows = inference_model(model, image_paths[: num - 1], image_paths[1:num])  # list of numpy.ndarray
    torch_flows = [torch.from_numpy(flow).unsqueeze(0).to(args.device) for flow in flows]  # * list (1,h,w,2)
    for i, flow in enumerate(flows):
        visualize_flow(flow, output / f"{i:04d}.png")

    # * rolling shutter correctin
    solver = eval(f"{args.model}_flow")
    F0tau = solver(*torch_flows[:num], args.gamma, args.tau)  # * (1,h,w,2)

    # * warp image
    rs_path = image_paths[num // 2]
    tsfm = transforms.Compose([transforms.ToTensor()])
    rs_image = tsfm(Image.open(rs_path).convert("RGB")).unsqueeze(0).to(args.device)  # * (1,3,h,w)
    rsc_image = feats_sampling(rs_image, -F0tau)

    # * save image
    save_image(rsc_image, output / f"rsc_{rs_path.stem}.png")
