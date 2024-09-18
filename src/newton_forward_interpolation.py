import numpy as np
import matplotlib.pyplot as plt

class NewtonForwardInterpolation:
    def __init__(self, x_points, y_points):
        """
        Inisialisasi kelas dengan titik-titik data x dan y.
        
        Parameters:
        - x_points: Daftar nilai x dari data yang diberikan.
        - y_points: Daftar nilai y dari data yang diberikan.
        """
        self.x_points = np.array(x_points, dtype=float)
        self.y_points = np.array(y_points, dtype=float)
        self.n = len(x_points)
        self.difference_table = np.zeros((self.n, self.n))
        self.difference_table[:, 0] = self.y_points  # Kolom pertama diisi dengan nilai y
        
        self.create_difference_table()

    def create_difference_table(self):
        """
        Membuat tabel selisih maju berdasarkan titik-titik data.
        """
        for i in range(1, self.n):
            for j in range(self.n - i):
                self.difference_table[j, i] = self.difference_table[j + 1, i - 1] - self.difference_table[j, i - 1]

    def newton_forward_formula(self, x_value):
        """
        Menerapkan formula interpolasi Newton maju untuk menghitung nilai pada x_value.
        
        Parameters:
        - x_value: Nilai x yang ingin dihitung
        
        Returns:
        - Nilai interpolasi pada titik x_value
        """
        h = self.x_points[1] - self.x_points[0]
        u = (x_value - self.x_points[0]) / h
        result = self.difference_table[0, 0]
        
        u_product = 1
        for i in range(1, self.n):
            u_product *= (u - (i - 1))
            result += (u_product * self.difference_table[0, i]) / np.math.factorial(i)
        
        return result

    def plot(self, resolution=100):
        """
        Menampilkan grafik interpolasi Newton maju dengan titik data asli.
        
        Parameters:
        - resolution: Jumlah titik untuk grafik interpolasi (default 100)
        """
        # Titik x untuk grafik interpolasi
        x_vals = np.linspace(self.x_points[0], self.x_points[-1], resolution)
        y_vals = [self.newton_forward_formula(x) for x in x_vals]
        
        # Plot data asli
        plt.plot(self.x_points, self.y_points, 'ro', label="Titik Data Asli")
        
        # Plot hasil interpolasi
        plt.plot(x_vals, y_vals, 'b-', label="Interpolasi Newton Maju")
        
        # Label dan judul
        plt.title("Grafik Interpolasi Newton Maju")
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.legend()
        plt.grid(True)
        plt.show()

    def show_table(self):
        """
        Menampilkan tabel selisih maju dalam bentuk teks di console.
        """
        print("Tabel Selisih Maju:")
        print(f"{'':<15}", end="")
        for i in range(self.n):
            print(f"Δ^{i}y".ljust(15), end="")
        print()
        
        for i in range(self.n):
            print(f"x{i:<2}".ljust(15), end="")
            for j in range(self.n - i):
                print(f"{self.difference_table[i, j]:<15.4f}", end="")
            print()