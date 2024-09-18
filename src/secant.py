class Secant:
    def __init__(self, f, x0, x1, tol=1e-7, max_iter=100):
        """
        Inisialisasi kelas dengan fungsi f dan dua titik awal.
        f: fungsi yang akar-nya dicari
        x0, x1: dua titik awal
        tol: toleransi konvergensi
        max_iter: jumlah iterasi maksimum
        """
        self.f = f
        self.x0 = x0
        self.x1 = x1
        self.tol = tol
        self.max_iter = max_iter

    def find_root(self):
        """
        Mencari akar dari fungsi menggunakan metode secant.
        Mengembalikan akar yang diperkirakan.
        """
        x0, x1 = self.x0, self.x1
        
        for _ in range(self.max_iter):
            f_x0 = self.f(x0)
            f_x1 = self.f(x1)
            
            if abs(f_x1 - f_x0) < 1e-12:  # untuk menghindari pembagian dengan nol
                raise ValueError("Perbedaan nilai fungsi terlalu kecil; metode mungkin tidak konvergen.")
            
            # Hitung akar baru menggunakan formula secant
            x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
            
            # Cek konvergensi
            if abs(self.f(x2)) < self.tol:
                return x2
            
            # Update titik
            x0, x1 = x1, x2
        
        raise ValueError("Metode tidak konvergen dalam jumlah iterasi maksimum")