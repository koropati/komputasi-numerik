# komputasi-numerik
Beberapa Kode Penyelesaian pada mata kuliah Komputasi Numerik dengan Bahasa Python. Pascasarjana Ilmu Komputer Universitas Pendidikan Ganesha 

# Instalasi Program

* Clone Repository ini dengan cara 
```
git clone https://github.com/koropati/komputasi-numerik.git
```
atau dengan cara clone melalui SSH
```
git clone git@github.com:koropati/komputasi-numerik.git
```

* Setelah selesai melakukan clone repository, masuk ke folder project
```
cd komputasi-numerik
```

* Jika Belum memiliki Virtual Environment Project Python silahkan buat dengan cara:
```
python -m venv {nama_environtment}
```
contoh misal nama env nya adalah ```.venv```:
```
python -m venv .venv
```

* Jika pip belum terupdate. silahkan update pip dengan cara:
```
python -m pip install --upgrade pip
```

* Aktifkan Virtual Environment yang telah dibuat:
```
.venv\Scripts\activate
```

* Install semua package yang dibutuhkan dengan cara:
```
pip install -r requirements.txt
```

# Menjalankan Example Program

* Menjalankan contoh perhitungan metode secant
```
python example\secant.py
```

* Menjalankan contoh perhitungan metode cholesky
```
python example\cholesky.py
```

* Menjalankan contoh perhitungan metode newton raphson.py
```
python example\newton_raphson.py
```

#