import tkinter as tk
import numpy as np

def _check_model_range(temperatures):
    if max(temperatures) > 100 or min(temperatures) < -100:
        tk.messagebox.showwarning("Model out of range",
                                  "The inputs provided leads to \
                                    temperatures out of range. \
                                    This will cause parts of the graph \
                                    to not be visible!")
        return 1

    if np.isnan(temperatures).any():
        tk.messagebox.showwarning("Model out of range",
                                  "The inputs provided leads to \
                                    NAN temperatures. \
                                    This will cause parts of the graph \
                                    to not be visible!")
        return 1