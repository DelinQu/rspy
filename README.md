# rspy

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
[![License](https://img.shields.io/github/license/rspy/rspy)](https://github.com/rspy/rspy/blob/master/LICENSE)
![Coverage Report](assets/images/coverage.svg)

The `core` implementation of Fast Rolling Shutter Correction in the Wild, TPAMI 2023 and Towards Nonlinear-Motion-Aware and Occlusion-Robust Rolling Shutter Correction, ICCV 2023.
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
pip install -U rspy
```
It's recommended to clone the code and run the demo files in the `rspy` folder. In our implementation, we use [open-mmlab/mmflow](https://github.com/open-mmlab/mmflow) to caculate the optical flow, and please refer to the [installation](https://github.com/open-mmlab/mmflow/blob/master/docs/en/install.md) for optical flow support.

### Usage

[`Makefile`](https://github.com/rspy/rspy/blob/master/Makefile) contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry run:

```bash
make poetry-download
```

To uninstall

```bash
make poetry-remove
```

</p>
</details>


## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/rspy/rspy/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               | **Title in Releases**  |
| :-----------------------------------: | :--------------------: |
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`](https://github.com/rspy/rspy/blob/master/.github/release-drafter.yml).

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

## 🛡 License

[![License](https://img.shields.io/github/license/rspy/rspy)](https://github.com/rspy/rspy/blob/master/LICENSE)

This project is licensed under the terms of the `GNU GPL v3.0` license. See [LICENSE](https://github.com/rspy/rspy/blob/master/LICENSE) for more details.

## 📃 Citation

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
