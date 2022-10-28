import tkinter as tk
import numpy as np


def _check_inputs(layers, epsilons, H, type_run: str = "RUN"):
    # Check if inputs are empty

    if layers[0] == '':
        if type_run == 'RUN':
            tk.messagebox.showerror("Empty", "Number of layers is empty")
        return 1
    if epsilons[0] == '':
        if type_run == 'RUN':
            tk.messagebox.showerror("Empty",
                                    "There are no emmisitivities introduced")
        return 2
    if H[0] == '':
        if type_run == 'RUN':
            tk.messagebox.showerror("Empty",
                                    "There are no convective \
                                        fluxes introduced")
        return 3

    # Check that layers is int
    try:
        layers = int(layers[0])
    except ValueError:
        if type_run == 'RUN':
            tk.messagebox.showerror("Value Error",
                                    "Number of layers must \
                                        be a single integer")
        return 4

    # Split vectors in constituent elements
    epsilons = epsilons[0].split(' ')
    H = H[0].split(' ')

    # Check that elements can be transformed to float type
    for element in epsilons:
        try:
            float(element)
        except ValueError:
            if type_run == 'RUN':
                tk.messagebox.showerror("Value Error",
                                        "The elements of the \
                                            emmisitivity must be \
                                        floats separated by space")
            return 5
    for element in H:
        try:
            float(element)
        except ValueError:
            if type_run == 'RUN':
                tk.messagebox.showerror("Value Error",
                                        "The elements of the \
                                            convective fluxes \
                                        must be floats separated by space")
            return 6

    # Transform the variables into the correct types
    epsilons = np.array([float(x) for x in epsilons])
    H = np.array([float(x) for x in H])

    # Check that elements are within correct ranges
    if layers < 1:
        if type_run == 'RUN':
            tk.messagebox.showerror("Value Error",
                                    "The number of layers must \
                                        be greater than 1")
        return 7
    for element in epsilons:
        if element < 0 or element > 1:
            if type_run == 'RUN':
                tk.messagebox.showerror("Value Error",
                                        "Emmisitivities must be \
                                            between 0 and 1 \
                                        (including)")
            return 8
    for element in H:
        if element < 0:
            if type_run == 'RUN':
                tk.messagebox.showerror("Value Error",
                                        "Convective fluxes must \
                                            be non-negative")
            return 9

    # Check that the number of elements in the vectors is equal to
    # the number of layers
    if len(epsilons) != layers:
        if type_run == 'RUN':
            tk.messagebox.showerror("Model Error",
                                    "The number of emmisitivity elemets must \
                                    equal the number of layers")
        return 10
    if len(H) != layers:
        if type_run == 'RUN':
            tk.messagebox.showerror("Model Error",
                                    "The number of convective fluxes elemets \
                                    must equal the number of layers")
        return 11
