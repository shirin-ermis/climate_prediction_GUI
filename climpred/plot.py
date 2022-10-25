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
        fig = plt.figure()
        plt.plot(T, heights)

        # Plot parameters
        plt.set_yticklabels(['TS', 'T1', 'T2'])
        fig.xlim(-100, 100)
        fig.ylabel('Height')
        fig.xlabel('Temperature / °C')
