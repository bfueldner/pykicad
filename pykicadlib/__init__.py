"""
.. module:: pykicad.__init__
   :synopsis: pykicadlib entry point

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import pykicadlib.config
import pykicadlib.symbol.types      # noqa: F401
import pykicadlib.symbol.elements   # noqa: F401
from .version import __version__    # noqa: F401

# import pykicadlib.footprint.helper
# import pykicadlib.footprint.layer
# import pykicadlib.footprint.layers
# import pykicadlib.footprint.type
# import pykicadlib.footprint.element
# import pykicadlib.footprint.footprint

# import pykicadlib.symbol.element
# import pykicadlib.symbol.decorator
# import pykicadlib.symbol.library
