.. _Branching:

2. Creating a branch
---------------------

Before we start making changes to the source code, the first thing we will do is
create a new branch. This is because we want to keep the changes we are about to
make separate from the main source code. To do this, first change directory into
the source code::

    $ cd HitchCos

Now, to create a new branch, type the following::

        $ git branch the-name-of-the-branch

Note that the name of the branch should be descriptive of the changes you are
going to make. For example, if you are going to add a new function to the source
code, you could name the branch :code:`implementing-new-function`.

Now checkout to that branch::

    $ git checkout the-name-of-the-branch