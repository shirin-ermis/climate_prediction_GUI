
import unittest
import climpred as cp


class ModelTest(unittest.TestCase):
    """
    Tests the :class:`Model` class.
    """
    def test_create(self):
        """
        Tests Model creation.
        """
        model = cp.Model()
        self.assertEqual(model.value, 1)
