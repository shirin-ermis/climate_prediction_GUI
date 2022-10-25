import unittest

import matplotlib
import climpred as cp
import matplotlib.pyplot as plt
import numpy as np
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
