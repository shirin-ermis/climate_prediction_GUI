import unittest
import matplotlib.pyplot as plt
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
        self.assertEqual(type(model.plot), type(plt.figure()))


if __name__ == "__main__":
    unittest.main()
