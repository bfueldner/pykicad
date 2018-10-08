import unittest

import test.schematic.type
import test.schematic.element
import test.schematic.from_str

import test.pcb.helper
import test.pcb.type
import test.pcb.layer
import test.pcb.element

if __name__ == '__main__':
    test_schematic_type = unittest.TestLoader().loadTestsFromTestCase(test.schematic.type.case)
    test_schematic_element = unittest.TestLoader().loadTestsFromTestCase(test.schematic.element.case)
    test_schematic_from_str = unittest.TestLoader().loadTestsFromTestCase(test.schematic.from_str.case)

    test_pcb_helper = unittest.TestLoader().loadTestsFromTestCase(test.pcb.helper.case)
    test_pcb_type = unittest.TestLoader().loadTestsFromTestCase(test.pcb.type.case)
    test_pcb_layer = unittest.TestLoader().loadTestsFromTestCase(test.pcb.layer.case)
    test_pcb_element = unittest.TestLoader().loadTestsFromTestCase(test.pcb.element.case)

    test_suites = [
        test_schematic_type,
        test_schematic_element,
     #  test_schematic_from_str,

        test_pcb_helper,
        test_pcb_type,
        test_pcb_layer,
        test_pcb_element
    ]
    suite = unittest.TestSuite(test_suites)
    unittest.TextTestRunner(verbosity = 2).run(suite)
