import numpy as np

A = np.array([[1, 1], [2, -1], [1, 3], [3, 1]])
B = np.array([[3.01], [0.003], [7.03], [4.97]])
X = np.linalg.solve(A, B)
