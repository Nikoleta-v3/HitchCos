.. |uncheck| raw:: html

    <input type="checkbox">

.. _ContributingTest:

4. Contributing a test
----------------------

Navigate to the issues tab of the repository and find an issue that you would
like to work on. Some of these issues are tagged as :code:`enhancement`. The
issue will have a description of the function that needs to be implemented, and
where the function code should be included.

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
| |uncheck| Implement the new function.
| |uncheck| Include a docstring in the function.
| |uncheck| Implement a test for your new function.
| |uncheck| Test the function using the test suite.
| |uncheck| Add the changes to the staging area.
| |uncheck| Commit the changes.