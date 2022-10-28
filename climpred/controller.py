import climpred as cp
import tkinter as tk
import markdown
from tkinter import ttk


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
        input_value_overwritten = cp.calculate_temperature_matrix(cloud_cover=self.view.slider.get() / 100)  # noqa
        print(input_value_overwritten)
        my_plot = cp.Plot(input_value_overwritten)
        print(input_value)
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
                           scrollregion=(0, 0, 700, 600),
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
        file_text = open('FAQ.txt', 'r')
        markdown_text = markdown.markdown(file_text.read())
        canvas.create_text(0, 0,
                           text=markdown_text,
                           fill="black",
                           anchor='nw',
                           width=600)
        # canvas.pack()


if __name__ == '__main__':
    calculator = Controller()
    calculator.main()
