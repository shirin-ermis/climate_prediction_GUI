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
        input_value = self.view.slider.get()
        # The overwritten one is just a dummy because now we don't take
        # inputs from sliders yet
        input_value_overwritten = cp.calculate_temperature_matrix(cloud_cover=self.view.slider.get())  # noqa
        print(input_value_overwritten)
        my_plot = cp.Plot(input_value_overwritten)
        print(input_value)
        self.view._make_graph(my_plot)


if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
