import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src import NewtonDividedDifferences

# Example data
x_values = [8, 10, 12, 14]
y_values = [15, 20, 25, 30]

newton_interpolator = NewtonDividedDifferences(x_values, y_values)

newton_interpolator.print_interpolation(11)

# Display Newton interpolation results
print("Newton Divided Differences Interpolation Results:")
newton_interpolator.plot()