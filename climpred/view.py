from tkinter import ttk
import climpred as cp
import tkinter as tk
import matplotlib
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
)
import matplotlib # noqa
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa


class View(tk.Tk):
    """ Docs
    """
    PAD = 10

    def __init__(self, controller):

        super().__init__()

        self.controller = controller

        self.title('Climate Modelling')

        self._make_main_frame()

        self._make_control_frame()

        self._make_graph_frame()

        self._initiate_graph()

        self._make_cloud_cover_slider()

        self._make_epsilon_1_slider()

        self._make_epsilon_2_slider()

        self._make_S_0_slider()

        self._make_H_S_slider()

        self._make_H_L_slider()

        self._make_calculate_button()

        self._center_window()

        self._make_advanced_button()

        self._make_faq_button()

        self._make_graph_label()

    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.grid(sticky="nsew")

    def _make_control_frame(self):
        self.control_frame = ttk.Frame(self.main_frm)
        self.control_frame.grid(column=0, row=0, sticky="ns")

    def _make_graph_frame(self):
        self.graph_frame = ttk.Frame(self.main_frm)
        self.graph_frame.grid(column=1, row=0, sticky="ns")

    def _initiate_graph(self):
        my_dummy_plot = cp.Plot([0, 0, 0])
        self._make_graph(my_dummy_plot)

    def _make_graph(self, plot_obj: object):
        plt.close('all')
        for widgets in self.graph_frame.winfo_children():
            widgets.destroy()
        figure_canvas = FigureCanvasTkAgg(plot_obj.plot, self.graph_frame)
        figure_canvas.get_tk_widget().grid(row=1, ipadx=150, ipady=50,
                                           sticky="ns")
        self._make_graph_label()

    def _center_window(self):
        self.update()

        # width = self.winfo_width()
        # height = self.winfo_height()

        # x_offset = (self.winfo_screenwidth() - width) // 2
        # y_offset = (self.winfo_screenheight() - height) // 2

        self.geometry("1920x1080")

        # self.geometry(
        #     f'{width}x{height}+{x_offset}+{y_offset}'
        # )

    def _make_cloud_cover_slider(self):
        self.cloud_cover_slider = tk.Scale(
            self.control_frame, from_=0, to=1,
            orient=tk.HORIZONTAL, length=250,
            label="Cloud Cover", resolution=0.01
        )
        self.cloud_cover_slider.set(0)
        self.cloud_cover_slider.grid(row=1)

    def _make_calculate_button(self):
        self.btn_calc = tk.Button(self.control_frame, text="Calculate model",
                             command=self.controller._on_press_calculate_button) # noqa
        self.btn_calc.grid(row=0)

    def _make_faq_button(self):
        self.btn_faq = tk.Button(self.control_frame, text="Model FAQ",
                             command=self.controller._on_press_faq_button) # noqa
        self.btn_faq.grid(row=0, column=1)

    def _make_new_window(self):
        pass
        # new_window = tk.Toplevel()
        # tk.Label(master=new_window, text="This is a new window").pack()

    def _make_epsilon_1_slider(self):
        self.epsilon_1_slider = tk.Scale(
            self.control_frame, from_=0.01, to=1,
            orient=tk.HORIZONTAL, length=250,
            label="Emissivity for lower layer", resolution=0.01
        )
        self.epsilon_1_slider.set(0.01)
        self.epsilon_1_slider.grid(row=2)

    def _make_epsilon_2_slider(self):
        self.epsilon_2_slider = tk.Scale(
            self.control_frame, from_=0.01, to=1,
            orient=tk.HORIZONTAL, length=250,
            label="Emissivity for upper layer", resolution=0.01
        )
        self.epsilon_2_slider.set(0.01)
        self.epsilon_2_slider.grid(row=3)

    def _make_S_0_slider(self):
        self.S_0_slider = tk.Scale(
            self.control_frame, from_=10, to=2000,
            orient=tk.HORIZONTAL, length=250,
            label="Solar Constant (W/m^(-2))", resolution=10
        )
        self.S_0_slider.set(10)
        self.S_0_slider.grid(row=6)

    def _make_H_S_slider(self):
        self.H_S_slider = tk.Scale(
            self.control_frame, from_=0, to=200,
            orient=tk.HORIZONTAL, length=250,
            label="Convective flux for upper layer (W/m^(-2))", resolution=10
        )
        self.H_S_slider.set(0)
        self.H_S_slider.grid(row=4)

    def _make_H_L_slider(self):
        self.H_L_slider = tk.Scale(
            self.control_frame, from_=0, to=200,
            orient=tk.HORIZONTAL, length=250,
            label="Convective flux for lower layer (W/m^(-2))", resolution=10
        )
        self.H_L_slider.set(0)
        self.H_L_slider.grid(row=5)

    def _make_advanced_button(self):
        self.advanced_btn = tk.Button(self.control_frame,
                                      text="Advanced model",
                             command=self.controller._on_press_advanced_button) # noqa
        self.advanced_btn.grid(row=8)

    def _create_advanced_window(self):
        # Toplevel object which will
        # be treated as a new window
        self.advanced_Window = tk.Toplevel(self)

        # sets the title of the
        # Toplevel widget
        self.advanced_Window.title("Advanced modeller")

        # sets the geometry of toplevel
        self.advanced_Window.geometry("255x350")

        # Create advanced frame
        self.advanced_frm = ttk.Frame(self.advanced_Window)
        self.advanced_frm.grid(sticky="nsew")

        # Create advanced cloud cover slider
        self.advanced_cloud_cover_slider = tk.Scale(
            self.advanced_frm, from_=0, to=1,
            orient=tk.HORIZONTAL, length=250,
            label="Cloud Cover", resolution=0.01
        )
        self.advanced_cloud_cover_slider.set(0)
        self.advanced_cloud_cover_slider.grid(row=0)

        # Create number of layers entry
        self.layers = tk.StringVar()
        self.advanced_layers_entry = tk.Entry(
            self.advanced_frm,
            justify='right',
            textvariable=self.layers,
        )
        self.advanced_layers_entry.grid(row=2)
        tk.Label(self.advanced_frm, text='Number of layers').grid(row=1)

        # Create advanced epsilon entry
        self.epsilon = tk.StringVar()
        self.advanced_epsilon_entry = tk.Entry(
            self.advanced_frm,
            justify='right',
            textvariable=self.epsilon,
        )
        self.advanced_epsilon_entry.grid(row=4)
        tk.Label(self.advanced_frm, text='Emmisivity vector').grid(row=3)

        # Create advanced H entry
        self.H = tk.StringVar()
        self.advanced_H_entry = tk.Entry(
            self.advanced_frm,
            justify='right',
            textvariable=self.H,
        )
        self.advanced_H_entry.grid(row=6)
        self.label = tk.Label(self.advanced_frm,
                              text='Convective flux vector').grid(row=5)

        # Create advanced Solcar constant slider
        self.advanced_solar_constant_slider = tk.Scale(
            self.advanced_frm, from_=10, to=2000,
            orient=tk.HORIZONTAL, length=250,
            label="Solar constant", resolution=0.01
        )
        self.advanced_solar_constant_slider.set(0)
        self.advanced_solar_constant_slider.grid(row=7)

        # Create advanced calculate button
        self.advanced_calculate_btn = tk.Button(self.advanced_frm,
                                                text="Calculate model",
                             command=self.controller._on_press_advanced_calculate_button) # noqa
        self.advanced_calculate_btn.grid(row=8)

    def _make_graph_label(self):
        f = open('top-bar-explanation.txt', 'r')
        raw_text = f.read()
        self.graph_label = tk.Label(self.graph_frame,
                                    text=raw_text,
                                    wraplength=700)
        self.graph_label.grid(row=0)
