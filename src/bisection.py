import numpy as np
import matplotlib.pyplot as plt

class Bisection:
    def __init__(self, f, a, b, tol=1e-7, max_iter=100):
        """
        Inisialisasi kelas dengan fungsi f dan dua titik awal (a, b).
        f: fungsi yang akar-nya dicari
        a, b: dua titik awal (harus mengapit akar, f(a) * f(b) < 0)
        tol: toleransi konvergensi
        max_iter: jumlah iterasi maksimum
        """
        self.f = f
        self.a = a
        self.b = b
        self.tol = tol
        self.max_iter = max_iter
        self.iterations = []  # Simpan nilai-nilai iterasi untuk visualisasi dan tabel

    def find_root(self):
        """
        Mencari akar dari fungsi menggunakan metode bagi dua.
        Mengembalikan akar yang diperkirakan.
        """
        a, b = self.a, self.b

        if self.f(a) * self.f(b) >= 0:
            raise ValueError("f(a) dan f(b) harus memiliki tanda yang berbeda")

        for i in range(self.max_iter):
            c = (a + b) / 2
            f_a = self.f(a)
            f_b = self.f(b)
            f_c = self.f(c)
            delta = (b - a) / 2
            f_a_f_b = f_a * f_b
            f_b_f_c = f_b * f_c

            # Simpan iterasi untuk tabel dan grafik
            self.iterations.append((a, b, c, f_a, f_b, f_c, delta, f_a_f_b, f_b_f_c))

            # Cek konvergensi
            if abs(f_c) < self.tol or abs(b - a) < self.tol:
                return c

            # Update interval
            if f_a * f_c < 0:
                b = c
            else:
                a = c

        raise ValueError("Metode tidak konvergen dalam jumlah iterasi maksimum")

    def print_iteration_table(self):
        """
        Menampilkan tabel hasil iterasi yang berisi nilai a, b, c, f(a), f(b), f(c), (b-a)/2, f(a) * f(b), f(b) * f(c).
        """
        print(f"{'Iterasi':<10}{'a':<10}{'b':<10}{'c':<10}{'f(a)':<12}{'f(b)':<12}{'f(c)':<12}{'(b-a)/2':<12}{'f(a)*f(b)':<15}{'f(b)*f(c)'}")
        print("-" * 120)
        for i, (a, b, c, f_a, f_b, f_c, delta, f_a_f_b, f_b_f_c) in enumerate(self.iterations, start=1):
            print(f"{i:<10}{a:<10.6f}{b:<10.6f}{c:<10.6f}{f_a:<12.6f}{f_b:<12.6f}{f_c:<12.6f}{delta:<12.6f}{f_a_f_b:<15.6f}{f_b_f_c:<12.6f}")

    def plot(self):
        """
        Menampilkan grafik dari fungsi dan proses iterasi metode bagi dua.
        """
        # Buat titik-titik untuk grafik fungsi
        x_vals = np.linspace(self.a - 1, self.b + 1, 500)
        y_vals = self.f(x_vals)

        # Buat grafik fungsi
        plt.plot(x_vals, y_vals, label="f(x)", color="blue")
        plt.axhline(0, color='black', linewidth=1)

        # Plot iterasi bisection
        iter_a_vals = [a for a, _, _, _, _, _, _, _, _ in self.iterations]
        iter_b_vals = [b for _, b, _, _, _, _, _, _, _ in self.iterations]
        iter_c_vals = [c for _, _, c, _, _, _, _, _, _ in self.iterations]

        # Plot titik a, b, dan c pada setiap iterasi
        plt.plot(iter_a_vals, [self.f(a) for a in iter_a_vals], 'ro-', label="Iterasi a", alpha=0.6)
        plt.plot(iter_b_vals, [self.f(b) for b in iter_b_vals], 'go-', label="Iterasi b", alpha=0.6)
        plt.plot(iter_c_vals, [self.f(c) for c in iter_c_vals], 'bo-', label="Iterasi c", alpha=0.6)

        # Tampilkan titik-titik iterasi
        for i, (c) in enumerate(iter_c_vals):
            plt.text(c, self.f(c), f'Iter {i+1}', fontsize=8, color='purple')

        # Label dan judul
        plt.title("Metode Bagi Dua")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.show()
