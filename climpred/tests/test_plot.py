import unittest
import climpred as cp
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TKagg')


class PlotTest(unittest.TestCase):
    """
    Tests the :class:`Plot` class.
    """
    def test_create_plot(self):
        """
        Tests plot creation
        """
        T = np.array([1, 2, 3])
        plot = cp.Plot(T)
        self.assertEqual(type(plot.plot), type(plt.figure()))
