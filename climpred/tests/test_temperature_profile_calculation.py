import unittest
import climpred as cp
import numpy.testing as npt
import numpy as np

# Stefan-Boltzmann constant (W/m^(-2)K^(-4))
sigma = 5.67e-8


class TestTemperatureVector(unittest.TestCase):

    def test_vector_length(self):
        self.assertEqual(len(cp.calculate_temperature_matrix()), 3), \
            "Array length should be 3"

    def test_temp_range(self):
        for temp in range(3):
            assert (-1000 <= cp.calculate_temperature_matrix()[temp] <= 100), \
                "Temperature out of range"

    def test_matrix_calculation(self):
        sigma = 5.67e-8  # Stefan-Boltzmann constant (W/m^(-2)K^(-4))
        solar = 1000
        e1 = 1
        e2 = 0.1
        # coefficient matrix  for parameters below
        a = np.array([[-1, e1, (1-e1)*e2],
                      [e1, -2*e1, e1*e2],
                      [(1-e1)*e2, e1*e2, -2*e2]])
        b = np.array([1, 0, 0]) * (-0.94*solar)/(4*sigma)  # rhs
        npt.assert_array_almost_equal(
            cp.calculate_temperature_matrix(cloud_cover=0,
                                            epsilon_1=e1,
                                            epsilon_2=e2,
                                            H_S=0,
                                            H_L=0,
                                            S_0=solar),
            np.around((np.linalg.solve(a, b)**0.25)-273.15, 2))


if __name__ == '__main__':
    unittest.main()
