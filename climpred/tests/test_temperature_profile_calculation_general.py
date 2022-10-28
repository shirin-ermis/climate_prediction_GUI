import unittest
import climpred as cp
import numpy.testing as npt
import numpy as np

# Stefan-Boltzmann constant (W/m^(-2)K^(-4))
sigma = 5.67e-8


class TestTemperatureVector(unittest.TestCase):
    # Simple case

    def test_vector_length(self):
        layers = 2
        cloud_cover = 0.35
        epsilons = np.array([0.5, 0.5])
        H = np.array([50., 50.])
        S_0 = 1367.
        Temp_output = cp.calculate_temperature_matrix_general(layers,
                                                              cloud_cover,
                                                              epsilons,
                                                              H,
                                                              S_0
                                                              )
        self.assertEqual(len(Temp_output), layers + 1)

    def test_matrix_calculation(self):
        layers = 2
        epsilons = np.array([0.5, 0.5])
        # coefficient matrix  for parameters below
        ans = np.array([[-1, 0.5, 0.25],
                        [0.5, -1, 0.25],
                        [0.25, 0.25, -1]])
        npt.assert_array_almost_equal(
            cp.create_matrix(layers, epsilons),
            ans)

        layers = 3
        epsilons = np.zeros(layers)
        ans = np.zeros((layers + 1, layers + 1))
        ans[0, 0] = -1
        npt.assert_array_almost_equal(
            cp.create_matrix(layers, epsilons),
            ans)

    def test_create_RHS_vector(self):
        sigma = 5.67e-8
        layers = 2
        cloud_cover = 0.35
        H = np.array([50., 50.])
        S_0 = 1367.
        the_albedo = cp.get_albedo(cloud_cover)
        vector = cp.create_RHS_vector(layers,
                                      H,
                                      S_0,
                                      the_albedo)
        ans = np.array([50 - S_0 * (1 - the_albedo) / 4,
                        0,
                        -50.0])
        ans /= sigma
        npt.assert_array_almost_equal(vector, ans)


if __name__ == '__main__':
    unittest.main()
