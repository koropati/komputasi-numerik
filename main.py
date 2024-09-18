
from src.secant import Secant


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

# Menampilkan tabel iterasi
secant_solver.print_iteration_table()

# Menampilkan grafik
secant_solver.plot()