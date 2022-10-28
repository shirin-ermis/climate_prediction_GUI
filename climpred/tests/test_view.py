#
# test_view.py
#
import unittest
import tkinter as tk
import tkinter.ttk as ttk
import climpred as cp


class ViewTest(unittest.TestCase):
    """
    Tests the :class:`View` class.
    """

    # set global variables for testing
    global ctrl, view
    ctrl = cp.Controller()
    view = cp.View(ctrl)

    def test_init(self):
        with self.assertRaises(AttributeError):
            cp.View(111)
        self.assertEqual(view.controller, ctrl)
        self.assertEqual(view.title(), 'Climate Modelling')

    def test_make_main_frame(self):
        isinstance(view.main_frm, type(ttk.Frame()))
        mf_info = view.main_frm.grid_info()

        self.assertEqual(mf_info['column'], 0)
        self.assertEqual(mf_info['row'], 0)
        self.assertEqual(mf_info['columnspan'], 1)
        self.assertEqual(mf_info['rowspan'], 1)
        self.assertEqual(mf_info['sticky'], 'nesw')

    def test_make_control_frame(self):
        isinstance(view.control_frame, type(ttk.Frame()))
        cf_info = view.control_frame.grid_info()

        self.assertEqual(cf_info['column'], 0)
        self.assertEqual(cf_info['row'], 0)
        self.assertEqual(cf_info['columnspan'], 1)
        self.assertEqual(cf_info['rowspan'], 1)
        self.assertEqual(cf_info['sticky'], 'ns')

    def test_make_graph_frame(self):
        isinstance(view.graph_frame, type(ttk.Frame()))
        gf_info = view.graph_frame.grid_info()

        self.assertEqual(gf_info['column'], 1)
        self.assertEqual(gf_info['row'], 0)
        self.assertEqual(gf_info['columnspan'], 1)
        self.assertEqual(gf_info['rowspan'], 1)
        self.assertEqual(gf_info['sticky'], 'ns')

    def test_initiate_graph(self):
        # self.assertTrue(plt.fignum_exists(my_dummy_plot))

        # test to make sure figure plots [0,0,0]
        pass

    def test_make_graph(self):
        graph_info = view.graph_frame.winfo_children()[0].grid_info()

        self.assertEqual(graph_info['row'], 0)
        self.assertEqual(graph_info['ipadx'], 150)
        self.assertEqual(graph_info['ipady'], 100)
        self.assertEqual(graph_info['sticky'], 'ns')

    def test_center_window(self):
        view.geometry("800x600")
        view._center_window()

        dimensions = '800x600'
        new_geometry = view.geometry().split('+')
        self.assertEqual(new_geometry[0], dimensions)

    def test_make_cloud_cover_slider(self):
        view._make_cloud_cover_slider()
        self.assertEqual(view.cloud_cover_slider.get(), 0)
        self.assertEqual(view.cloud_cover_slider['orient'], 'horizontal')
        self.assertEqual(view.cloud_cover_slider['from'], 0.0)
        self.assertEqual(view.cloud_cover_slider['to'], 1.0)
        self.assertEqual(view.cloud_cover_slider['label'], "Cloud Cover")
        self.assertEqual(view.cloud_cover_slider['resolution'], 0.01)

    def test_make_calculate_button(self):
        view._make_calculate_button
        view.btn.invoke()
        self.assertEqual(view.btn['text'], "Calculate model")

    def test_make_epsilon_1_slider(self):
        view._make_epsilon_1_slider()
        self.assertEqual(view.epsilon_1_slider.get(), 0.01)
        self.assertEqual(view.epsilon_1_slider['orient'], 'horizontal')
        self.assertEqual(view.epsilon_1_slider['from'], 0.01)
        self.assertEqual(view.epsilon_1_slider['to'], 1.0)
        self.assertEqual(view.epsilon_1_slider['label'], "Emissivity for lower layer")
        self.assertEqual(view.epsilon_1_slider['resolution'], 0.01)

    def test_make_epsilon_2_slider(self):
        view._make_epsilon_2_slider()
        self.assertEqual(view.epsilon_2_slider.get(), 0.01)
        self.assertEqual(view.epsilon_2_slider['orient'], 'horizontal')
        self.assertEqual(view.epsilon_2_slider['from'], 0.01)
        self.assertEqual(view.epsilon_2_slider['to'], 1.0)
        self.assertEqual(view.epsilon_2_slider['label'], "Emissivity for upper layer")
        self.assertEqual(view.epsilon_2_slider['resolution'], 0.01)

    def test_make_S_0_slider(self):
        view._make_S_0_slider()
        self.assertEqual(view.S_0_slider.get(), 10)
        self.assertEqual(view.S_0_slider['orient'], 'horizontal')
        self.assertEqual(view.S_0_slider['from'], 10.0)
        self.assertEqual(view.S_0_slider['to'], 2000.0)
        self.assertEqual(view.S_0_slider['label'], "Solar Constant (W/m^(-2))")
        self.assertEqual(view.S_0_slider['resolution'], 10)

    def test_make_H_S_slider(self):
        view._make_H_S_slider()
        self.assertEqual(view.H_S_slider.get(), 0)
        self.assertEqual(view.H_S_slider['orient'], 'horizontal')
        self.assertEqual(view.H_S_slider['from'], 0.0)
        self.assertEqual(view.H_S_slider['to'], 200.0)
        self.assertEqual(view.H_S_slider['label'], "Convective flux for upper layer (W/m^(-2))")
        self.assertEqual(view.H_S_slider['resolution'], 10)

    def test_make_H_L_slider(self):
        view._make_H_L_slider()
        self.assertEqual(view.H_L_slider.get(), 0)
        self.assertEqual(view.H_L_slider['orient'], 'horizontal')
        self.assertEqual(view.H_L_slider['from'], 0.0)
        self.assertEqual(view.H_L_slider['to'], 200.0)
        self.assertEqual(view.H_L_slider['label'], "Convective flux for lower layer (W/m^(-2))")
        self.assertEqual(view.H_L_slider['resolution'], 10)

    def test_make_advanced_button(self):
        view._make_advanced_button()
        view.advanced_btn.invoke()
        self.assertEqual(view.advanced_btn['text'], "Advanced model")

    def test_create_advanced_window(self):
        # testing for Window and Frame properties
        view._create_advanced_window()

        self.assertEqual(view.advanced_Window.title(), "Advanced modeller")
        isinstance(view.advanced_frm, type(ttk.Frame))
        self.assertEqual(view.advanced_frm.grid_info()['sticky'], "nesw")

    def test_Advanced_Cloud_Cover_Slider(self):
        # testing for Advanced Cloud Cover Slider
        view._create_advanced_window()

        self.assertEqual(view.advanced_cloud_cover_slider.get(), 0)
        self.assertEqual(view.advanced_cloud_cover_slider['orient'], 'horizontal')
        self.assertEqual(view.advanced_cloud_cover_slider['from'], 0.0)
        self.assertEqual(view.advanced_cloud_cover_slider['to'], 1.0)
        self.assertEqual(view.advanced_cloud_cover_slider['label'], "Cloud Cover")
        self.assertEqual(view.advanced_cloud_cover_slider['resolution'], 0.01)

    def test_Number_of_Layers_Entry(self):
        # testing for Number of Layers Entry
        view._create_advanced_window()

        isinstance(view.layers, type(tk.StringVar))
        self.assertEqual(view.advanced_layers_entry['justify'], 'right')
        self.assertEqual(view.advanced_frm.winfo_children()[2]['text'], 'Number of layers')

    def test_Advanced_Epsilon_Entry(self):
        # testing for Advanced Epsilon Entry
        view._create_advanced_window()

        isinstance(view.epsilon, type(tk.StringVar))
        self.assertEqual(view.advanced_epsilon_entry['justify'], 'right')
        self.assertEqual(view.advanced_frm.winfo_children()[4]['text'], 'Emmisivity vector')

    def test_Advanced_H_Entry(self):
        # testing for Advanced H Entry
        view._create_advanced_window()

        isinstance(view.layers, type(tk.StringVar))
        self.assertEqual(view.advanced_layers_entry['justify'], 'right')
        self.assertEqual(view.advanced_frm.winfo_children()[6]['text'], 'Convective flux vector')

    def test_Advanced_Solar_Constant_Slider(self):
        # testing for Advanced Solar Constant Slider
        view._create_advanced_window()

        self.assertEqual(view.advanced_solar_constant_slider.get(), 10.0)
        self.assertEqual(view.advanced_solar_constant_slider['orient'], 'horizontal')
        self.assertEqual(view.advanced_solar_constant_slider['from'], 10.0)
        self.assertEqual(view.advanced_solar_constant_slider['to'], 2000.0)
        self.assertEqual(view.advanced_solar_constant_slider['label'], "Solar constant")
        self.assertEqual(view.advanced_solar_constant_slider['resolution'], 0.01)

    def test_Advanced_Calculate_Button(self):
        # testing for advanced calculate button
        view._create_advanced_window()
        
        view.advanced_calculate_btn.invoke()
        self.assertEqual(view.btn['text'], "Calculate model")


if __name__ == "__main__":
    unittest.main()
