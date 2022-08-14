# type: ignore[attr-defined]
from typing import Optional

from enum import Enum
from random import choice

import typer
from rich.console import Console

from media_filesize_estimator import version
from media_filesize_estimator.mediaEstimation import Estimation
from media_filesize_estimator.mediaExtraction import Extraction


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
    property: str = typer.Option(
        None,
        "-p",
        "--property",
        case_sensitive=False,
        help="Parameter (resolution/frame_rate/bit_depth/sampling_rate/channels) to compare",
    ),
    save_format: str = typer.Option(
        None,
        "-sf",
        "--save-format",
        case_sensitive=False,
        help="Format (json/xml/csv) to save media metadata",
    ),
    save_location: str = typer.Option(
        "./",
        "-sl",
        "--save-location",
        case_sensitive=False,
        help="Location to save media metadata and/or graph",
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

    if save_format is not None:
        extractionObj = Extraction(media)
        if save_format == "json":
            meta_file_path = extractionObj.jsonCreation(save_location)
        elif save_format == "xml":
            meta_file_path = extractionObj.XMLCreation(save_location)
        elif save_format == "csv":
            meta_file_path = extractionObj.CSVCreation(save_location)
        console.print(
            f"[bold {color}]Extracted metadata is saved at {meta_file_path}[/]"
        )

    obj = Estimation(media)
    out_graph_path = obj.plotGraph(property, save_location)
    console.print(
        f"[bold {color}]Estimated filesize graph saved at {out_graph_path}[/]"
    )


if __name__ == "__main__":
    app()
