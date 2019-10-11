"""KiCAD symbol decorator.

.. py::module:: pykicadlib.symbol.decorators.connector_female
   :synopsis: KiCAD symbol decorator

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""
from pykicadlib.config import Symbol as Config
from pykicadlib.symbol.decorator import Decorator
from pykicadlib.symbol.elements import Arc, Polygon


class ConnectorFemale(Decorator):
    """Female connector symbol.

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
        line.thickness = 0
        line.unit = unit
        line.add(Polygon.Point(x, y))
        x += self.sign * (Config.PIN_OFFSET + int(Config.PIN_GRID * 0.6))
        line.add(Polygon.Point(x, y))
        self.elements.append(line)

        x += self.sign * int(Config.PIN_GRID * 0.4)
        arc = Arc(
            x,
            y,
            int(Config.PIN_GRID * 0.4),
            x,
            y - int(Config.PIN_GRID * 0.4),
            x,
            y + int(Config.PIN_GRID * 0.4),
            -90 - self.sign / 10,
            90 + self.sign / 10
        )
        arc.thickness = Config.DECORATION_THICKNESS
        arc.unit = unit
        self.elements.append(arc)
