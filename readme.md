# 🐍 Python Fundamentals & Data Analytics Ecosystem

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Pandas%20%7C%20NumPy%20%7C%20Seaborn-150458?style=flat-square&logo=pandas&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active%20Learning-2ea44f?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

Repository dokumentasi terstruktur yang mencakup perjalanan pembelajaran bahasa pemrograman Python—mulai dari sintaks fundamental, struktur data, manajemen file, eksplorasi *modules & packages*, pengembangan *mini-projects* CLI, hingga implementasi **Data Analysis & Automated Reporting** menggunakan ekosistem *data science* Python.

---

## 📑 Daftar Isi
- [Struktur Repository](#-struktur-repository)
- [Highlight Projects & Studi Kasus](#-highlight-projects--studi-kasus)
- [Prasyarat & Instalasi](#-prasyarat--instalasi)
- [Cara Menjalankan](#-cara-menjalankan)
- [Catatan](#-catatan)

---

## 📂 Struktur Repository

```text
.
├── 01_dasar_python/       # Konsep fundamental, kontrol alur, struktur data, & File I/O
├── 02_modules_python/     # Modularisasi, custom package, standard library, & third-party packages
├── 03_mini_project/       # Implementasi aplikasi CLI dalam versi basic & modular
├── 04_data_analyst/       # Modul Data Analysis (NumPy, Pandas, Cleaning, EDA, & Reporting)
├── 05_studi_kasus_DA/     # Studi kasus analisis bisnis kedai kopi end-to-end
├── constraints.txt        # Daftar dependensi package eksternal
└── README.md              # Dokumentasi repository
```

### 1. `01_dasar_python/`
Fokus pada penguasaan logika pemrograman dasar dan fitur inti Python tanpa dependensi eksternal:
- **Sintaks & Tipe Data:** Deklarasi variabel, *input/output*, manipulasi *string* (`dasar_variabel.py`, `input_manipulasi.py`).
- **Struktur Data:** Implementasi dan operasi pada `list`, `dictionary`, dan `set` (`list_dictionary_set.py`).
- **Kontrol Alur & Fungsi:** Operator logika/aritmatika, percabangan, perulangan (`operator_percabangan_perulangan.py`), pembuatan fungsi, serta penanganan *error* menggunakan `try-except` (`function_try_except.py`).
- **File I/O:** Operasi baca dan tulis file eksternal berbasis teks (`file.py`, `siswa.txt`, `bank_soal.txt`).

### 2. `02_modules_python/`
Fokus pada arsitektur kode yang bersih, penggunaan kembali kode (*reusability*), serta eksplorasi ekosistem Python:
- **Modularisasi & Custom Package:** Pembuatan modul lokal (`matematika.py`) dan *package* terstruktur (`matematika_package/` yang berisi modul `dasar.py` dan `geometry.py`).
- **Python Standard Library:** Eksplorasi modul bawaan seperti `os`, `math`, `random`, `datetime`, dan pengolahan data `json`.
- **Third-Party Packages:** Implementasi pustaka eksternal menggunakan `requests` (HTTP request), `colorama` (styling terminal), `Pillow` (manipulasi gambar), dan `qrcode` (generator QR Code).
- **Environment & Package Management:** Dokumentasi perintah manajemen `pip`, PyPI, dan *virtual environment* (`perintah_dasar_pip_PyPI.txt`, `perintah_environment.txt`).

### 3. `03_mini_project/`
Implementasi proyek-proyek berbasis CLI yang disusun dalam dua pendekatan untuk membandingkan penulisan kode prosedural dalam satu file (`basic/`) dengan arsitektur kode yang terpisah berdasarkan fungsinya (`modular/`):
- **`ujian_sekolah/`** — Simulasi ujian pilihan ganda interaktif dari file bank soal eksternal.
- **`kalkulator/`** — Aplikasi kalkulator aritmatika dasar berbasis terminal.
- **`tebak_angka/`** — Permainan interaktif menebak angka acak dengan sistem petunjuk.

### 4. `04_data_analyst/`
Eksplorasi pengolahan data terstruktur, pembersihan data kotor (*data wrangling*), visualisasi statistik, hingga otomatisasi ekspor laporan multi-sheet:
- **Dataset Generator (`data/`):** Skrip sintetis (`generate_data.py`) yang menghasilkan dataset transaksi ritel (`sales.csv`, `transaksi.csv`, `pelanggan.csv`) dengan skenario anomali nyata (*missing values*, duplikat, inkonsistensi format teks/tanggal).
- **Interactive Notebooks:**
  - `numpy.ipynb` — Komputasi numerik berbasis array dan *vectorization*.
  - `pandas.ipynb` & `pandas_cleaning.ipynb` — Manipulasi `DataFrame`, *filtering*, *merging*, dan standardisasi data kotor.
  - `eda_vis.ipynb` — *Exploratory Data Analysis* (EDA) serta visualisasi tren dan perbandingan kategori menggunakan `matplotlib` dan `seaborn`.
  - `project.ipynb` — Pipeline analisis penjualan ritel terintegrasi.
- **Automated Reports (`reports/`):** Output grafik resolusi tinggi (`grafik_produk.png`, `grafik_tren.png`, `kategori.png`, `metode_pembayaran.png`, `omzet_per_kota.png`, `omzet_dibatalkan_per_kota.png`) dan laporan Excel terformat (`laporan_akhir_2026.xlsx`, `laporan_dibatalkan_2026.xlsx`).

### 5. `05_studi_kasus_DA/`
Studi kasus analisis operasional dan performa penjualan bisnis kedai kopi secara mandiri (*end-to-end*):
- **Dataset (`data/`):** Data relasional antara transaksi pesanan (`pesanan_kopi.csv`) dan katalog harga/modal (`menu_kopi.csv`) yang di-generate melalui `generate_data.ipynb`.
- **Analisis Bisnis (`main.ipynb` & `readme.md`):** Pembersihan data, relasi antar-tabel (*left join*), perhitungan margin profit per menu, evaluasi performa cabang dan *channel* pemesanan (`GoFood`, `Dine-In`, dll.), serta identifikasi jam sibuk (*peak hours*) kedai.

---

## 🚀 Highlight Projects & Studi Kasus

| Project / Studi Kasus | Deskripsi Singkat | Konsep & Tools Utama | Status |
| :--- | :--- | :--- | :--- |
| **`Retail Sales Pipeline`** (`04_data_analyst`) | Pembersihan data transaksi kotor, analisis *opportunity loss* pesanan batal, performa metode pembayaran, dan ekspor laporan otomatis ke Excel. | `Pandas`, `NumPy`, `Seaborn`, `Matplotlib`, `OpenPyXL` | Selesai |
| **`Coffee Shop Analytics`** (`05_studi_kasus_DA`) | Studi kasus analisis profitabilitas menu kopi, performa cabang, dominasi *channel* order, dan pola jam operasional tersibuk (*peak hours*). | Data Cleaning, Relational Merge, Time-Series Hour Extraction, EDA | Selesai |
| **`ujian_sekolah`** (`03_mini_project`) | Simulasi ujian pilihan ganda yang memuat soal dari `bank_soal.txt`, mengacak urutan pertanyaan dan opsi jawaban, serta menghitung skor akhir. | File I/O, `random`, `list`, `dictionary`, string parsing | `basic` (Selesai) · `modular` (In Progress) |
| **`kalkulator`** (`03_mini_project`) | Aplikasi kalkulator aritmatika interaktif berbasis CLI. | Fungsi, percabangan, validasi input | `basic` (Selesai) · `modular` (In Progress) |
| **`tebak_angka`** (`03_mini_project`) | Permainan tebak angka acak dengan sistem petunjuk tinggi/rendah dan batas percobaan. | Perulangan `while`, modul `random`, kontrol alur | `basic` (Selesai) · `modular` (In Progress) |

---

## ⚙️ Prasyarat & Instalasi

Pastikan **Python 3.12+** sudah terpasang di sistem Anda.

1. **Clone repository ini:**
   ```bash
   git clone https://github.com/SatriaFarel/belajar_python.git
   cd belajar_python
   ```

2. **Buat dan aktifkan *virtual environment* (disarankan):**
   ```bash
   # Linux / macOS
   python3 -m venv .venv
   source .venv/bin/activate

   # Windows (Command Prompt / PowerShell)
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependensi yang dibutuhkan:**
   ```bash
   pip install -r constraints.txt
   ```

---

## ▶️ Cara Menjalankan

### A. Menjalankan Skrip CLI (`01` – `03`)
```bash
# Menjalankan simulasi ujian (versi basic)
cd 03_mini_project/ujian_sekolah/basic
python3 ujian_sekolah.py

# Menjalankan skrip package eksternal
cd ../../../02_modules_python
python3 package_qrcode.py
```

### B. Menjalankan Modul & Studi Kasus Data Analyst (`04` – `05`)
1. Pastikan *virtual environment* (`.venv`) sudah aktif dan ekstensi **Jupyter** terpasang di VS Code (atau jalankan `jupyter notebook` di terminal).
2. Jika ingin me-regenerasi dataset mentah di folder `04_data_analyst`:
   ```bash
   cd 04_data_analyst
   python3 data/generate_data.py
   ```
3. Buka file `.ipynb` (seperti `04_data_analyst/project.ipynb` atau `05_studi_kasus_DA/main.ipynb`), pilih kernel `.venv`, lalu jalankan seluruh *cell* dari atas ke bawah (**Run All**).

---

## 📝 Catatan
- Jangan lupa perbarui `constraints.txt` dengan perintah `pip freeze > constraints.txt` setiap kali menambahkan pustaka baru untuk analisis data (seperti `pandas`, `seaborn`, atau `openpyxl`).
- Pastikan *working directory* saat menjalankan notebook berada di dalam masing-masing folder modul (`04_data_analyst/` atau `05_studi_kasus_DA/`) agar *relative path* menuju folder `data/` dan `reports/` terbaca dengan benar.
- Repository ini terus diperbarui seiring dengan penyelesaian versi `modular` pada seluruh *mini-project* CLI serta rencana eksplorasi integrasi database relasional (**Python + MySQL**).