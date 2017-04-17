import sys, os
import unittest

sys.path.insert(0, os.path.dirname(__file__))

import test_hashes

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suites = [loader.loadTestsFromTestCase(test_hashes.TestHashFunctions)]
    test_suite = unittest.TestSuite(suites)
    unittest.TextTestRunner().run(test_suite)
