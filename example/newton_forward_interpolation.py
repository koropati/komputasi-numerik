import sys
import os

# Menambahkan path ke folder src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import NewtonForwardInterpolation

# Contoh penggunaan
x_points = [0, 1, 2, 3, 4]
y_points = [1, 2, 4, 8, 16]

# Membuat objek dari kelas
interpolation = NewtonForwardInterpolation(x_points, y_points)

# Menampilkan tabel selisih
interpolation.show_table()

# Menampilkan grafik interpolasi
interpolation.plot()