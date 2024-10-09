import numpy as np
import matplotlib.pyplot as plt

# Class for Newton Divided Differences Interpolation
class NewtonDividedDifferences:
    def __init__(self, x_values, y_values):
        self.x_values = np.array(x_values)
        self.y_values = np.array(y_values)
        self.coefficients = self.divided_differences()

    def divided_differences(self):
        n = len(self.x_values)
        table = np.zeros((n, n))
        table[:, 0] = self.y_values
        for j in range(1, n):
            for i in range(n - j):
                table[i, j] = (table[i + 1, j - 1] - table[i, j - 1]) / (self.x_values[i + j] - self.x_values[i])
        return table[0, :]

    def interpolate(self, x):
        n = len(self.coefficients)
        y_interpolated = self.coefficients[0]
        for i in range(1, n):
            term = self.coefficients[i]
            for j in range(i):
                term *= (x - self.x_values[j])
            y_interpolated += term
        return y_interpolated

    def plot(self):
        x_range = np.linspace(min(self.x_values), max(self.x_values), 1000)
        y_range = [self.interpolate(x) for x in x_range]
        plt.plot(x_range, y_range, label='Newton Polynomial')
        plt.scatter(self.x_values, self.y_values, color='red', zorder=5, label='Data Points')
        plt.title("Newton Divided Differences Interpolation")
        plt.legend()
        plt.grid(True)
        plt.show()

    def print_interpolation(self, x):
        y_interp = self.interpolate(x)
        print(f"Interpolated value at x = {x} using Newton method is: {y_interp:.6f}")