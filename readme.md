# 🐍 Python Fundamentals & Ecosystem

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active%20Learning-2ea44f?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

Repository dokumentasi terstruktur yang mencakup perjalanan pembelajaran bahasa pemrograman Python—mulai dari sintaks fundamental, struktur data, manajemen file, eksplorasi *modules & packages*, hingga pengembangan *mini-projects* dalam arsitektur **Basic (Single-File)** dan **Modular**.

---

## 📑 Daftar Isi
- [Struktur Repository](#-struktur-repository)
- [Highlight Mini-Projects](#-highlight-mini-projects)
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

---

## 🚀 Highlight Mini-Projects

| Project | Deskripsi Singkat | Konsep Utama | Status Arsitektur |
| :--- | :--- | :--- | :--- |
| **`ujian_sekolah`** | Simulasi ujian pilihan ganda yang memuat soal dari `bank_soal.txt`, mengacak urutan pertanyaan dan opsi jawaban, serta menghitung persentase skor akhir. | File I/O, `random`, `list`, `dictionary`, string parsing | `basic` (Selesai) · `modular` (In Progress) |
| **`kalkulator`** | Aplikasi kalkulator aritmatika interaktif berbasis CLI. | Fungsi, percabangan, validasi input | `basic` (Selesai) · `modular` (In Progress) |
| **`tebak_angka`** | Permainan tebak angka acak dengan sistem petunjuk tinggi/rendah dan batas percobaan. | Perulangan `while`, modul `random`, kontrol alur | `basic` (Selesai) · `modular` (In Progress) |

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

Jalankan skrip melalui terminal dengan masuk ke direktori masing-masing project atau materi:

```bash
# Menjalankan simulasi ujian (versi basic)
cd 03_mini_project/ujian_sekolah/basic
python3 ujian_sekolah.py

# Menjalankan skrip package eksternal
cd ../../../02_modules_python
python3 package_qrcode.py
```

---

## 📝 Catatan
- Pastikan file pendukung seperti `bank_soal.txt` berada di dalam folder `03_mini_project/ujian_sekolah/basic/` (atau disesuaikan *path*-nya) agar skrip `ujian_sekolah.py` dapat membacanya tanpa kendala.
- Repository ini terus diperbarui seiring dengan penyelesaian versi `modular` pada seluruh *mini-project* serta pendalaman materi ke tingkat lanjut (*Object-Oriented Programming* dan pengembangan API).