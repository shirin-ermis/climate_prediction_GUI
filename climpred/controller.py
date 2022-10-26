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

    def _on_slider_slide(self, event):
        input_value = self.view.slider.get()
        my_plot = cp.Plot(input_value)
        print(input_value)
        self.view._make_graph(my_plot)


if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
