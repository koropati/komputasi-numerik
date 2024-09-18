import sys
import os

# Menambahkan path ke folder src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import NewtonRaphson

# Contoh penggunaan:
# Fungsi yang ingin dicari akarnya: f(x) = x^3 - x - 2
def f(x):
    return x**3 - x - 2

# Turunan dari fungsi tersebut: f'(x) = 3x^2 - 1
def f_prime(x):
    return 3*x**2 - 1

# Membuat objek NewtonRaphson dengan fungsi dan turunannya
newton_raphson = NewtonRaphson(f, f_prime, tolerance=1e-6)

# Cari akar dengan perkiraan awal x0 = 2
x0 = 3
try:
    root, iterations = newton_raphson.find_root(x0)
    print(f"Akar ditemukan: {root} setelah {iterations} iterasi.")
    print(f"\n")
    newton_raphson.print_iteration_table()
    newton_raphson.plot()
except ValueError as e:
    print(e)