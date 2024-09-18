import numpy as np

class Cholesky:
    def __init__(self, A):
        """
        Inisialisasi kelas dengan matriks A.
        A: matriks simetris positif-definit
        """
        self.A = A
        self.L = self.cholesky_decomposition()

    def cholesky_decomposition(self):
        """
        Melakukan dekomposisi Cholesky pada matriks A
        Mengembalikan matriks segitiga bawah L
        """
        A = self.A
        n = A.shape[0]
        L = np.zeros_like(A)
        
        for i in range(n):
            for j in range(i + 1):
                if i == j:
                    # Elemen diagonal
                    L[i, j] = np.sqrt(A[i, i] - np.sum(L[i, :j] ** 2))
                else:
                    # Elemen non-diagonal
                    L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]
                    
        return L

    def solve(self, b):
        """
        Menyelesaikan sistem persamaan Ax = b menggunakan dekomposisi Cholesky
        b: vektor solusi
        Mengembalikan vektor x
        """
        L = self.L
        
        # Langkah 1: Selesaikan Ly = b
        y = np.linalg.solve(L, b)
        
        # Langkah 2: Selesaikan L^T x = y
        x = np.linalg.solve(L.T, y)
        
        return x