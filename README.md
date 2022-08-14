# media-filesize-estimator

<div align="center">

[![Build status](https://github.com/kHarshit/media-filesize-estimator/workflows/build/badge.svg?branch=master&event=push)](https://github.com/kHarshit/media-filesize-estimator/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/media-filesize-estimator.svg)](https://pypi.org/project/media-filesize-estimator/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/kHarshit/media-filesize-estimator/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)
![Coverage Report](assets/images/coverage.svg)

Estimates media file size in different formats w/o actually converting the file

</div>


## Installation

The package works with python 3.8+.

```bash
pip install -U media-filesize-estimator

# or install with `Poetry`
poetry add media-filesize-estimator
```

Then you can run

```bash
media-filesize-estimator --help

# or with `Poetry`:
poetry run media-filesize-estimator --help
```

## Working

```
$ media-filesize-estimator --help
Usage: media-filesize-estimator [OPTIONS]

  Estimates media file size in different formats w/o actually converting the
  file

Options:
  -m, --media TEXT           Media file path  [required]
  -p, --param TEXT           Parameter (resolution/bitrate/framerate) to
                             compare
  -sf, --save_format TEXT    Format (json/xml/csv) to save media metadata
  -sl, --save_location TEXT  Location to save media metadata
  -v, --version              Prints the version of the media-filesize-
                             estimator package.
  --help                     Show this message and exit.
```

## Contributing

Thanks for considering contributing to this project. Please follow [Contributing guidelines](https://github.com/kHarshit/media-filesize-estimator/blob/main/CONTRIBUTING.md).

## 🛡 License

[![License](https://img.shields.io/github/license/kHarshit/media-filesize-estimator)](https://github.com/kHarshit/media-filesize-estimator/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/kHarshit/media-filesize-estimator/blob/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{media-filesize-estimator,
  author = {kHarshit, Pappuru-Dinesh, TejodhayBonam, AbdulBasitA},
  title = {Estimates media file size in different formats w/o actually converting the file},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/kHarshit/media-filesize-estimator}}
}
```

### Credits 

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)
