"""Test KiCAD symbol library.

.. module:: test.symbol.library
   :synopsis: Symbol library tests

.. moduleauthor:: Benjamin Füldner <benjamin@fueldner.net>
"""

import unittest
from pykicadlib.symbol.library import Symbol, Description


class TestSymbolLibrarySymbol(unittest.TestCase):
    """Test class pykicadlib.symbol.library.Symbol."""

    def test_symbol(self):
        """String output."""
        text1 = '''EESchema-LIBRARY Version 2.3
#encoding utf-8
#
# name
#
DEF name ref 0 0 Y Y 6 L N
F0 "ref" 50 150 60 H V L CNN
F1 "name" 50 -150 60 H V L CNN
F2 "footprint" 50 -250 60 H I L CNN
F3 "document" 50 -350 60 H I L CNN
DRAW
P 4 0 1 20  -150 150  150 0  -150 -150  -150 150 f
X A $A -250 0 100 R 40 40 1 1 I
X VCC $VCC 0 200 125 D 40 40 1 1 W
X GND $GND 0 -200 125 U 40 40 1 1 W
X Y $Y 250 0 100 L 40 40 1 1 O
ENDDRAW
ENDDEF
#
#End Library
'''
        text2 = '''EESchema-LIBRARY Version 2.3
#encoding utf-8
#
# name
#
DEF name ref 0 0 Y Y 6 L N
F0 "ref" 50 150 60 H V L CNN
F1 "name" 50 -150 60 H V L CNN
F2 "footprint" 50 -250 60 H I L CNN
F3 "document" 50 -350 60 H I L CNN
DRAW
P 4 0 1 20  -150 150  150 0  -150 -150  -150 150 f
X A $A -250 0 100 R 40 40 1 1 I
X Y $Y 250 0 100 L 40 40 1 1 O
ENDDRAW
ENDDEF
#
#End Library
'''

        mapping = {
            'a': '1',
            'y': '3',
            'vcc': '2',
            'gnd': '4',
            'color': 'red',
        }

        test = Symbol('TEST', 'IC', 'SOIC:soic_8', '')
        test.from_str(text1, mapping, 1)
        # self.assertEqual(len(test.fields), 4)
        self.assertEqual(len(test.elements), 5)

        test.from_str(text2, mapping, 2)
        # self.assertEqual(len(test.fields), 4)
        self.assertEqual(len(test.elements), 8)

        test.from_str(text2, mapping, 3)
        # self.assertEqual(len(test.fields), 4)
        self.assertEqual(len(test.elements), 11)

        test.optimize()
        # self.assertEqual(len(test.fields), 4)
        self.assertEqual(len(test.elements), 9)

        test.sort()
        print(test)


class TestSymbolLibraryDescription(unittest.TestCase):
    """Test class pykicadlib.symbol.library.Description."""

    description = """#
$CMP TEST
D IC
K SOIC:soic_8
$ENDCMP
"""

    def test_description(self):
        """String output."""
        test = Description('TEST', 'IC', 'SOIC:soic_8', '')
        self.assertEqual(
            str(test),
            TestSymbolLibraryDescription.description)
