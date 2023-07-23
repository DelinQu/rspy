# rspy (under construction)

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.8-blue
)](https://img.shields.io/badge/python-3.9-pink) [![Python Version](https://img.shields.io/badge/python-3.9-pink
)](https://img.shields.io/badge/python-3.8-blue) [![Python Version](https://img.shields.io/badge/python-3.10-green
)](https://img.shields.io/badge/python-3.10-green)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/rspy/rspy/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/rspy/rspy/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/rspy/rspy/releases)
[![License](https://img.shields.io/badge/GNU%20GPL%20v3.0-3.9-orange)](https://img.shields.io/badge/GNU%20GPL%20v3.0-3.9-orange)
![Coverage Report](assets/images/coverage.svg)

The `core` implementation of [Fast Rolling Shutter Correction in the Wild, TPAMI 2023](https://ieeexplore.ieee.org/document/10148802) and [Towards Nonlinear-Motion-Aware and Occlusion-Robust Rolling Shutter Correction, ICCV 2023](https://arxiv.org/abs/2303.18125).
</div>

|            **3GS**            |             **Gpark**             |
| :---------------------------: | :-------------------------------: |
| ![3gs](assets/images/3gs.gif) | ![gpark](assets/images/gpark.gif) |

## 🚀 Features
- A light weight library for rolling shutter correction which is easy to use.
- Support linear, qudratic and cubic motion models.
- Support sparse features correction and can be pluged into 3D vision algorithm pipeline, such as SfM, SLAM, etc.

## Installation

```bash
pip install git@github.com:DelinQu/rspy.git
# pip install rspy is unavailable now
```
It's recommended to clone the code and run the demo files in the `rspy` folder. In our implementation, we use [open-mmlab/mmflow](https://github.com/open-mmlab/mmflow) to caculate the optical flow, and please refer to the [installation](https://github.com/open-mmlab/mmflow/blob/master/docs/en/install.md) for optical flow support.

### Usage

[`rspy`](https://github.com/rspy/rspy/blob/master/rspy) contains `linear`, `quadratic` and `cubic` models for faster rolling shutetr correction. The `solver` is the core of the rspy, which receives the optical flow fields and return the correction field. The `feats_sampling` function warps the RS image back to GS one.

<details>
<summary>0. Hyparameters </summary>

- `gamma`: the ratio of the exposure time to the frame interval.
- `tau`: the normalized timestamp warping to.

</details>


<details>
<summary>1. Linear rolling shutter correction</summary>
<p>

`linear_flow` receives a optical flow field from $I_{0} \to I_{-1}$ and return correction field $u_{0 \to \tau}$.
```python
F0tau = solver(F0n1, gamma, tau)  # * (1,h,w,2)
rsc_image = feats_sampling(rs_image, -F0tau)
```
</p>
</details>

<details>
<summary>2. Quadratic rolling shutter correction</summary>
<p>

`quadratic_flow` receives two optical flow fields from $I_{0} \to I_{-1}$ and $I_{0} \to I_{1}$, and return correction field $u_{0 \to \tau}$.
```python
F0tau = solver(F0n1, F01, gamma, tau)  # * (1,h,w,2)
rsc_image = feats_sampling(rs_image, -F0tau)
```
</p>
</details>

<details>
<summary>3. Cubic rolling shutter correction</summary>
<p>

`cubic_flow` receives three optical flow fields from $I_{0} \to I_{-2}$, $I_{0} \to I_{-1}$ and $I_{0} \to I_{1}$, and return correction field $u_{0 \to \tau}$.

```python
F0tau = solver(F0n2, F0n1, F01, gamma, tau)  # * (1,h,w,2)
rsc_image = feats_sampling(rs_image, -F0tau)
```
</p>
</details>

## 🍀 Demo
We provided a demo for rolling shutter correction in `rspy`， which read the images from the `demo` folder and save the results in the `out` folder. The demo can be run by the following command:
```bash
python rspy/demo.py --model=linear

python rspy/demo.py --model=qudratic

python rspy/demo.py --model=cubic
```
You can also use your own images with a sutable `gamma` and `tau` to get a satisfactory result.

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/rspy/rspy/releases) page.
|         **Label**         | **Title in Releases** |
| :-----------------------: | :-------------------: |
| `the foundation of rspy`  |      🐣 Features       |
| `relase the pypi package` |       🚀 Release       |
|    `To be continue :)`    |          ⇨ ▶️          |



## 🛡 License

[![License](https://img.shields.io/github/license/rspy/rspy)](https://github.com/rspy/rspy/blob/master/LICENSE)

This project is licensed under the terms of the `GNU GPL v3.0` license. See [LICENSE](https://github.com/rspy/rspy/blob/master/LICENSE) for more details.

## 📃 Citation
If you find this project useful for your research, please use the following BibTeX entry:
```bibtex
@ARTICLE{qu2023fast,
  author={Qu, Delin and Liao, Bangyan and Zhang, Huiqing and Ait-Aider, Omar and Lao, Yizhen},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence}, 
  title={Fast Rolling Shutter Correction in the Wild}, 
  year={2023},
  volume={},
  number={},
  pages={1-18},
  doi={10.1109/TPAMI.2023.3284847}
}

@article{qu2023towards,
  title   = {Towards Nonlinear-Motion-Aware and Occlusion-Robust Rolling Shutter Correction},
  author  = {Delin Qu and Yizhen Lao and Zhigang Wang and Dong Wang and Bin Zhao and Xuelong Li},
  year    = {2023},
  journal = {arXiv preprint arXiv: 2303.18125}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)
