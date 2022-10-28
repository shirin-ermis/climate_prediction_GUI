import climpred as cp
import numpy as np

# Stefan-Boltzmann constant (W/m^(-2)K^(-4))
sigma = 5.67e-8


def product(i, j, epsilons):
    prod = 1
    for k in range(i + 1, j):
        prod *= 1 - epsilons[k]

    return prod


def create_matrix(N, epsilons):
    diag_elem = np.zeros((N + 1, N + 1))
    matrix = diag_elem.copy()
    epsilons = np.insert(epsilons, 0, 1)
    for i in range(N + 1):
        if i == 0:
            diag_elem[i, i] = -epsilons[0]
        else:
            diag_elem[i, i] = -2 * epsilons[i]

        for j in range(i + 1, N + 1):
            matrix[i, j] = epsilons[i] * product(i, j, epsilons) * epsilons[j]
    return matrix + matrix.transpose() + diag_elem


def create_RHS_vector(N, H, S_0, the_albedo):
    vector = np.zeros(N + 1)
    vector[0] = H[0] - S_0 * (1 - the_albedo) / 4
    for i in range(1, N):
        vector[i] = H[i] - H[i - 1]
    vector[N] = -H[N - 1]
    vector = vector / sigma
    return vector


def calculate_temperature_matrix_general(
    layers: int = 2,
    cloud_cover: float = 0.35,
    epsilons: np.ndarray = np.array([0.5, 0.5]),
    H: np.ndarray = np.array([50., 50.]),
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

    the_albedo = cp.get_albedo(cloud_cover)

    epsilon_matrix = create_matrix(layers, epsilons)

    rhs_vector = create_RHS_vector(layers, H, S_0, the_albedo)

    epsilon_inverse_matrix = np.linalg.inv(epsilon_matrix)

    temperature_matrix = (np.dot(epsilon_inverse_matrix, rhs_vector))**0.25
    # converted return to celsius
    return np.around(temperature_matrix - 273.15, 2)
