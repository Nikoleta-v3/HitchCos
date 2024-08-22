.. |uncheck| raw:: html

    <input type="checkbox">

.. _ContributingDocs:

3. Contributing to the documentation
-------------------------------------

In the issues section of the project, you can find issues that are labeled
:code:`documentation`. These are issues that are related to the documentation of
the project. You can choose one of these issues to work on.

The documentation is a crucial part of any open-source project. It helps users
understand how to use the software and how to contribute to it.

All the files for the documentation are in the :code:`docs` directory. The
documentation is written in `reStructuredText
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_. The
documentation is built using `Sphinx <https://www.sphinx-doc.org/en/master/>`_.

In order to modify the documentation, you need to change the files in the
:code:`docs` directory. Open the project in your preferred editor. If you do not
have a preferred editor `Visual Studio Code <https://code.visualstudio.com>`_ is
recommended.

Take a few minutes to familiarize yourself with the structure of the
documentation. The main file for the documentation is :code:`index.rst` which is
in the :code:`docs` directory. This file includes all the other files in the
documentation. The documentation is split into different sections, each of which
is in a separate folder in the :code:`docs` directory.


Checking the modification
^^^^^^^^^^^^^^^^^^^^^^^^^^

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

| |uncheck| Choose an issue labeled :code:`documentation` from the issues section.
| |uncheck| Familiarize yourself with the structure of the documentation.
| |uncheck| Make the necessary changes to the documentation.
| |uncheck| Build the documentation using `Sphinx <https://www.sphinx-doc.org/en/master/>`_.
| |uncheck| Check the changes you made by opening :code:`_build/html/index.html` in a browser.
| |uncheck| Add the changes to the staging area.
| |uncheck| Commit the changes.