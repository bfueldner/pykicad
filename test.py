import unittest

#import test.schematic
import test.type

import test.schematic.field
import test.schematic.from_string
#import test.symbol.field

if __name__ == '__main__':
#    schematic = unittest.TestLoader().loadTestsFromTestCase(test.schematic.case)
    test_type = unittest.TestLoader().loadTestsFromTestCase(test.type.case)

    test_schematic_field = unittest.TestLoader().loadTestsFromTestCase(test.schematic.field.case)
    test_schematic_from_string = unittest.TestLoader().loadTestsFromTestCase(test.schematic.from_string.case)

#    symbol_field = unittest.TestLoader().loadTestsFromTestCase(test.symbol.field.case)

    test_suites = [
        test_type,

        test_schematic_field,
        test_schematic_from_string,

    #    symbol_field,
    ]
    suite = unittest.TestSuite(test_suites)
    unittest.TextTestRunner(verbosity = 2).run(suite)
