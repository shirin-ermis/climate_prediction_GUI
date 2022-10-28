import unittest
import tkinter as tk
from numpy import NaN
import climpred as cp


class RangeTest(unittest.TestCase):
    """
    Tests model_out_of_range.py.
    """
    def test_check_model_range(self):
        """
        Tests function checking if values
        are beyond plot limits.
        """
        self.assertEqual(cp._check_model_range([-100, 0, 100]), None)
        tk.destroy('all')
        self.assertEqual(cp._check_model_range([-101, 3, 5]), 1)
        self.assertEqual(cp._check_model_range([-20, 90, 101]), 1)

        self.assertEqual(cp._check_model_range([NaN, 2, 100]), 1)
        self.assertEqual(cp._check_model_range([-101, NaN, 101]), 1)


if __name__ == "__main__":
    unittest.main()
