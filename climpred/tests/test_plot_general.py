import unittest
import climpred as cp
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa


class PlotTest(unittest.TestCase):
    """
    Tests the :class:`Plot_general` class.
    """
    def test_create_plot(self):
        """
        Tests plot creation
        """
        T = np.array([2, 3, 4, 5, 6])
        plot = cp.Plot_general(T)
        self.assertEqual(type(plot.plot), type(plt.figure()))
        self.assertEqual(len(plot.height_ticks), len(plot.height_labels))
