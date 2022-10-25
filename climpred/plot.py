# import climpred as cp
import matplotlib.pyplot as plt
import numpy as np


class Plot():
    """
    Class to create plots for the model that displays the temperatures
    in the atmospheric layers
    """

    def __init__(self, slider_value):
        self.plot = None
        self.create_plot(slider_value, 2, 3)

    def create_plot(self, TS, T1, T2):
        # Data
        T = np.array([TS, T1, T2])
        heights = np.array([0, 1, 2])

        # Plotting
        self.plot = plt.figure()
        plt.plot(T, heights)

        # Plot parameters
        plt.yticks(ticks=[0, 1, 2], labels=['surface', 'lower level', 'upper level'])
        # plt.yticklabel(['surface', 'lower level', 'upper level'])
        plt.xlim(-100, 100)
        plt.ylabel('Height')
        plt.xlabel('Temperature / °C')
