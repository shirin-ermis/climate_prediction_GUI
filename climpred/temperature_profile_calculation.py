import numpy as np

albedo = 0.3

epsilon_1 = 0.5
epsilon_2 = 0.5

# Convective flux frum surface to layer 1
H_S = 1

# Convective flux from layer 1 to layer 2
H_L = 1

# Solar constant:
S_0 = 1367
sigma = 5.67e-8
T_s = 1
T_1 = 1
T_2 = 1

epsilon_matrix = np.array([[-1, epsilon_1, (1 - epsilon_1) * epsilon_2],
                           [epsilon_1, -2 * epsilon_1, epsilon_1 * epsilon_2],
                           [(1 - epsilon_1) * epsilon_2, epsilon_1 * epsilon_2, -2 * epsilon_2]])

temperature_matrix = np.array([(T_s)**4, (T_1)**4, (T_2)**4])

rhs_vector = (1 / sigma) * np.array([(H_S - (S_0 / 4) * (1 - albedo)), 
                               H_L - H_S, 
                               (-1 * H_L)])

epsilon_inverse_matrix = np.linalg.inv(epsilon_matrix)  
temperature_matrix = np.dot(epsilon_inverse_matrix, rhs_vector)
print(temperature_matrix)
solution_matrix = (temperature_matrix)**0.25
print(solution_matrix)