# type: ignore[attr-defined]
"""`media-filesize-estimator` estimates media file size in different formats w/o actually converting the file"""

import sys
from importlib import metadata as importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()
