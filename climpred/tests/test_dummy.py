# Dummy test to be used as a template for unit testing

import unittest
import climpred as cp


class DummyTest(unittest.TestCase):
    """
    Tests the :class:`Dummy` class.
    """
    def test_create(self):
        """
        Tests Dummy creation.
        """
        dummy = cp.Model()
        self.assertEqual(dummy.value, '')
