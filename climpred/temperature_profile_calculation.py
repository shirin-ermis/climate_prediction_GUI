import numpy as np

# Planetary albedo (dimensionless)
albedo = 0.3

# Emissitivity/absorptivity for layer 1 (dimensionless)
epsilon_1 = 0.5

# Emissitivity/absorptivity for layer 2 (dimensionless)
epsilon_2 = 0.5

# Convective flux frum surface to layer 1 (W/m^(-2))
H_S = 50

# Convective flux from layer 1 to layer 2 (W/m^(-2))
H_L = 50

# Solar constant (W/m^(-2))
S_0 = 1367

# Stefan-Boltzmann constant (W/m^(-2)K^(-4))
sigma = 5.67e-8

epsilon_matrix = np.array([[-1, epsilon_1, (1 - epsilon_1) * epsilon_2],
                           [epsilon_1, -2 * epsilon_1, epsilon_1 * epsilon_2],
                           [(1 - epsilon_1) * epsilon_2, epsilon_1 * epsilon_2, -2 * epsilon_2]])


rhs_vector = (1 / sigma) * np.array([(H_S - (S_0 / 4) * (1 - albedo)), 
                               H_L - H_S, 
                               (-1 * H_L)])

epsilon_inverse_matrix = np.linalg.inv(epsilon_matrix)  

temperature_matrix = (np.dot(epsilon_inverse_matrix, rhs_vector))**0.25

# Surface temperature (K)
T_s = temperature_matrix[0]

# Layer 1 temperature (K)
T_1 = temperature_matrix[1]

# Layer 2 temperature (K)
T_2 = temperature_matrix[2]








