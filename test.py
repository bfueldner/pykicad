#!/usr/bin/env python3

import sys
import unittest

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

import test.symbols.type
import test.symbols.element
import test.symbols.from_str
import test.symbols.library

import test.footprint.helper
import test.footprint.type
import test.footprint.layer
import test.footprint.element
#import test.footprint.footprint

if __name__ == '__main__':
    test_symbols_type = unittest.TestLoader().loadTestsFromTestCase(test.symbols.type.case)
    test_symbols_element = unittest.TestLoader().loadTestsFromTestCase(test.symbols.element.case)
    test_symbols_from_str = unittest.TestLoader().loadTestsFromTestCase(test.symbols.from_str.case)
    test_symbols_library = unittest.TestLoader().loadTestsFromTestCase(test.symbols.library.case)

    test_footprint_helper = unittest.TestLoader().loadTestsFromTestCase(test.footprint.helper.case)
    test_footprint_type = unittest.TestLoader().loadTestsFromTestCase(test.footprint.type.case)
    test_footprint_layer = unittest.TestLoader().loadTestsFromTestCase(test.footprint.layer.case)
    test_footprint_element = unittest.TestLoader().loadTestsFromTestCase(test.footprint.element.case)
#    test_footprint_footprint = unittest.TestLoader().loadTestsFromTestCase(test.footprint.footprint.case)

    test_suites = [
        test_symbols_type,
        test_symbols_element,
        test_symbols_from_str,
        test_symbols_library,

        test_footprint_helper,
        test_footprint_type,
        test_footprint_layer,
        test_footprint_element,
    #    test_footprint_footprint
    ]
    suite = unittest.TestSuite(test_suites)
    unittest.TextTestRunner(verbosity = 2).run(suite)
