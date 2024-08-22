Installation Guide
==================

To install the package, you first need to obtain a copy of the project's
repository on your computer. This is done by cloning the repository.

We recommend that you first create a fork of the repository (refer to
:ref:`Forking` for more details).

After forking the repository, clone your fork to your computer by running the
following command in your terminal after navigating to the directory where you
want to place the project::


    $ git clone https://github.com/<your-github-username>/a-hitchhikers-guide-to-contributing-to-open-source.git


Replace `<your-github-username>` with your actual GitHub username. Next,
navigate to the project directory::


    $ cd a-hitchhikers-guide-to-contributing-to-open-source


Then, install the package by running the following command::

    $ pip install .


If you want to install the package in development mode, use the following
command instead::


    $ pip install -e .


*Why install in development mode?* Development mode is useful if you plan to
modify the code. In this mode, any changes you make to the source files are
immediately reflected in the installed package, without needing to reinstall it.