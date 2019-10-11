"""KiCAD symbol decorator.

.. py::module:: pykicadlib.symbol.decorators.connector_male
   :synopsis: KiCAD symbol decorator

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""
from pykicadlib.config import Symbol as Config
from pykicadlib.symbol.decorator import Decorator
from pykicadlib.symbol.elements import Polygon, Rectangle


class ConnectorMale(Decorator):
    """Male connector symbol.

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
        line.unit = unit
        line.add(Polygon.Point(x, y))
        x += self.sign * Config.PIN_OFFSET
        line.add(Polygon.Point(x, y))
        self.elements.append(line)

        rectangle = Rectangle(
            x,
            y - int(Config.PIN_GRID * 0.2),
            x + int(self.sign * Config.PIN_GRID),
            y + int(Config.PIN_GRID * 0.2)
        )
        rectangle.thickness = Config.DECORATION_THICKNESS
        rectangle.fill = Rectangle.Fill.foreground
        rectangle.unit = unit
        self.elements.append(rectangle)
