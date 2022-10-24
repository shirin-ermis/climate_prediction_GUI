import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)

class View(tk.Tk):
    """ Docs
    """
    PAD = 10
    
    def __init__(self, controller):
        
        super().__init__()
        
        self.controller = controller
        
        self.title('Climate Modelling')
        
        self._make_main_frame()
        
        self._make_graph()
        
        self._center_window()
        
    def main(self):
        self.mainloop()
        
    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)
        
    def _make_graph(self):
        x = np.linspace(0,1,100)
        y = np.sin(10*x)
        
        graph_figure = Figure(figsize=(6, 4), dpi=100)
        figure_canvas = FigureCanvasTkAgg(graph_figure, self)
        axes = graph_figure.add_subplot()
        axes.plot(x,y)
        axes.set_title('A GRAPH')
        axes.set_ylabel('y')
        axes.set_xlabel('x')
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