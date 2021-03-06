Welcome to physics! |image0| |image1| |image2|
======================================================

**physics** is a simple **Educational library** written in `Python`_.
It could be used for your **school projects**.

Have you ever tried to define a number using errors? Calculating gravity?
Get a proportionality relation? Now, that's possible and **simple**.

Contents
========

-  `Installation`_

   -  `Installation from pypi`_ (using **pip**) - Latest stable
      version
   -  `From Github`_

      -  `Using pip`_
      -  `Downloading files`_

   -  `Documentation`_

-  `Files`_
-  `How to contribute`_

Installation
------------

From PyPi
-------------

Just use **pip**:

::

    pip install physics

Or if you want to *upgrade* the package:

::

    pip install --upgrade physics

From Github
---------------

Using Pip
~~~~~~~~~

Try using that piece of code:

::

    pip install git+https://github.com/pyTeens/physics.git

Or if you want to *upgrade* the package

::

    pip install --upgrade git+https://github.com/pyTeens/physics.git

Downloading files
~~~~~~~~~~~~~~~~~

*In primis* (from Latin, “firstable”), **clone** the repository:

::

    git clone https://github.com/pyTeens/physics.git

Then, change directory:

::

    cd physics

And finally, install the **package**:

::

    sudo python3 setup.py install

Files
-----

You’ll find lots of *not understandable* **directory** and **files**, so
here a list and definitions of them:

-  **physics** - *Main directory*

   -  **physics/__init__.pyx** - *Init file, it included all
      classes*
   -  **physics/errors.pyx** - *Errors class*
   -  **physics/gravity.pyx** - *Gravity class*
   -  **physics/numbers.pyx** - *Numbers class*
   -  **physics/proportionality.pyx** - *Proportionality class*

How to contribute
-----------------

*In primis* (“firstable”), you **must** read the `code of conducts`_ and
the `contributing document`_, then ask
`hearot`_ to enter the **organization**
(`pyTeens`_).

**Copyright** (c) 2019 `pyTeens <https://teens.python.it>`__. All rights
reserved.

.. _Python: https://python.org
.. _Installation: #installation
.. _Installation from pypi: #from-pypi
.. _From Github: #from-github
.. _Using pip: #using-pip
.. _Downloading files: #downloading-files
.. _Documentation: http://pyphysics.readthedocs.io
.. _Files: #files
.. _How to contribute: #how-to-contribute
.. _code of conducts: CODE_OF_CONDUCTS.md
.. _contributing document: CONTRIBUTING.md
.. _pyTeens: https://github.com/pyTeens
.. _hearot: https://github.com/hearot

.. |image0| image:: https://travis-ci.org/pyTeens/physics.svg?branch=master
    :target: https://travis-ci.org/pyTeens/physics
.. |image1| image:: https://img.shields.io/pypi/v/physics.svg
    :target: https://pypi.org/project/physics/
.. |image2| image:: https://img.shields.io/github/contributors/pyTeens/physics.svg
    :target: https://github.com/pyTeens/physics