import matplotlib.pyplot as plt
import numpy as np


class Plot_general():
    """
    Class to create plots for the model that displays the temperatures
    in the atmospheric layers
    """

    def __init__(self, T):
        self.plot = None
        self.create_plot(T)

    def create_plot(self, T):
        # Data
        heights = np.array(range(len(T)))

        # Plotting
        self.plot = plt.figure()
        plt.plot(T, heights)
        plt.title('Atmospheric temperature profile')

        # Plot parameters
        self.height_ticks = range(len(T))
        self.height_labels = [str(x) for x in range(1, len(T))]
        self.height_labels.insert(0, 'Surface')
        plt.yticks(ticks=self.height_ticks, labels=self.height_labels)
        plt.xlim(-100, 100)
        plt.ylabel('Height')
        plt.xlabel('Temperature / °C')
