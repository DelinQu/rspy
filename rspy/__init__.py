# type: ignore[attr-defined]
"""The core implementation of Fast Rolling Shutter Correction in the Wild, TPAMI 2023 and Towards Nonlinear-Motion-Aware and Occlusion-Robust Rolling Shutter Correction, ICCV 2023."""

import sys
from importlib import metadata as importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()
