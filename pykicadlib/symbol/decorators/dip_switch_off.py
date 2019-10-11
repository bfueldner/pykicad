"""KiCAD symbol decorator.

.. py::module:: pykicadlib.symbol.decorators.connector_male
   :synopsis: KiCAD symbol decorator

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""
from pykicadlib.config import Symbol as Config
from pykicadlib.symbol.decorator import Decorator
from pykicadlib.symbol.elements import Rectangle


class DipSwitchOff(Decorator):
    """DIP switch pictogram without wiper.

    :param int x:
        X coordinate
    :param int y:
        Y coordinate
    :param Direction direction:
        Connector direction
    :param int unit:
        Unit
    """

    def __init__(self, x, y, direction, unit=0):
        """Constructor."""
        super().__init__(direction)

        x += self.sign * (Config.PIN_OFFSET + int(Config.PIN_GRID * 0.5))
        rectangle = Rectangle(
            x,
            y - int(Config.PIN_GRID * 0.4),
            x + self.sign * Config.PIN_GRID * 2,
            y + int(Config.PIN_GRID * 0.4)
        )
        rectangle.thickness = Config.DECORATION_THICKNESS
        rectangle.unit = unit
        self.elements.append(rectangle)
