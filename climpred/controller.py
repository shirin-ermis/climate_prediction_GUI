import climpred as cp
import numpy as np


class Controller():
    """
    Main controller
    """

    def __init__(self):
        self.model = cp.Model()
        self.view = cp.View(self)

    def main(self):
        self.view.main()

    def _on_press_calculate_button(self):
        # The input_value will be taken from the sliders
        # The overwritten one is just a dummy because now we don't take
        # inputs from sliders yet
        input_value_overwritten = cp.calculate_temperature_matrix(
            cloud_cover=self.view.cloud_cover_slider.get(),
            epsilon_1=self.view.epsilon_1_slider.get(),
            epsilon_2=self.view.epsilon_2_slider.get(),
            H_S=self.view.H_S_slider.get(),
            H_L=self.view.H_L_slider.get(),
            S_0=self.view.S_0_slider.get()
        )
        my_plot = cp.Plot(input_value_overwritten)
        self.view._make_graph(my_plot)

    def _on_press_advanced_button(self):
        self.view._create_advanced_window()

    def _on_press_advanced_calculate_button(self):
        # The input_value will be taken from the sliders
        # The overwritten one is just a dummy because now we don't take
        # inputs from sliders yet
        layers = self.view.layers.get(),
        cloud_cover = self.view.advanced_cloud_cover_slider.get(),
        epsilons = self.view.advanced_epsilon_entry.get(),
        H = self.view.advanced_H_entry.get(),
        S_0 = self.view.advanced_solar_constant_slider.get()

        # Check if inputs are valid
        flag = cp._check_inputs(layers, epsilons, H)
        if flag == 1:
            flag = 0
            return

        # transform variables to correct types
        layers = int(layers[0])
        cloud_cover = cloud_cover[0]
        epsilons = epsilons[0].split(' ')
        epsilons = np.array([float(x) for x in epsilons])
        H = H[0].split(' ')
        H = np.array([float(x) for x in H])
        temperatures = cp.calculate_temperature_matrix_general(
            layers=layers,
            cloud_cover=cloud_cover,
            epsilons=epsilons,
            H=H,
            S_0=S_0
        )
        print(temperatures)
        # Check if model is within range
        flag = cp._check_model_range(temperatures)

        my_plot = cp.Plot_general(temperatures)
        self.view._make_graph(my_plot)


if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
