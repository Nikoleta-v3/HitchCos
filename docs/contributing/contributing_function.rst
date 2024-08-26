.. |uncheck| raw:: html

    <input type="checkbox">

.. _ContributingFunction:

5. Contributing a new function
-------------------------------

Navigate to the issues tab of the repository and find an issue that you would
like to work on. Some of these issues are tagged as :code:`enhancement`. The
issue will have a description of the function that needs to be implemented, and
where the function code should be included.


Install the package in development mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To contribute any source code such a test, you need to install the package in
development mode. To do this, run the following command from the root of the
project folder::

    $ pip install -e .


Implementing your function
^^^^^^^^^^^^^^^^^^^^^^^^^^^

In your function you need to remember to include a docstring that describes what
the function does. This is important for users of the software to understand how
to use the function. The docstring should be in the following format::

    def function_name(arguments):
        """
        Description of the function.

        Parameters
        ----------
        arguments : type
            Description of the argument.

        Returns
        -------
        type
            Description of the return value.
        """

        # code for the function


Documenting your function
^^^^^^^^^^^^^^^^^^^^^^^^^^

The online documentation has a section
https://hitchcos.readthedocs.io/en/latest/api.html where all the functions are
documented. This list is generated automatically. However, you can compile the
documentation locally and check that your function has appeared.

To build the documentation, the first thing you need to do is to download
`Sphinx <https://www.sphinx-doc.org/en/master/>`_. You can do this via `pip`::

    $ python -m pip install sphinx

To build the documentation navigate to the :code:`docs` directory::
    
    $ cd docs

and run the command::

    $ make html
    Running Sphinx v5.0.2
    loading pickled environment... done
    building [mo]: targets for 0 po files that are out of date
    building [html]: targets for 0 source files that are out of date
    updating environment: 0 added, 0 changed, 0 removed
    looking for now-outdated files... none found
    no targets are out of date.
    build succeeded.

    The HTML pages are in build/html.

You can open :code:`_build/html/index.html` in a browser to see the
documentation locally which should include the changes you made.




Testing your function
^^^^^^^^^^^^^^^^^^^^^

Before you commit your changes, you need to test your function. To do this, you
need to run the test suite. The test suite is in the :code:`tests` directory.
The test suite is written using `pytest <https://docs.pytest.org/en/stable/>`_.
To run the test suite, run the command from the root of the project folder::

    $ pytest tests
    ============================= test session starts ==============================
    platform linux -- Python 3.8.5, pytest-6.2.2, pluggy-0.13.1
    rootdir: /home/nikoleta/Documents/a-hitchhikers-guide-to-contributing-to-open-source
    collected 0 items

    ============================== no tests ran in 0.01s ==============================


Committing the change
^^^^^^^^^^^^^^^^^^^^^

Once you are done with your changes, you need to commit them. First, you need to
**stage** the files you have changed. To do this, run the following command::

    $ git add <name of the file tou want to commit>

Do this for all the files you have changed. Once you have staged all the files,
you can commit them::

    $ git commit

This will open a text editor where you can write your commit title and message.


Checklist
^^^^^^^^^

| |uncheck| Choose an issue labeled :code:`enhancement` from the issues section.
| |uncheck| Familiarize yourself with the structure of the source code.
| |uncheck| Install the package in development mode.
| |uncheck| Implement the new function.
| |uncheck| Include a docstring in the function.
| |uncheck| Implement a test for your new function.
| |uncheck| Test the function using the test suite.
| |uncheck| Add the changes to the staging area.
| |uncheck| Commit the changes.