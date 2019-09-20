# pragma pylint: disable=too-few-public-methods, pointless-string-statement
"""
.. module:: pykicad.config
   :synopsis: pykicadlib configuration

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""


class Symbol():
    '''Symbol configuration'''

    ROOT = '${KICAD_SYMBOL_DIR}'

    LIBRARY_START = 'EESchema-LIBRARY Version 2.4\n# encoding utf-8\n'
    LIBRARY_END = '#\n# End Library\n'
    LIBRARY_EXTENSION = '.lib'

    DESCRIPTION_START = 'EESchema-DOCLIB  Version 2.0\n'
    DESCRIPTION_END = '#\n# End Doc Library\n'
    DESCRIPTION_EXTENSION = '.dcm'

    TABLE_EXTENSION = '.csv'

    ELEMENT_THICKNESS = 20
    DECORATION_THICKNESS = 10
    FIELD_TEXT_SIZE = 60
    PIN_LENGTH = 100
    PIN_GRID = 100
    PIN_OFFSET = 50    # Pin name offset
    PIN_NAME_SIZE = 40
    PIN_NUMBER_SIZE = 40

    POWER_SYMBOL_REFERENCE = ['#PWR']


class Documents():
    '''Documents configuration'''

    ROOT = '${KICAD_DOCUMENT_DIR}'


class Packages3d():
    '''3D packages configuration'''

    ROOT = '${KISYS3DMOD}'
    FOLDER_EXTENSION = '.3dshapes'
    FILE_EXTENSION = ['stp', 'wrl']


class Footprint():
    '''Footprint configuration'''

    # Footprint
    ROOT = '${KISYSMOD}'
    FOLDER_EXTENSION = '.pretty'
    FILE_EXTENSION = '.kicad_mod'

    # FOOTPRINT_PRECISION = 3

    # REFERENCE_LAYER = 'F.SilkS'
    REFERENCE_FONT_SIZE = 1.0
    REFERENCE_FONT_THICKNESS = 0.15

    # VALUE_LAYER = 'F.Fab'
    VALUE_FONT_SIZE = 1.0
    VALUE_FONT_THICKNESS = 0.15

    # PACKAGE_LAYER = 'F.SilkS'
    # PACKAGE_LINE_WIDTH = 0.15
    PACKAGE_LINE_WIDTH = 0.3

    # Scale line with and font size depending on device area
    SMALL_DEVICE = 5.0
    MEDIUM_DEVICE = 20.0
    BIG_DEVICE = 100.0

    SMD_LAYERS = 'F.Cu F.Paste F.Mask'
    THD_LAYERS = '*.Cu *.Mask F.SilkS'

    # http://www.leiton.de/technologie-starre-leiterplatten.html
    # http://www.multi-circuit-boards.eu/leiterplatten-design-hilfe/design-parameter/restring.html
    DRILL = [
        0.2,
        0.25,
        0.3,
        0.35,
        0.4,
        0.45,
        0.5,
        0.55,
        0.6,
        0.65,
        0.7,
        0.75,
        0.8,
        0.85,
        0.9,
        0.95,
        1.0
    ]
    ANNULAR_RING = 0.15


"""Configuration parsing module, which generate a python namespace"""
'''
__all__ = ("Config")

from collections import Mapping, Sequence

class Config(object):
    """A dict subclass that exposes its items as attributes.

    Warning: Namespace instances do not have direct access to the
    dict methods.

    """

    def __init__(self, configFile):
        for line in open(configFile,"r"):
            parts = line.rstrip().split("=",1)
            if len(parts) > 1:
                # Strip enclosing double quotes
                if parts[1].startswith('"') and parts[1].endswith('"'):
                    parts[1] = parts[1][1:-1]

                try:
                    numVal = float(parts[1])
                    setattr(self,parts[0],numVal)
                except:
                    setattr(self,parts[0],parts[1])

    __hash__ = None

    def __eq__(self, other):
        return vars(self) == vars(other)

    def __ne__(self, other):
        return not (self == other)

    def __contains__(self, key):
        return key in self.__dict__

    def dict(self):
        return self.__dict__
'''
