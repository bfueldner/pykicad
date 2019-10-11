"""KiCAD symbol decorator.

.. py::module:: pykicadlib.symbol.decorator
   :synopsis: KiCAD symbol decorator

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""
from pykicadlib.config import Symbol as Config
from pykicadlib.symbol.elements import Pin


class Registry(type):
    """Metaclass to register decorators.

    :param str name:
        Class name
    :param list bases:
        List of bases
    :param str namespace:
        Namespace
    """

    decorator = {}  #: Decorator registry

    def __init__(cls, name, bases, namespace):
        """Constructor."""
        super().__init__(name, bases, namespace)

        if name != 'Decorator':
            Registry.decorator[name] = cls


class Decorator(metaclass=Registry):
    """Base class for decorators.

    :param Direction direction:
        Direction of decorator
    """

    def __init__(self, direction):
        """Constructor."""
        if direction in (Pin.Direction.up, Pin.Direction.down):
            raise ValueError('Only pins with left or right direction can be decorated')

        self.sign = 1 if direction == Pin.Direction.left else -1
        self.elements = []

    @property
    def height(self):
        """Height.

        :type:
            int
        """
        return Config.PIN_GRID

    @property
    def width(self):
        """Width.

        :type:
            int
        """
        return Config.PIN_OFFSET + Config.PIN_GRID * 1.5
