import climpred as cp


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
        cloud_cover = self.view.cloud_cover_slider.get()
        eps_1 = self.view.epsilon_1_slider.get()
        eps_2 = self.view.epsilon_2_slider.get()
        H_S = self.view.H_S_slider.get()
        H_L = self.view.H_L_slider.get()
        S_0 = self.view.S_0_slider.get()
        # The overwritten one is just a dummy because now we don't take
        # inputs from sliders yet
        input_value_overwritten = cp.calculate_temperature_matrix(cloud_cover=self.view.cloud_cover_slider.get(),
                                                                epsilon_1=self.view.epsilon_1_slider.get(), epsilon_2=self.view.epsilon_2_slider.get(),
                                                                H_S=self.view.H_S_slider.get(), H_L=self.view.H_L_slider.get(), S_0=self.view.S_0_slider.get())  # noqa
        print(input_value_overwritten)
        my_plot = cp.Plot(input_value_overwritten)
        print(cloud_cover, eps_1, eps_2, H_S, H_L, S_0)
        self.view._make_graph(my_plot)


if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
