# A Hitchhiker's Guide to Contributing to Open Source

Open source material that will help you transition from user to contributor.
Learn to use Git, document and test code, improve documentation, and master
GitHub.

This repository contains the files necessary for a mock Python package called
`listwiz`. It is a package that allows us to handle and manipulate lists.

Any Python project has its own repository and slightly different style, but many
things remain the same across projects. This project follows the recommended
structure. Below, you can see several files and folders along with their
purposes:

- `.github/workflows`: This directory contains files for running Continuous
  Integration (CI).
- `docs`: Contains all necessary files for the online documentation of the
  package. This package is built using Sphinx, and you can see the online
  documentation here:
- `src`: The folder with the source code of the package. Note that the
  convention is to name this folder `src/<name_of_package>`. In this case, it's
  `src/listwiz`. Inside, you will find several Python files and an `__init__.py`
  file at the root.
- `tests`: This folder contains all the tests for the source code. We usually
  aim for each file in `src` to have an associated test file in the `tests`
  folder.
- `.gitignore`: This file lists all the files we want Git to ignore. Our Python
  package generates a lot of auxiliary files, and examples of these are listed
  here.
- `README.md`: A file that allows us to deploy the online documentation.
- `setup.py`: The file that is run when we install the package.
- `LICENSE`: The file that contains the license information.
- `CONTRIBUTING.rst`: The file with the contributing guidelines.

Installation notes.