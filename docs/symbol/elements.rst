Symbol elements
***************

Symbols consist of multiple elements. These are well known elements like lines,
circles and arcs. Additionally elements are added, the help construct symbols
out of element primitives.

Examples
========

Here is a simple example::

    >>> element = pykicadlib.symbol.elements.Rectangle(10, 10, 20, 20, 5, pykicadlib.symbol.types.Fill.none)
    >>> print(element)
    S 10 10 20 20 0 1 5 N

API
===

Alias
-----

.. autoclass:: pykicadlib.symbol.elements.Alias

Field
-----

.. autoclass:: pykicadlib.symbol.elements.Field
    :members:
    :member-order: bysource
    :inherited-members:

Graphics
--------

.. autoclass:: pykicadlib.symbol.elements.Arc
    :members:
    :member-order: bysource
    :inherited-members:

.. autoclass:: pykicadlib.symbol.elements.Circle
    :members:
    :member-order: bysource
    :inherited-members:

.. autoclass:: pykicadlib.symbol.elements.Pin
    :members:
    :member-order: bysource
    :inherited-members:

.. autoclass:: pykicadlib.symbol.elements.Polygon
    :members:
    :member-order: bysource
    :inherited-members:

.. autoclass:: pykicadlib.symbol.elements.Rectangle
    :members:
    :member-order: bysource
    :inherited-members:

.. autoclass:: pykicadlib.symbol.elements.Text
    :members:
    :member-order: bysource
    :inherited-members:

Helper
------

.. autofunction:: pykicadlib.symbol.elements.from_str

.. autoclass:: pykicadlib.symbol.elements.Boundary
    :members:
    :member-order: bysource
    :inherited-members:

.. autoclass:: pykicadlib.symbol.elements.Point
    :members:
    :member-order: bysource
    :inherited-members:
