#
# test_controller.py
#
import unittest

from pyparsing import Empty
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
        ctrl.view.btn_calc.invoke()

    def test_on_press_advanced_calculate_button(self):
        # setting inputs for running ctrl._on_press_advanced_calculate_button()
        ctrl.view.advanced_btn.invoke()

        ctrl.view.layers.set(5)
        ctrl.view.advanced_cloud_cover_slider.set(0.5)
        ctrl.view.advanced_epsilon_entry.insert(0, '0.7 0.7 0.7 0.7 0.7')
        ctrl.view.advanced_H_entry.insert(0, '5 5 5 5 5')
        ctrl.view.advanced_solar_constant_slider.set(1000)

        ctrl._on_press_advanced_calculate_button()


if __name__ == "__main__":
    unittest.main()
