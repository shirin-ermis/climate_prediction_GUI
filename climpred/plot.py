# import climpred as cp
import matplotlib.pyplot as plt
import numpy as np


class Plot():
    """
    Class to create plots for the model that displays the temperatures
    in the atmospheric layers
    """

    def __init__(self):
        self.plot = None

    def creat_plot(self, TS, T1, T2):
        # Data
        T = np.array([TS, T1, T2])
        heights = np.array([0, 1, 2])

        # Plotting
        self.plot = plt.figure()
        plt.plot(T, heights)

        # Plot parameters
        plt.set_yticks([0, 1, 2])
        plt.set_yticklabels(['surface', 'lower level', 'upper level'])
        self.plot.xlim(-100, 100)
        self.plot.ylabel('Height')
        self.plot.xlabel('Temperature / °C')
