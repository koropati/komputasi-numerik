import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import Bisection

if __name__ == "__main__":
    def f(x):
        return x**3 - 5*x + 1

    bisection = Bisection(f, 0, 2, tol=0.00001)
    try:
        root = bisection.find_root()
        print(f"Akar yang ditemukan: {root:.6f}")
    except ValueError as e:
        print(e)

    bisection.print_iteration_table()
    bisection.plot()