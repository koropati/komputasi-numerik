import sys
import os

# Menambahkan path ke folder src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from src import Cholesky

# Contoh penggunaan
A = np.array([[4, 2], [2, 3]], dtype=float)
b = np.array([10, 11], dtype=float)

# Inisialisasi objek Cholesky dengan matriks A
cholesky_solver = Cholesky(A)

# Menyelesaikan sistem persamaan Ax = b
x = cholesky_solver.solve(b)
print("Solusi x:", x)

# Menampilkan grafik
cholesky_solver.plot_matrix()