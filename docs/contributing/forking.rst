.. _Forking:

1. Forking and Cloning the repository
-------------------------------------

Forking the repository
^^^^^^^^^^^^^^^^^^^^^^

Most projects have protected GitHub repositories, meaning you cannot make
changes directly to the source code. Instead, you need to create a copy of the
source code under your own GitHub account and then make changes to that copy.
This process is called a **fork**. To do this, navigate to the GitHub repository
of the project
(https://github.com/Nikoleta-v3/HitchCos)
and click the :code:`Fork` button. Then choose your GitHub account as the
**onwer** and click on :code:`Create fork`.


.. image:: /_static/forking.png


Cloning the repository
^^^^^^^^^^^^^^^^^^^^^^

Once we have a fork of the repository on **your** Github account, create a copy
of it to your computer. This is called cloning. Do this by clicking the
:code:`Code` button and copying the address of the repository to your clipboard:

.. image:: /_static/cloning.png

Note that we want to copy the address of the repository using the `SSH`
protocol. Now, open your command line tool and type `git clone`, then paste the
address you just copied. The command should look like the following, where
`<your-username>` is replaced with your GitHub username::


    $ git clone git@github.com:Nikoleta-v3/HitchCos.git

This will download the source code to your computer::

    Cloning into 'HitchCos'...
    remote: Enumerating objects: 117, done.
    remote: Counting objects: 100% (117/117), done.
    remote: Compressing objects: 100% (94/94), done.
    remote: Total 117 (delta 14), reused 105 (delta 9), pack-reused 0 (from 0)
    Receiving objects: 100% (117/117), 3.63 MiB | 3.43 MiB/s, done.
    Resolving deltas: 100% (14/14), done.