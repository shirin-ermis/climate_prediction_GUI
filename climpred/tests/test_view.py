#
# test_view.py
#
import unittest
from unittest.mock import patch
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

    # def test_main(self):
    #     view.main()
    #     view.mainloop.__glo
    #     view.main.

    def test_make_main_frame(self):
        isinstance(view.main_frm, type(ttk.Frame()))
        mf_info = view.main_frm.info()

        self.assertEqual(mf_info['expand'], '0')
        self.assertEqual(mf_info['anchor'], 'center')
        self.assertEqual(mf_info['fill'], 'none')
        self.assertEqual(mf_info['side'], 'top')
        
    def test_make_control_frame(self):
        isinstance(view.control_frame, type(ttk.Frame()))
        cf_info = view.control_frame.info()
        self.assertEqual(cf_info['expand'], '1')
        self.assertEqual(cf_info['anchor'], 'w')
        self.assertEqual(cf_info['fill'], 'both')
        self.assertEqual(cf_info['side'], 'left')

    def test_make_graph_frame(self):
        isinstance(view.graph_frame, type(ttk.Frame()))
        gf_info = view.graph_frame.info()

        self.assertEqual(gf_info['expand'], '1')
        self.assertEqual(gf_info['anchor'], 'e')
        self.assertEqual(gf_info['fill'], 'both')
        self.assertEqual(gf_info['side'], 'right')

    def test_initiate_graph(self):
        # self.assertTrue(plt.fignum_exists(my_dummy_plot))

        # test to make sure figure plots [0,0,0]
        pass

    def test_make_graph(self):
        graph_info = view.graph_frame.winfo_children()[0].info()

        self.assertEqual(graph_info['expand'], '1')
        self.assertEqual(graph_info['anchor'], 'center')
        self.assertEqual(graph_info['fill'], 'both')
        self.assertEqual(graph_info['side'], 'top')

    def test_center_window(self):
        view.geometry("800x600")
        view._center_window()
        dimensions = '800x600+320+150'
        self.assertEqual(view.geometry(), dimensions)

    def test_make_slider(self):
        view._make_slider()
        self.assertEqual(view.slider.get(), 0)
        self.assertEqual(view.slider['orient'], 'horizontal')
        self.assertEqual(view.slider['from'], 0.0)
        self.assertEqual(view.slider['to'], 100.0)

    def test_make_Cloud_Cover_Label(self):
        view._make_Cloud_Cover_label()
        self.assertEqual(view._Cloud_Cover_Label['text'], "Cloud Cover as %")

    def test_make_calculate_button(self):
        view._make_calculate_button
        view.btn.invoke()
        self.assertEqual(view.btn['text'], "Calculate model")

if __name__ == "__main__":
    unittest.main()
