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

        self._make_slider()

        self._make_calculate_button()

        self._center_window()

    def main(self):
        self.mainloop()

    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.grid(sticky="nsew")

    def _make_control_frame(self):
        self.control_frame = ttk.Frame(self.main_frm)
        self.control_frame.grid(column=0, sticky="nsw")

    def _make_graph_frame(self):
        self.graph_frame = ttk.Frame(self.main_frm)
        self.graph_frame.grid(column=1, sticky="nse")

    def _initiate_graph(self):
        my_dummy_plot = cp.Plot([0, 0, 0])
        self._make_graph(my_dummy_plot)

    def _make_graph(self, plot_obj: object):
        plt.close('all')
        for widgets in self.graph_frame.winfo_children():
            widgets.destroy()
        figure_canvas = FigureCanvasTkAgg(plot_obj.plot, self.graph_frame)
        figure_canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def _center_window(self):
        self.update()

        width = self.winfo_width()
        height = self.winfo_height()

        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2

        self.geometry(
            f'{width}x{height}+{x_offset}+{y_offset}'
        )

    def _make_slider(self):
        self.slider = tk.Scale(self.control_frame, from_=0, to=200,
                               orient=tk.HORIZONTAL, length=250)
        self.slider.set(0)
        self.slider.grid(row=1)

    def _make_Cloud_Cover_Label(self):
        self._Cloud_Cover_Label = tk.Label(self.control_frame,
                                           text="Cloud Cover as %")

    def _make_calculate_button(self):
        self.btn = tk.Button(self.control_frame, text="Calculate model",
                             command=self.controller._on_press_calculate_button) # noqa
        self.btn.grid(row=0)
