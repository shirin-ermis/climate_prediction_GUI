#
# test_controller.py
#
from ctypes.wintypes import HACCEL
import unittest
import climpred as cp

class ControllerTest(unittest.TestCase):
    """
    Tests the :class:`Controller` class.
    """
    global ctrl 
    ctrl = cp.Controller()

    def test_init(self):
        isinstance(ctrl.model, type(cp.Model()))
        isinstance(ctrl.view, type(cp.View(ctrl)))

    def test_on_press_calculate_button(self):
        ctrl._on_press_calculate_button()
        ctrl.view.btn.invoke()

    def test_on_press_advanced_calculate_button(self):
        ctrl._on_press_advanced_calculate_button()
        ctrl.view.advanced_calculate_btn.invoke()

       
if __name__ == "__main__":
    unittest.main()
