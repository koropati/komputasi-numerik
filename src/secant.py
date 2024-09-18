import numpy as np
import matplotlib.pyplot as plt

class Secant:
    def __init__(self, f, x0, x1, tol=1e-7, max_iter=100):
        """
        Inisialisasi kelas dengan fungsi f dan dua titik awal.
        f: fungsi yang akar-nya dicari
        x0, x1: dua titik awal
        tol: toleransi konvergensi
        max_iter: jumlah iterasi maksimum
        """
        self.f = f
        self.x0 = x0
        self.x1 = x1
        self.tol = tol
        self.max_iter = max_iter
        self.iterations = []  # Simpan nilai-nilai iterasi untuk visualisasi

    def find_root(self):
        """
        Mencari akar dari fungsi menggunakan metode secant.
        Mengembalikan akar yang diperkirakan.
        """
        x0, x1 = self.x0, self.x1
        self.iterations.append((x0, self.f(x0)))
        self.iterations.append((x1, self.f(x1)))

        for i in range(self.max_iter):
            f_x0 = self.f(x0)
            f_x1 = self.f(x1)
            
            if abs(f_x1 - f_x0) < 1e-12:  # untuk menghindari pembagian dengan nol
                raise ValueError("Perbedaan nilai fungsi terlalu kecil; metode mungkin tidak konvergen.")
            
            # Hitung akar baru menggunakan formula secant
            x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
            
            # Simpan iterasi untuk grafik dan tabel
            self.iterations.append((x2, self.f(x2)))
            
            # Cek konvergensi
            if abs(self.f(x2)) < self.tol:
                return x2
            
            # Update titik
            x0, x1 = x1, x2
        
        raise ValueError("Metode tidak konvergen dalam jumlah iterasi maksimum")

    def plot(self):
        """
        Menampilkan grafik dari fungsi dan proses iterasi metode secant.
        """
        # Buat titik-titik untuk grafik fungsi
        x_vals = np.linspace(self.x0 - 1, self.x1 + 1, 500)
        y_vals = self.f(x_vals)

        # Buat grafik fungsi
        plt.plot(x_vals, y_vals, label="f(x)", color="blue")
        plt.axhline(0, color='black',linewidth=1)

        # Plot iterasi secant
        iter_x_vals = [x for x, _ in self.iterations]
        iter_y_vals = [y for _, y in self.iterations]
        plt.plot(iter_x_vals, iter_y_vals, 'ro-', label="Iterasi Secant")

        # Tampilkan titik-titik iterasi
        for i, (x, y) in enumerate(self.iterations):
            plt.text(x, y, f'Iter {i}', fontsize=9, color='red')

        # Label dan judul
        plt.title("Metode Secant")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.show()

    def print_iteration_table(self):
        """
        Menampilkan tabel hasil iterasi yang berisi nilai x, f(x), dan perubahan x.
        """
        print(f"{'Iterasi':<10}{'x':<20}{'f(x)':<20}{'Δx'}")
        print("-" * 60)
        for i in range(1, len(self.iterations)):
            x0, fx0 = self.iterations[i - 1]
            x1, fx1 = self.iterations[i]
            delta_x = abs(x1 - x0)
            # Format nilai x, f(x), dan delta_x dengan 6 angka di belakang koma
            print(f"{i:<10}{x1:<20.6f}{fx1:<20.6f}{delta_x:.6f}")