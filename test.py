import unittest

#import test.schematic
import test.type

import test.schematic.field
import test.schematic.rectangle
import test.schematic.from_string

import test.pcb.helper
import test.pcb.layer
#import test.symbol.field

if __name__ == '__main__':
#    schematic = unittest.TestLoader().loadTestsFromTestCase(test.schematic.case)
    test_type = unittest.TestLoader().loadTestsFromTestCase(test.type.case)

    test_schematic_field = unittest.TestLoader().loadTestsFromTestCase(test.schematic.field.case)
    test_schematic_rectangle = unittest.TestLoader().loadTestsFromTestCase(test.schematic.rectangle.case)
    test_schematic_from_string = unittest.TestLoader().loadTestsFromTestCase(test.schematic.from_string.case)

    test_pcb_helper = unittest.TestLoader().loadTestsFromTestCase(test.pcb.helper.case)
    test_pcb_layer = unittest.TestLoader().loadTestsFromTestCase(test.pcb.layer.case)

    test_suites = [
        test_type,

        test_schematic_field,
        test_schematic_rectangle,
    #   test_schematic_from_string,

        test_pcb_helper,
        test_pcb_layer
    ]
    suite = unittest.TestSuite(test_suites)
    unittest.TextTestRunner(verbosity = 2).run(suite)
