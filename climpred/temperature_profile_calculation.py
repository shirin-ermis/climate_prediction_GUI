import climpred as cp
import numpy as np

# Stefan-Boltzmann constant (W/m^(-2)K^(-4))
sigma = 5.67e-8


def calculate_temperature_matrix(
    cloud_cover: float = 0.35,
    epsilon_1: float = 0.5,
    epsilon_2: float = 0.5,
    H_S: float = 50.,
    H_L: float = 50.,
    S_0: float = 1367.
):
    '''
    Takes atmospheric parameters and returns a three-point temperature profile.

    Parameters
    ----------
    cloud_cover: float
    Fraction of globe covered by clouds (dimensionless)

    epsilon_1: float
    Emissitivity/absorptivity for layer 1 (dimensionless)

    epsilon_2: float
    Emissitivity/absorptivity for layer 2 (dimensionless)

    H_S: float
    Convective flux frum surface to layer 1 (W/m^(-2))

    H_L: float
    Convective flux frum layer 1 to layer 2 (W/m^(-2))

    S_0: float
    Solar constant (W/m^(-2))

    Returns
    ----------
    temperature_matrix: np.ndarray
    An array of three points for the temperature profile: T_surface,
    T_level1, T_level2 (K)

    '''

    albedo = cp.get_albedo(cloud_cover)

    epsilon_matrix = np.array([[-1, epsilon_1, (1 - epsilon_1) * epsilon_2],
                               [epsilon_1, -2 * epsilon_1,
                               epsilon_1 * epsilon_2],
                               [(1 - epsilon_1) * epsilon_2,
                               epsilon_1 * epsilon_2, -2 * epsilon_2]])

    rhs_vector = (1 / sigma) * np.array([(H_S - (S_0 / 4) * (1 - albedo)),
                                        H_L - H_S,
                                        (-1 * H_L)])

    epsilon_inverse_matrix = np.linalg.inv(epsilon_matrix)

    temperature_matrix = (np.dot(epsilon_inverse_matrix, rhs_vector))**0.25
    # converted return to celsius
    return np.around(temperature_matrix - 273.15, 2)
