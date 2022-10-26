import unittest
import climpred as cp

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


if __name__ == '__main__':
    unittest.main()
