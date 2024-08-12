Make a contribution to the documentation
==================================================

In this tutorial we will make a contribution to `lsitwiz`.

Forking the repository
----------------------

Navigate to http://github.com and create an account. If you are in education you
can apply for a specific education account here: https://education.github.com.

Navigate to the Github repository:
https://github.com/Nikoleta-v3/a-hitchhikers-guide-to-contributing-to-open-source.
This is the hub for development of the source code. You cannot make modification
to this copy of the source code so you need to create your own copy under your
Github account. You do this by creating a **fork**. Do this by clicking the
:code:`Fork` button and following the instructions:

.. image:: /_static/forking.png

Cloning the repository
----------------------

Once we have a fork of the repository on **your** Github account, create a copy
of it to your computer. This is called cloning. Do this by clicking the `Code`
button and copying the address of the repository to your clipboard:

.. image:: /_static/cloning.png

Now to create a clone of the source code open your command line tool and type
the following (**replace** :code:`<your username>` with your Github username):

    $ git clone https://github.com/<your username>/a-hitchhikers-guide-to-contributing-to-open-source.git

This will download the source code to your computer::

    $ git clone https://github.com/<your username>/a-hitchhikers-guide-to-contributing-to-open-source.git
    Cloning into 'a-hitchhikers-guide-to-contributing-to-open-source.git'...
    remote: Enumerating objects: 1813, done.
    remote: Counting objects: 100% (362/362), done.
    remote: Compressing objects: 100% (225/225), done.
    remote: Total 1813 (delta 160), reused 233 (delta 79), pack-reused 1451
    Receiving objects: 100% (1813/1813), 439.94 KiB | 2.67 MiB/s, done.
    Resolving deltas: 100% (905/905), done.

Creating a branch
-----------------

In order to modify the source code you must create a new branch. After cloning,
first change directory in to the Nashpy source code::

    $ cd a-hitchhikers-guide-to-contributing-to-open-source

Now, to keep the changes you are about to make separate from the :code:`main`
source code, create a **branch**::

    $ git branch implementing-task-a

Now checkout to that branch::

    $ git checkout implementing-task-a

Modifying the documentation
---------------------------


Checking the modification
-------------------------


Implementing a function
----------------------

Navigate to the issues.


Running the test suite
----------------------

You can run the entire test suite which will check that this modification has
not caused any problems::

    $ python -m pip install tox
    $ python -m tox

Committing the change
---------------------

Now you need to **stage** this file::

    $ git add docs/contributing/reference/contributors/index.rst

Now commit this file::

    $ git commit

This will open a text editor where you can write your commit title and message::

    Add <your username> to list of contributors

    I am doing the contribution tutorial.

Closing the editor will commit the changes you made.

Pushing the change to Github
----------------------------

Now that all that is done, you are going to send the changes back to your copy
of the source code on Github::

    $ git push origin add-name-to-contributors-list

Opening a Pull Request
----------------------

You now have 2 copies of the modified source code of Nashpy. One locally on your
computer, the other under your Github account. In order to include those changes
in to the main source code of Nashpy you will open a Pull request.

To do this, go to your fork of the Nashpy repository:
:code:`https://github.com/<your username>/Nashpy`. You should see a
:code:`Compare and Pull Request` button:

.. image:: /_static/contributing/tutorial/before_pr/main.png

Once you have clicked on that, you can review your changes and then eventually
click on :code:`Create pull request` to create the Pull Request.

Making further modifications
----------------------------

Once a Pull Request is opened, a number of automated checks will start. This
will check the various software tests but also build a viewable version of the
documentation.

You can click on the corresponding :code:`details` button to see any of these:

.. image:: /_static/contributing/tutorial/ci/main.png

Your modification will also be reviewed:

.. image:: /_static/contributing/tutorial/review/main.png

To make any required changes, **modify the files**.

Then stage and commit the files::

    $ git add docs/contributing/reference/contributors/index.rst
    $ git commit

This will open a text editor where you can write your commit title and message
(similarly to before).

Once this is done, push the code to Github which will automatically update the
pull request::

    $ git push origin add-name-to-contributors-list

This final process of making further modifications might repeat itself and
eventually the Pull Request will be **merged** and your changes included in the
main version of the Nashpy source code.