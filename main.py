import numpy as np
from src.cholesky import Cholesky
from src.secant import Secant


# Contoh penggunaan
A = np.array([[4, 2], [2, 3]], dtype=float)
b = np.array([10, 11], dtype=float)

# Inisialisasi objek Cholesky dengan matriks A
cholesky_solver = Cholesky(A)

# Menyelesaikan sistem persamaan Ax = b
x = cholesky_solver.solve(b)
print("Solusi x:", x)


# Contoh penggunaan
def func(x):
    return x**2 - 4  # Misalkan kita ingin menemukan akar dari f(x) = x^2 - 4

x0 = 1.0
x1 = 3.0

# Inisialisasi objek Secant dengan fungsi dan titik awal
secant_solver = Secant(func, x0, x1)

# Menyelesaikan sistem untuk menemukan akar
akar = secant_solver.find_root()
print("Akar yang diperkirakan:", akar)