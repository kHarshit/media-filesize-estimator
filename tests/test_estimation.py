"""Tests for Estimation class"""

import pytest

from media_filesize_estimator.mediaEstimation import Estimation


@pytest.mark.parametrize(
    ("param", "expected"),
    [
        (
            "resolution",
            {
                "1920x1080": 593.262,
                "3840x2160": 2373.047,
                "2560x1440": 1054.688,
                "1280x720": 263.672,
                "640x360": 65.918,
            },
        ),
        (
            "bit_depth",
            {
                "8 bit": 593.262,
                "10 bit": 741.577,
                "12 bit": 889.893,
                "16 bit": 1186.523,
            },
        ),
        (
            "frame_rate",
            {
                "29.97 FPS": 592.668,
                "24 FPS": 474.609,
                "30 FPS": 593.262,
                "60 FPS": 1186.523,
                "90 FPS": 1779.785,
            },
        ),
    ],
)
def test_estimation(param, expected):
    "Test estimation function"
    estimationObj = Estimation("assets/sample_video_redfort.mp4")
    assert estimationObj.estimate(param) == expected
