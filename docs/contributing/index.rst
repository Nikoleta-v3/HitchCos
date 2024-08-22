Make a contribution to the documentation
============================================

In this tutorial we will learn how to make a contribution to `listwiz`.

Open source projects are typically hosted on platforms like GitHub, GitLab, or
others, with the source code managed using Git. In this tutorial, we will use
GitHub as an example. To make a contribution, you need to have a GitHub account.
You can create an account by navigating to GitHub: http://github.com. If you are
in education, you can apply for a specific education account here:
https://education.github.com.


Forking the repository
----------------------

Most projects have protected GitHub repositories, meaning you cannot make
changes directly to the source code. Instead, you need to create a copy of the
source code under your own GitHub account and then make changes to that copy.
This process is called a **fork**. To do this, navigate to the GitHub repository
of the project
(https://github.com/Nikoleta-v3/a-hitchhikers-guide-to-contributing-to-open-source)
and click the :code:`Fork` button. Then choose your GitHub account as the
**onwer** and click on :code:`Create fork`.


.. image:: /_static/forking.png

Cloning the repository
----------------------

Once we have a fork of the repository on **your** Github account, create a copy
of it to your computer. This is called cloning. Do this by clicking the
:code:`Code` button and copying the address of the repository to your clipboard:

.. image:: /_static/cloning.png

Note that we want to copy the address of the repository using the `SSH`
protocol. Now, open your command line tool and type `git clone`, then paste the
address you just copied. The command should look like the following, where
`<your-username>` is replaced with your GitHub username::


    $ git clone httpsgit@github.com:<your-username>/a-hitchhikers-guide-to-contributing-to-open-source.git

This will download the source code to your computer::

    Cloning into 'a-hitchhikers-guide-to-contributing-to-open-source'...
    remote: Enumerating objects: 117, done.
    remote: Counting objects: 100% (117/117), done.
    remote: Compressing objects: 100% (94/94), done.
    remote: Total 117 (delta 14), reused 105 (delta 9), pack-reused 0 (from 0)
    Receiving objects: 100% (117/117), 3.63 MiB | 3.43 MiB/s, done.
    Resolving deltas: 100% (14/14), done.

Creating a branch
-----------------

Before we start making changes to the source code, the first thing we will do is
create a new branch. This is because we want to keep the changes we are about to
make separate from the main source code. To do this, first change directory into
the source code::

    $ cd a-hitchhikers-guide-to-contributing-to-open-source

Now, to create a new branch, type the following::
    
        $ git branch the-name-of-the-branch

Note that the name of the branch should be descriptive of the changes you are
going to make. For example, if you are going to add a new function to the source
code, you could name the branch :code:`implementing-new-function`.

Now checkout to that branch::

    $ git checkout the-name-of-the-branch


Modifying the documentation
---------------------------

One set of changes you can make to the source code is to the documentation. The
documentation is a crucial part of any open-source project. It helps users
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


Implementing a function
------------------------

Navigate to the issues tab of the repository and find an issue that you would
like to work on. Some of these issues are tagged as :code:`enhancement`. The issue
will have a description of the function that needs to be implemented, and where
the function code should be included.

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
---------------------

Once you are done with your changes, you need to commit them. First, you need to
**stage** the files you have changed. To do this, run the following command::

    $ git add <name of the file tou want to commit>

Do this for all the files you have changed. Once you have staged all the files,
you can commit them::

    $ git commit

This will open a text editor where you can write your commit title and message.


Pushing the change to Github
----------------------------

Now that all that is done, you are going to send the changes back to your copy
of the source code on Github::

    $ git push origin the-name-of-the-branch


Opening a Pull Request
----------------------

You now have 2 copies of the modified source code of the `listwiz` project. One
locally on your computer, the other under your Github account. So first you will
push your locally modified source code to your Github account. To do this run
the command::

    $ git push origin the-name-of-the-branch

Now we want to merge the changes from your Github account to the main source
code of `listwiz`. To do this, open a Pull Request. To do this, navigate to the
repository on your Github account. You should see a :code:`Compare and Pull
Request` button:



Making further modifications
----------------------------

Once a Pull Request is opened, a number of automated checks will start. This
will check the various software tests but also build a viewable version of the
documentation.

You can click on the corresponding :code:`details` button to see any of these:



Your modification will also be reviewed:



To make any required changes, **modify the files**.

Then stage and commit the files::

    $ git add <name of the file tou want to commit>
    $ git commit

This will open a text editor where you can write your commit title and message
(similarly to before).

Once this is done, push the code to Github which will automatically update the
pull request::

    $ git push origin add-name-to-contributors-list

This final process of making further modifications might repeat itself and
eventually the Pull Request will be **merged** and your changes included in the
main version of the source code.