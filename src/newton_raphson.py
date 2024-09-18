import numpy as np
import matplotlib.pyplot as plt

class NewtonRaphson:
    def __init__(self, func, func_derivative, tolerance=1e-6, max_iter=100):
        """
        Inisialisasi metode Newton-Raphson.
        
        Parameters:
        - func: Fungsi yang akan dicari akarnya.
        - func_derivative: Turunan dari fungsi tersebut.
        - tolerance: Nilai toleransi untuk menghentikan iterasi (default 1e-6).
        - max_iter: Maksimal jumlah iterasi (default 100).
        """
        self.func = func
        self.func_derivative = func_derivative
        self.tolerance = tolerance
        self.max_iter = max_iter
        self.iterations = []  # Simpan nilai-nilai tiap iterasi untuk grafik dan tabel

    def find_root(self, x0):
        """
        Mencari akar dari fungsi menggunakan metode Newton-Raphson.
        
        Parameters:
        - x0: Perkiraan awal untuk akar.
        
        Returns:
        - Akar dari fungsi, jika ditemukan dalam batas iterasi dan toleransi.
        - Jumlah iterasi yang diperlukan.
        """
        x = x0
        for i in range(self.max_iter):
            fx = self.func(x)
            fpx = self.func_derivative(x)
            
            if fpx == 0:
                raise ValueError("Turunan f'(x) bernilai nol, metode gagal.")
            
            # Hitung nilai x baru
            x_new = x - fx / fpx
            
            # Simpan hasil iterasi untuk tabel dan grafik
            self.iterations.append((i + 1, x, fx, abs(x_new - x)))

            # Periksa apakah sudah mencapai toleransi yang diinginkan
            if abs(x_new - x) < self.tolerance:
                return x_new, i + 1
            
            x = x_new
        
        # Jika iterasi maksimal tercapai tanpa konvergensi
        raise ValueError("Akar tidak ditemukan dalam batas iterasi yang ditentukan.")

    def print_iteration_table(self):
        """
        Menampilkan tabel hasil iterasi yang berisi nilai x, f(x), dan perubahan x.
        """
        print(f"{'Iterasi':<10}{'x':<20}{'f(x)':<20}{'Δx'}")
        print("-" * 60)
        for iteration, x, fx, delta_x in self.iterations:
            # Tampilkan dengan 4 angka di belakang koma
            print(f"{iteration:<10}{x:<20.4f}{fx:<20.4f}{delta_x:.4f}")

    def plot(self):
        """
        Menampilkan grafik dari fungsi dan proses iterasi metode Newton-Raphson.
        """
        # Buat titik-titik untuk grafik fungsi
        x_vals = np.linspace(min([x for _, x, _, _ in self.iterations])-1, max([x for _, x, _, _ in self.iterations])+1, 500)
        y_vals = self.func(x_vals)

        # Buat grafik fungsi
        plt.plot(x_vals, y_vals, label="f(x)", color="blue")
        plt.axhline(0, color='black', linewidth=1)

        # Plot iterasi Newton-Raphson
        iter_x_vals = [x for _, x, _, _ in self.iterations]
        iter_y_vals = [self.func(x) for x in iter_x_vals]
        plt.plot(iter_x_vals, iter_y_vals, 'ro-', label="Iterasi Newton-Raphson")

        # Tampilkan titik-titik iterasi
        for i, (iteration, x, fx, delta_x) in enumerate(self.iterations):
            plt.text(x, fx, f'Iter {iteration}', fontsize=9, color='red')

        # Label dan judul
        plt.title("Metode Newton-Raphson")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.show()
