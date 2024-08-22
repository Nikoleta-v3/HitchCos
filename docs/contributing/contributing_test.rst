.. |uncheck| raw:: html

    <input type="checkbox">

.. _ContributingTest:

4. Contributing a test
----------------------

Navigate to the issues tab of the repository and find an issue that you would
like to work on. Some of these issues are tagged as :code:`Tests`. The
issue will have a description of the function that needs to be implemented, and
where the function code should be included.

Install the package in development mode
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To contribute any source code such a test, you need to install the package in
development mode. To do this, run the following command from the root of the
project folder::

    $ pip install -e .


Running the test suite
^^^^^^^^^^^^^^^^^^^^^^

Once you have implemented your test you need to run the test suite to ensure
that your test is working correctly. The test suite is written using `pytest
<https://docs.pytest.org/en/stable/>`_. To run it, , run the following command
from the root of the project folder::

    $ pytest tests


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

| |uncheck| Choose an issue labeled :code:`Tests` from the issues section.
| |uncheck| Install the package in development mode.
| |uncheck| Implement the test.
| |uncheck| Run the test suite.
| |uncheck| Add the changes to the staging area.
| |uncheck| Commit the changes.