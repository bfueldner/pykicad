"""KiCAD symbol decorator.

.. py::module:: pykicadlib.symbol.decorators.switch_no
   :synopsis: KiCAD symbol decorator

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""
from pykicadlib.config import Symbol as Config
from pykicadlib.symbol.decorator import Decorator
from pykicadlib.symbol.elements import Polygon


class SwitchNo(Decorator):
    """Switch 'normaly open'.

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

        line = Polygon()
        line.thickness = Config.DECORATION_THICKNESS
        line.unit = unit
        line.add(Polygon.Point(x, y))
        x += self.sign * (Config.PIN_OFFSET + Config.PIN_GRID)
        line.add(Polygon.Point(x, y))
        self.elements.append(line)
