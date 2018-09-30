import unittest

import test.symbol.field

if __name__ == '__main__':
    symbol_field = unittest.TestLoader().loadTestsFromTestCase(test.symbol.field.case)

    test_suites = [
        symbol_field,
    ]
    suite = unittest.TestSuite(test_suites)
    unittest.TextTestRunner(verbosity = 2).run(suite)
