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
        if flag is not None:
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
        new_window.geometry("600x600")
        new_window.title("Model FAQ")
        # frame = tk.Frame(new_window, width=700, height=200)
        # frame.grid(sticky='nsew')

        # Create a canvas object
        hscroll = ttk.Scrollbar(new_window, orient='horizontal')
        vscroll = ttk.Scrollbar(new_window, orient='vertical')
        canvas = tk.Canvas(new_window,
                           scrollregion=(0, 0, 600, 1200),
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
        file_text = ('FAQ \n \
                    ---------------------- \n \
                    \n \
                    * What am I looking at? \n \
                    You\'re looking at an atmospheric temperature profile. \n \
                    The air temperature is calculated at a number of \n \
                    levels (initially three) beginning at the surface  \n \
                    and ending at the top of the atmosphere. \n \
                    \n \
                    * Why is it zero all the way up? \n \
                    We haven\'t given the model any information yet. \n \
                    For instance, the starting value for the solar  \n \
                    constant, which is how much energy (light)  \n \
                    from the sun is reaching Earth, is initially set at  \n \
                    10 Watts per square meter (W/m^(-2)). With such a low  \n \
                    energy input, the Earth would be very cold.  \n \
                    Change the value for the solar constant \n \
                    to about 1370 W/m^(-2) - that\'s about how much it is \n \
                    in real life. \
                    \n \n \
                    * What are the other values I can change? \n \
                    - Cloud cover is the percentage of the planet shaded \n \
                    by clouds. The higher the proportion of cloud cover, \n \
                    the more energy they reflect back to space. \n \
                    Clouds aren\'t perfect reflectors - even thick white \n \
                    clouds let about a quarter of the sunlight through - \n \
                    but if the whole planet were covered with clouds, it \n \
                    would be quite cold and dark in their shade. \n \
                    The real value for planet Earth is about 35%. \n \
                    - The emissitivities for the layers of the atmosphere \n \
                    are values between 0 and 1 that describe how much \n \
                    energy they absorb and emit. Something with a low  \n \
                    emissivity won\'t absorb much energy, so it won\'t  \n \
                    emit much either. \n \
                    The emissitivity of an atmospheric layer is mostly \n \
                    determined by the amount of water it contains;  \n \
                    it can be low or high.  \n \
                    Try out a few different values. \n \
                    - The convective heat fluxes between layers describe \n \
                    how much energy is transported upwards by  \n \
                    non-radiative processes, like the rising of warm air  \n \
                    (convection). \n \
                    Like the emissitivity for a given layer, there isn\'t \n \
                    a single standard constant value in real life.  \n \
                    Try some low and high values. What happens if the  \n \
                    convective flux in one layer is much higher than  \n \
                    in the others? \n \
                    \n \
                    * How do I use the model? \n \
                    Adjust the sliders, then click "Calculate model". \n \
                    To add more layers to the model, click  \n \
                    "Advanced model". \n \
                    \n \n \
                    * What calculations does the model perform? \n \
                    The model solves for the temperature at a range of \n \
                    points in the atmosphere using a set of  \n \
                    matrix equations. \n \
                    For details, see \n \
                    https://biocycle.atmos.colostate.edu/shiny/2layer/. \n \
        ')

        # markdown_text = markdown.markdown(file_text.read())
        canvas.create_text(10, 10,
                           text=file_text,
                           fill="black",
                           anchor='nw',
                           width=600)
        # canvas.pack()


if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
