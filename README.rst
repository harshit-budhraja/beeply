beeply
======

A python package that helps you produce musical notes using your
computer's characteristic beep sounds. Written in Python.

Dependencies
------------

``winsound`` python package is required. This package is present by
default, if you use python on windows.

Installation
------------

``pip install beeply``.

Usage
-----

-  Import beeply in your python code as ``from beeply import notes``.
-  Create an object of a class "beeps" as ``mybeep = notes.beeps()``.
   You can also set the default time period (in milliseconds) for which
   the note plays by passing it as an argument during object creation
   like ``mybeep = notes.beeps(400)``. If you do not specify anything,
   it takes a default value of 900ms.
-  Use this object to hear the musical notes. For example -
   ``mybeep.hear('C')``. You can also play a certain note for a time
   period other than the default period by specifying it in the
   arguments like ``mybeep.hear('C',2000)`` [Plays the C note for 2
   seconds].

You can use C, D, E... for notes in the middle scale i.e. Scale 0 while
adding a ``_`` after the note raises it to the next scale i.e. Scale 1.
For example, using ``mybeep.hear('C_')`` will produce the C note in the
Scale 1.
