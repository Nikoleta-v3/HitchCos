# A Hitchhiker's Guide to Contributing to Open Source

Open source material that will help you transition from user to contributor.
Learn to use Git, document and test code, improve documentation, and master
GitHub.

## `listwiz`

This repository contains the files necessary for a mock Python package called
`listwiz`. It is a package that allows us to handle and manipulate lists.

```python
  >>> import listwiz as lwz
  >>> unsorted_list = [2, 4, 1, 3, 5, 10, 7, 8, 9, 6]
  >>> sorted_list = lwz.sorting.merge_sort(unsorted_list)
  >>> sorted_list
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## Structure

Any Python project has its own repository and slightly different style, but many
things remain the same across projects. This project follows the recommended
structure. Below, you can see the various files and folders of the project along
with their purposes:

- `.github/workflows`: This directory contains files for running Continuous
  Integration (CI).

- `docs`: Contains all necessary files for the online documentation of the
  package. This package is built using Sphinx, and you can see the online
  documentation here:
  [https://hitchcos.readthedocs.io/en/latest/](https://hitchcos.readthedocs.io/en/latest/).

- `src`: The folder with the source code of the package. The convention is to
  name this folder `src/<name_of_package>`. In this case, it's `src/listwiz`.

- `tests`: This folder contains all the tests for the source code. We usually
  aim for each file in `src` to have an associated test file in the `tests`
  folder.

- `.gitignore`: This file lists all the files we want Git to ignore. For
  example, our Python package generates many auxiliary files, which are listed
  here because we want to ignore them and not push them to our online
  repository.

- `.readthedocs.yaml`: A file that allows us to deploy the online documentation.

- `CODE_OF_CONDUCT`: The file that outlines the expected behavior for
  contributors/attendees.

- `LICENSE`: The file that contains the license information. Licenses are not
  restrictive, even though some people seem to think so. A license lets us know
  and informs users when it's okay to use a package and who has the original
  rights.

- `pyproject.toml`: The file that is run when we install the package.

- `README.md`: The file that provides an overview of the project and
  instructions for getting started.
