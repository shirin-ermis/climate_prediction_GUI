import tkinter as tk
import numpy as np

def _check_inputs(layers, epsilons, H):
    # Check if inputs are empty
    if layers[0]=='':
        tk.messagebox.showerror("Empty", "Number of layers is empty")
        return 1
    if epsilons[0]=='':
        tk.messagebox.showerror("Empty", "There are no emmisitivities introduced")
        return 1
    if H[0]=='':
        tk.messagebox.showerror("Empty", "There are no convective fluxes introduced")
        return 1

    # Check that layers is int
    try:
        layers = int(layers[0])
    except ValueError:
        tk.messagebox.showerror("Value Error", "Number of layers must be a single integer")
        return 1

    # Split vectors in constituent elements
    epsilons = epsilons[0].split(' ')
    H = H[0].split(' ')

    # Check that elements can be transformed to float type
    for element in epsilons:
        try:
            float(element)
        except ValueError:
            tk.messagebox.showerror("Value Error", "The elements of the emmisitivity must be floats separated by space")
            return 1
    for element in H:
        try:
            float(element)
        except ValueError:
            tk.messagebox.showerror("Value Error", "The elements of the convective fluxes must be floats separated by space")
            return 1

    # Transform the variables into the correct types
    epsilons = np.array([float(x) for x in epsilons])
    H = np.array([float(x) for x in H])

    # Check that elements are within correct ranges
    if layers < 1:
        tk.messagebox.showerror("Value Error", "The number of layers must be greater than 1")
        return 1
    for element in epsilons:
        if element < 0 or element > 1:
            tk.messagebox.showerror("Value Error", "Emmisitivities must be between 0 and 1 (including)")
            return 1
    for element in H:
        if element < 0:
            tk.messagebox.showerror("Value Error", "Convective fluxes must be non-negative")
            return 1

    # Check that the number of elements in the vectors is equal to the number of layers
    if len(epsilons) != layers:
        tk.messagebox.showerror("Model Error", "The number of emmisitivity elemets must equal the number of layers")
        return 1
    if len(H) != layers:
        tk.messagebox.showerror("Model Error", "The number of convective fluxes elemets must equal the number of layers")
        return 1
