import os
import random
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

# Pastikan folder data/ tersedia
os.makedirs("data", exist_ok=True)
np.random.seed(42)
random.seed(42)

# ==========================================
# 1. GENERATE pelanggan.csv (Untuk Tugas 2)
# ==========================================
jumlah_pelanggan = 200
kota_list = [
    "Jakarta Timur", "Jakarta Selatan", "Bekasi", "Depok",
    "Tangerang", "Bandung", "Surabaya", "jakarta timur ", " BEKASI"
]
segmen_list = ["Regular", "Silver", "Gold", "Platinum"]

data_pelanggan = []
for i in range(1, jumlah_pelanggan + 1):
    tgl_daftar = datetime(2025, 1, 1) + timedelta(days=random.randint(0, 600))
    data_pelanggan.append({
        "id_pelanggan": f"CUST-{i:04d}",
        "nama_pelanggan": f"Pelanggan_{i}",
        "kota": random.choice(kota_list) if random.random() > 0.05 else np.nan,
        "segmen": random.choice(segmen_list),
        "tanggal_daftar": tgl_daftar.strftime("%Y-%m-%d")
    })

df_pelanggan = pd.DataFrame(data_pelanggan)
df_pelanggan.to_csv("data/pelanggan.csv", index=False)

# ==========================================
# 2. GENERATE transaksi.csv & sales.csv
# ==========================================
jumlah_transaksi = 1500
produk_katalog = [
    ("PRD-01", "Mechanical Keyboard", "Elektronik", 650000, 420000),
    ("PRD-02", "Wireless Mouse", "Elektronik", 250000, 140000),
    ("PRD-03", "USB-C Hub 4-in-1", "Aksesoris", 180000, 95000),
    ("PRD-04", "Tumbler Stainless 900ml", "Lifestyle", 150000, 75000),
    ("PRD-05", "Laptop Stand Aluminum", "Aksesoris", 220000, 110000),
    ("PRD-06", "Monitor Light Bar", "Elektronik", 450000, 270000),
    ("PRD-07", "Desk Mat Leather", "Aksesoris", 120000, 55000),
    ("PRD-08", "Parfum Fresh 100ml", "Lifestyle", 190000, 85000),
]

metode_bayar = ["QRIS", "Transfer Bank", "E-Wallet", "Kartu Kredit", "qris ", "COD"]
status_kirim = ["Selesai", "Selesai", "Selesai", "Terlambat", "Dibatalkan"]

data_transaksi = []
for i in range(1, jumlah_transaksi + 1):
    prod = random.choice(produk_katalog)
    cust_id = f"CUST-{random.randint(1, jumlah_pelanggan):04d}"
    tgl = datetime(2026, 1, 1) + timedelta(days=random.randint(0, 325))
    
    # Format tanggal sengaja dicampur untuk latihan cleaning (Fase 3)
    rand_fmt = random.random()
    if rand_fmt < 0.75:
        tgl_str = tgl.strftime("%Y-%m-%d")
    elif rand_fmt < 0.90:
        tgl_str = tgl.strftime("%d/%m/%Y")
    else:
        tgl_str = tgl.strftime("%d-%b-%Y")

    qty = random.randint(1, 5)
    # Sisipkan outlier kuantitas ekstrem (1%)
    if random.random() < 0.01:
        qty = random.randint(25, 50)

    diskon_persen = random.choice([0, 0, 5, 10, 15, 20, 35])
    harga_satuan = prod[3]
    modal_satuan = prod[4]

    # Format harga kotor string "Rp xxx.xxx" pada 25% baris untuk latihan string cleaning
    if random.random() < 0.25:
        harga_str = f"Rp {harga_satuan:,.0f}".replace(",", ".")
    else:
        harga_str = str(harga_satuan)

    total_harga = int(harga_satuan * qty * (1 - diskon_persen / 100))
    profit = int((harga_satuan * (1 - diskon_persen / 100) - modal_satuan) * qty)

    # Sisipkan missing values (NaN) pada beberapa kolom
    kategori_val = prod[2] if random.random() > 0.04 else np.nan
    metode_val = random.choice(metode_bayar) if random.random() > 0.03 else np.nan

    data_transaksi.append({
        "id_transaksi": f"TRX-{i:05d}",
        "tanggal": tgl_str,
        "id_pelanggan": cust_id,
        "id_produk": prod[0],
        "nama_produk": prod[1],
        "kategori": kategori_val,
        "harga_satuan": harga_str,
        "qty": qty,
        "diskon_persen": diskon_persen,
        "total_harga": total_harga,
        "profit": profit,
        "metode_pembayaran": metode_val,
        "status_pengiriman": random.choice(status_kirim)
    })

df_transaksi = pd.DataFrame(data_transaksi)

# Tambahkan 30 baris duplikat sengaja untuk latihan drop_duplicates()
duplikat = df_transaksi.sample(30, random_state=42)
df_transaksi = pd.concat([df_transaksi, duplikat], ignore_index=True)

# Simpan sebagai transaksi.csv dan sales.csv agar kompatibel dengan semua contoh modul
df_transaksi.to_csv("data/transaksi.csv", index=False)
df_transaksi.to_csv("data/sales.csv", index=False)

print("Berhasil men-generate dataset di folder data/:")
print(f"- data/pelanggan.csv : {len(df_pelanggan)} baris")
print(f"- data/transaksi.csv : {len(df_transaksi)} baris (termasuk 30 duplikat & data kotor)")
print(f"- data/sales.csv     : {len(df_transaksi)} baris")