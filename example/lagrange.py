import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src import LagrangeInterpolation

# Example data
x_values = [1, 2, 3, 4]
y_values = [2, 3, 5, 4]

# Create instances of both classes and plot
lagrange_interpolator = LagrangeInterpolation(x_values, y_values)
lagrange_interpolator.print_interpolation(2.5)
# Display Lagrange interpolation results
print("Lagrange Interpolation Results:")
lagrange_interpolator.plot()