Think Python 3
==============

Examples from the book "Think Python - How to Think Like a Computer Scientist",
by Allen Downey, Jeff Elkner, and Chris Meyers.

    <http://www.greenteapress.com/thinkpython/thinkCSpy/html/index.html>

As far as I can tell, there are four versions of this book online.

Python 2:

1.  The aforementioned - Version 1, I believe
2.  http://www.greenteapress.com/thinkpython/html/index.html - Version 2.0.16

Python 3:

3.  http://openbookproject.net/thinkcs/python/english3e/
4.  http://faculty.stedwards.edu/mikek/python/thinkpython.pdf

These examples pull from 1 mostly, some from 2.

- - -

Modified and rewritten for Python 3 by Andrew Antle 2015.

    <http://ndndndnd.org>


Run Tests
---------

To run the tests:

1.  Setup a virtual environment

        $ cd thinkpython3/
        $ ls
        bin/ docs/ requirements.txt setup.py tests/ thinkpython3/
        $ pyvenv env
        $ ./env/bin/pip install -r requirements.txt
        $ ./env/bin/nosetests

    and watch the tests pass!
