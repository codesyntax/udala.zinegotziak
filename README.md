<div align="center">
    <h1 align="center">udala.zinegotziak</h1>
</div>
<div align="center">
[![PyPI](https://img.shields.io/pypi/v/udala.zinegotziak)](https://pypi.org/project/udala.zinegotziak/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/udala.zinegotziak)](https://pypi.org/project/udala.zinegotziak/)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/udala.zinegotziak)](https://pypi.org/project/udala.zinegotziak/)
[![PyPI - License](https://img.shields.io/pypi/l/udala.zinegotziak)](https://pypi.org/project/udala.zinegotziak/)
[![PyPI - Status](https://img.shields.io/pypi/status/udala.zinegotziak)](https://pypi.org/project/udala.zinegotziak/)

[![PyPI - Plone Versions](https://img.shields.io/pypi/frameworkversions/plone/udala.zinegotziak)](https://pypi.org/project/udala.zinegotziak/)

[![CI](https://github.com/codesyntax/udala.zinegotziak/actions/workflows/ci.yml/badge.svg)](https://github.com/codesyntax/udala.zinegotziak/actions/workflows/ci.yml)
![Code Style](https://img.shields.io/badge/Code%20Style-Black-000000)

[![GitHub contributors](https://img.shields.io/github/contributors/codesyntax/udala.zinegotziak)](https://github.com/codesyntax/udala.zinegotziak)
[![GitHub Repo stars](https://img.shields.io/github/stars/codesyntax/udala.zinegotziak?style=social)](https://github.com/codesyntax/udala.zinegotziak)

</div>

A Plone addon providing specific functionality for UdalPlone projects.

## Features

- Provides the `Councillor`, `Party`, and `Commission` content types for government representation
- RestAPI endpoints
- Volto-ready backend setup

## Installation

Install udala.zinegotziak with `pip`:

```shell
pip install udala.zinegotziak
```

And to create the Plone site:

```shell
make create-site
```

## Contribute

- [Issue tracker](https://github.com/codesyntax/udala.zinegotziak/issues)
- [Source code](https://github.com/codesyntax/udala.zinegotziak/)

### Prerequisites ✅

-   An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
-   [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
-   [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
-   [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)

### Installation 🔧

1.  Clone this repository, then change your working directory.

    ```shell
    git clone git@github.com:codesyntax/udala.zinegotziak.git
    cd udala.zinegotziak
    ```

2.  Install this code base.

    ```shell
    make install
    ```

### Add features using `plonecli`

This package provides markers as strings (`<!-- extra stuff goes here -->`) that are compatible with [`plonecli`](https://github.com/plone/plonecli) and [`bobtemplates.plone`](https://github.com/plone/bobtemplates.plone).
These markers act as hooks to add all kinds of subtemplates, including behaviors, control panels, upgrade steps, or other subtemplates from `plonecli`.

To run `plonecli` with configuration to target this package, run the following command.

```shell
make add <template_name>
```

For example, you can add a content type to your package with the following command.

```shell
make add content_type
```

## License

The project is licensed under GPLv2.
