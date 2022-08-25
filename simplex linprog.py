from scipy.optimize import linprog
import numpy as np

A_ub = np.array([[7, -23, 5, 9], [-5, 3, 1, 0], [-4, 8, -12, -4], [-3, -2, -9, -10], 
     [-1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
A_eq = np.array([[-16, 28, 5, 8], [0, -5, 3, 2]])
b_ub = np.array([56, 7, -1, -6, 0, 0, 0, 0])
b_eq = np.array([5, 8])
c = np.array([-4, 9, -1, 3])

result = linprog(c=c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, method="simplex")

print(result)