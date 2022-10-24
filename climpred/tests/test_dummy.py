# Dummy test to be used as a template for unit testing

import unittest
import climpred as cp

dummy = 5 * 5 # just to have a test, would not be in normal testing

class DummyTest(unittest.TestCase):
    """
    Tests the :class:`Dummy` class.
    """
    def test_create(self):
        """
        Tests Dummy creation.
        """
        # dummy = cp.Dummy() # doesn't exist, oh well
        self.assertEqual(dummy, 25)

