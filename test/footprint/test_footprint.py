import unittest
import pykicad


class TestFootprintBase(unittest.TestCase):

    @unittest.skip("No more implemented")
    def test_base(self):
        test = pykicad.footprint.footprint.base(
            pykicad.footprint.type.technology.smd,
            'SOIC',
            'soic/soic_8_narrow',
            'SOIC Footprint',
            ['SO', 'SOIC', 'Cool'])
        print(test)
