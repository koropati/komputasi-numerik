import numpy as np
import matplotlib.pyplot as plt

# Class for Lagrange Interpolation
class LagrangeInterpolation:
    def __init__(self, x_values, y_values):
        self.x_values = np.array(x_values)
        self.y_values = np.array(y_values)
    
    def interpolate(self, x):
        n = len(self.x_values)
        L = np.zeros(n)
        y_interpolated = 0
        for i in range(n):
            L[i] = np.prod([(x - self.x_values[j]) / (self.x_values[i] - self.x_values[j]) 
                            for j in range(n) if j != i])
            y_interpolated += L[i] * self.y_values[i]
        return y_interpolated

    def plot(self):
        x_range = np.linspace(min(self.x_values), max(self.x_values), 1000)
        y_range = [self.interpolate(x) for x in x_range]
        plt.plot(x_range, y_range, label='Lagrange Polynomial')
        plt.scatter(self.x_values, self.y_values, color='red', zorder=5, label='Data Points')
        plt.title("Lagrange Interpolation")
        plt.legend()
        plt.grid(True)
        plt.show()

    def print_interpolation(self, x):
        y_interp = self.interpolate(x)
        print(f"Interpolated value at x = {x} using Lagrange method is: {y_interp:.6f}")