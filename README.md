# media-filesize-estimator

<div align="center">

[![Build status](https://github.com/kHarshit/media-filesize-estimator/workflows/build/badge.svg?branch=master&event=push)](https://github.com/kHarshit/media-filesize-estimator/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/media-filesize-estimator.svg)](https://pypi.org/project/media-filesize-estimator/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/kHarshit/media-filesize-estimator/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

![Coverage Report](assets/images/coverage.svg)

`media-filesize-estimator` estimates media file size in different formats w/o actually converting the file

</div>


## Installation

```bash
pip install -U media-filesize-estimator
```

or install with `Poetry`

```bash
poetry add media-filesize-estimator
```

Then you can run

```bash
media-filesize-estimator --help
```

or with `Poetry`:

```bash
poetry run media-filesize-estimator --help
```

### Makefile usage

[`Makefile`](https://github.com/kHarshit/media-filesize-estimator/blob/master/Makefile) contains a lot of functions for faster development.

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

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks coulb be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort` and `black`.

```bash
make codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `isort`, `black` and `darglint` library

Update all dev libraries to the latest version using one comand

```bash
make update-dev-deps
```

<details>
<summary>4. Code security</summary>
<p>

```bash
make check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
make check-safety
```

</p>
</details>

</p>
</details>

<details>
<summary>5. Type checks</summary>
<p>

Run `mypy` static type checker

```bash
make mypy
```

</p>
</details>

<details>
<summary>6. Tests with coverage badges</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>7. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint
```

the same as:

```bash
make test && make check-codestyle && make mypy && make check-safety
```

</p>
</details>

<details>
<summary>8. Docker</summary>
<p>

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

Remove docker image with

```bash
make docker-remove
```

More information [about docker](https://github.com/kHarshit/media-filesize-estimator/tree/master/docker).

</p>
</details>

<details>
<summary>9. Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Delete .DS_STORE files

```bash
make dsstore-remove
```

Remove .mypycache

```bash
make mypycache-remove
```

Or to remove all above run:

```bash
make cleanup
```

</p>
</details>

## Working

```
$ media-filesize-estimator --help
Usage: media-filesize-estimator [OPTIONS]
```

## Contributing

Thanks for considering contributing to this project. Please follow [Contributing guidelines](https://github.com/kHarshit/media-filesize-estimator/blob/main/CONTRIBUTING.md).

## 🛡 License

[![License](https://img.shields.io/github/license/kHarshit/media-filesize-estimator)](https://github.com/kHarshit/media-filesize-estimator/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/kHarshit/media-filesize-estimator/blob/master/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{media-filesize-estimator,
  author = {kHarshit},
  title = {`media-filesize-estimator` estimates media file size in different formats w/o actually converting the file},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/kHarshit/media-filesize-estimator}}
}
```

### Credits 

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)
