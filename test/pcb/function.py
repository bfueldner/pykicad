import unittest

import kicad.pcb

class case(unittest.TestCase):

    def test_text_quote(self):
        test = kicad.pcb.quote_text('Text "with" quote')
        self.assertEqual(test, '"Text ""with"" quote"')

    def test_text_quote_raise(self):
        with self.assertRaises(ValueError):
            kicad.pcb.quote_text("\xc3")
