import sys
import os

# Menambahkan path ke folder src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import Secant

# Contoh penggunaan
def func(x):
    return x**2 - 4  # Misalkan kita ingin menemukan akar dari f(x) = x^2 - 4

# Contoh fungsi dan penggunaan metode secant
def func2(x):
    return x**3 - 6*x**2 + 11*x - 6

x0 = 1.0
x1 = 3.0

try:
    # Inisialisasi objek Secant dengan fungsi dan titik awal
    secant_solver = Secant(func, x0, x1, tol=1e-7, max_iter=100)

    # Menyelesaikan sistem untuk menemukan akar
    akar = secant_solver.find_root()
    print("Akar yang diperkirakan:", akar)
    print(f"\n")
    # Tampilkan Iterasi
    secant_solver.print_iteration_table()
    # Tampilkan grafik
    secant_solver.plot()
    
except Exception as e:
    print(f"Message: {e}")