"""KiCAD symbol decorator.

.. py::module:: pykicadlib.symbol.decorators.switch_wiper
   :synopsis: KiCAD symbol decorator

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""
from pykicadlib.config import Symbol as Config
from pykicadlib.symbol.decorators.switch_no import SwitchNo
from pykicadlib.symbol.elements import Polygon


class SwitchWiper(SwitchNo):
    """Switch wiper.

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
        super().__init__(x, y, direction, unit)

        line = self.elements[0]
        x += self.sign * (Config.PIN_OFFSET + Config.PIN_GRID)
        x += int(self.sign * Config.PIN_GRID * 1.2)
        y += int(Config.PIN_GRID * 0.6)
        line.add(Polygon.Point(x, y))
