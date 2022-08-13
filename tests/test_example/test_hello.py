"""Tests for hello function."""
from media_filesize_estimator import mediaExtraction
import pytest

from media_filesize_estimator.example import hello
from media_filesize_estimator.mediaEstimation import Estimation
from media_filesize_estimator.mediaExtraction import Extraction


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("Jeanette", "Hello Jeanette!"),
        ("Raven", "Hello Raven!"),
        ("Maxine", "Hello Maxine!"),
        ("Matteo", "Hello Matteo!"),
        ("Destinee", "Hello Destinee!"),
        ("Alden", "Hello Alden!"),
        ("Mariah", "Hello Mariah!"),
        ("Anika", "Hello Anika!"),
        ("Isabella", "Hello Isabella!"),
    ],
)
def test_hello(name, expected):
    """Example test with parametrization."""
    assert hello(name) == expected

# TODO
def test_config(file, expected):
    pass

