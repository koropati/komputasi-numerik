import sys
import os

# Menambahkan path ke folder src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import NewtonBackwardInterpolation

# Contoh penggunaan
if __name__ == "__main__":
    # Data titik (x, y)
    x_values = [3, 6, 9, 12, 15]
    y_values = [14, 20, 25, 36, 45]
    
    # Interpolasi nilai pada titik x
    x_to_interpolate = 13

    # Inisialisasi objek NewtonBackwardInterpolation
    newton_backward = NewtonBackwardInterpolation(x_values, y_values)

    # Cetak tabel selisih mundur
    newton_backward.print_backward_diff_table()

    
    interpolated_value = newton_backward.interpolate(x_to_interpolate)
    print(f"Nilai interpolasi pada x = {x_to_interpolate}: {interpolated_value:.6f}")
