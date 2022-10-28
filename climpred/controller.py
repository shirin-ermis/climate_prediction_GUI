import climpred as cp
import numpy as np
import tkinter as tk
from tkinter import ttk


class Controller():
    """
    Main controller
    """

    def __init__(self):
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
        flag = cp._check_model_range(temperatures, type='RUN')

        my_plot = cp.Plot_general(temperatures)
        self.view._make_graph(my_plot)

    def _on_press_faq_button(self):
        new_window = tk.Toplevel()
        new_window.geometry("700x200")
        new_window.title("Model FAQ")
        # frame = tk.Frame(new_window, width=700, height=200)
        # frame.grid(sticky='nsew')

        # Create a canvas object
        hscroll = ttk.Scrollbar(new_window, orient='horizontal')
        vscroll = ttk.Scrollbar(new_window, orient='vertical')
        canvas = tk.Canvas(new_window,
                           scrollregion=(0, 0, 700, 800),
                           yscrollcommand=vscroll.set,
                           xscrollcommand=hscroll.set)
        canvas.grid(column=0, row=0, sticky='nsew')
        hscroll.grid(column=0, row=1, sticky='ew')
        vscroll.grid(column=1, row=0, sticky='ns')
        hscroll['command'] = canvas.xview
        vscroll['command'] = canvas.yview
        new_window.grid_columnconfigure(0, weight=1)
        new_window.grid_rowconfigure(0, weight=1)

        # Add a text in Canvas
        file_text = open('./FAQ.txt', 'r')
        raw_text = str(file_text.read())
        # markdown_text = markdown.markdown(file_text.read())
        canvas.create_text(10, 10,
                           text=raw_text,
                           fill="black",
                           anchor='nw',
                           width=600)
        # canvas.pack()


if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
