.. pykicadlib documentation master file, created by
   sphinx-quickstart on Wed Sep 11 23:27:48 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CANopen for Python
==================

This package provides support for interacting with a network of CANopen_ nodes.

.. note::

   Most of the documentation here is directly stolen from the
   CANopen_ Wikipedia page.

   This documentation is a work in progress.
   Feedback and revisions are most welcome!

CANopen is a communication protocol and device profile specification for
embedded systems used in automation. In terms of the OSI model, CANopen
implements the layers above and including the network layer.
The CANopen standard consists of an addressing scheme, several small
communication protocols and an application layer defined by a device profile.
The communication protocols have support for network management, device
monitoring and communication between nodes, including a simple transport layer
for message segmentation/desegmentation.

Easiest way to install is to use pip_::

   $ pip install canopen


.. toctree::
   :maxdepth: 2

   symbol/type
.. symbol/element

.. _CANopen: https://en.wikipedia.org/wiki/CANopen
.. _pip: https://pip.pypa.io/en/stable/


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
