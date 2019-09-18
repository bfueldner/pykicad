Symbol elements
===============

Symbols consist of multiple elements. These are well known elements like lines,
circles and arcs. Additionally elements are added, the help construct symbols
out of element primitives.

Examples
--------

Here is a simple example::

    >>> element = pykicadlib.symbol.elements.Rectangle(10, 10, 20, 20, 5, pykicadlib.symbol.types.Fill.none)
    >>> print(element)
    S 10 10 20 20 0 1 5 N

API
---

.. automodule:: pykicadlib.symbol.elements
    :members:
