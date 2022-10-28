import unittest
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
        self.assertEqual(cp._check_model_range([-100, 0, 100], type='TEST'),
                         None)
        self.assertEqual(cp._check_model_range([-101, 3, 5], type='TEST'), 1)
        self.assertEqual(cp._check_model_range([-20, 90, 101], type='TEST'), 1)

        self.assertEqual(cp._check_model_range([NaN, 2, 100], type='TEST'), 1)
        self.assertEqual(cp._check_model_range([-101, NaN, 101], type='TEST'),
                         1)


if __name__ == "__main__":
    unittest.main()
