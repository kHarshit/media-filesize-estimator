# type: ignore[attr-defined]
from typing import Optional

from enum import Enum
from random import choice

import typer
from rich.console import Console

from media_filesize_estimator import mediaEstimation, version
from media_filesize_estimator.example import hello


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
    mediaConfig: str = typer.Option(
        None,
        "-media",
        "--mediaConfig",
        "--mediaConfiguration",
        case_sensitive=False,
        help="Media File Configuration\n filename(required) - Specify the file name \n Params: resolution, bitrate, framerate(optional) \n Save format(optional) - Specify XML or JSON \n Save location(optional) - Specify the save location",
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
    """Print a greeting with a giving name."""
    # if color is None:
    color = choice(list(Color))
    if mediaConfig is None:
        mediaConfig = choice(list(mediaEstimation))

    greeting: str = hello(name)
    console.print(f"[bold {color}]{greeting}[/]")


if __name__ == "__main__":
    app()
