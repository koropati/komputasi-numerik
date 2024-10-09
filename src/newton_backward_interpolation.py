import numpy as np

class NewtonBackwardInterpolation:
    def __init__(self, x_values, y_values):
        """
        Inisialisasi kelas dengan titik-titik data x dan y.
        x_values: daftar nilai x
        y_values: daftar nilai y (f(x))
        """
        self.x_values = np.array(x_values, dtype=float)
        self.y_values = np.array(y_values, dtype=float)
        self.n = len(x_values)

        if len(self.x_values) != len(self.y_values):
            raise ValueError("Panjang x_values dan y_values harus sama")

        self.backward_diff_table = self.calculate_backward_diff_table()

    def calculate_backward_diff_table(self):
        """
        Membuat tabel selisih mundur (backward difference table).
        """
        n = self.n
        diff_table = np.zeros((n, n))
        diff_table[:, 0] = self.y_values

        for j in range(1, n):
            for i in range(n - 1, j - 1, -1):
                diff_table[i][j] = diff_table[i][j - 1] - diff_table[i - 1][j - 1]

        return diff_table

    def u_calculate(self, u, n):
        """
        Menghitung nilai u*(u+1)*(u+2)*... untuk interpolasi mundur.
        """
        result = u
        for i in range(1, n):
            result *= (u + i)
        return result

    def factorial(self, n):
        """
        Menghitung nilai faktorial dari n.
        """
        return 1 if n == 0 else n * self.factorial(n - 1)

    def interpolate(self, x):
        """
        Menginterpolasi nilai pada titik x menggunakan Interpolasi Newton Mundur.
        """
        h = self.x_values[1] - self.x_values[0]
        u = (x - self.x_values[-1]) / h

        interpolated_value = self.y_values[-1]
        for i in range(1, self.n):
            interpolated_value += (self.u_calculate(u, i) * self.backward_diff_table[-1][i]) / self.factorial(i)

        return interpolated_value

    def print_backward_diff_table(self):
        """
        Menampilkan tabel selisih mundur dengan header dinamis.
        """
        print("Tabel Selisih Mundur:")

        # Print header tabel
        header = ["x", "f(x)"]
        for i in range(1, self.n):
            header.append(f"Δ^{i}y")
        print("\t".join(f"{h:<10}" for h in header))

        # Print isi tabel dengan nilai selisih mundur
        for i in range(self.n):
            row = [f"{self.x_values[i]:<10.4f}", f"{self.backward_diff_table[i][0]:<10.4f}"]
            for j in range(1, i + 1):
                row.append(f"{self.backward_diff_table[i][j]:<10.4f}")
            print("\t".join(row))