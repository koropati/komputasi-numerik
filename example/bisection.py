import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import Bisection

if __name__ == "__main__":
    def f(x):
        return x**2 - 2

    bisection = Bisection(f, 1, 2, tol=0.1)
    try:
        root = bisection.find_root()
        print(f"Akar yang ditemukan: {root:.6f}")
    except ValueError as e:
        print(e)

    bisection.print_iteration_table()
    bisection.plot()