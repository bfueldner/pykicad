import unittest
import pykicadlib.footprint


class TestFootprintBase(unittest.TestCase):

    @unittest.skip("No more implemented")
    def test_base(self):
        test = pykicadlib.footprint.footprint.base(
            pykicadlib.footprint.type.technology.smd,
            'SOIC',
            'soic/soic_8_narrow',
            'SOIC Footprint',
            ['SO', 'SOIC', 'Cool'])
        print(test)
