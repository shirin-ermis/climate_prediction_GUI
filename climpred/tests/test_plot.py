# import unittest
import climpred as cp
import matplotlib.pyplot as plt

# class PlotTest(unittest.TestCase):
#     """
#     Tests the :class:`Model` class.
#     """
#     def test_create_plot(self):
#         """
#         Tests plot creation
#         """
our_plot = cp.Plot()
our_plot.create_plot(1,2,4)
plt.show()
