# type: ignore[attr-defined]
from typing import Optional

from enum import Enum
from random import choice

import typer
from rich.console import Console

from media_filesize_estimator import mediaEstimation, version


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="media-filesize-estimator",
    help="`media-filesize-estimator` estimates media file size in different formats w/o actually converting the file",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(
            f"[yellow]media-filesize-estimator[/] version: [bold blue]{version}[/]"
        )
        raise typer.Exit()


@app.command(name="")
def main(
    media: str = typer.Option(
        ...,
        "-m",
        "--media",
        case_sensitive=False,
        help="Media file path",
    ),
    param: str = typer.Option(
        None,
        "-p",
        "--param",
        case_sensitive=False,
        help="Parameter (resolution/bitrate/framerate) to compare",
    ),
    save_format: str = typer.Option(
        None,
        "-sf",
        "--save_format",
        case_sensitive=False,
        help="Format (json/xml/csv) to save media metadata",
    ),
    save_location: str = typer.Option(
        None,
        "-sl",
        "--save_location",
        case_sensitive=False,
        help="Location to save media metadata",
    ),
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the media-filesize-estimator package.",
    ),
) -> None:
    """Estimates media file size in different formats w/o actually converting the file"""
    # if color is None:
    color = choice(list(Color))

    dummy_msg = "Package in development!"
    console.print(f"[bold {color}]{dummy_msg}[/]")


if __name__ == "__main__":
    app()
