Buat notebook baru dan selesaikan 5 Misi Utama berikut secara mandiri:

1. Misi Data Cleaning:
Hapus baris duplikat pada pesanan_kopi.csv.
Rapikan teks berantakan & nilai kosong (NaN) pada kolom cabang dan tipe_order.
Ubah waktu_transaksi menjadi tipe datetime.

2. Misi Data Enrichment (Gabung & Hitung Kolom Baru):
Gabungkan (merge) data pesanan dengan menu_kopi.csv berdasarkan id_menu.

3. Buat 2 kolom hitungan baru: omzet (harga_jual * qty) dan profit ((harga_jual - modal) * qty).
Filter data hanya untuk pesanan dengan status == "Selesai".

4. Misi Menjawab Pertanyaan Bisnis (Cetak angkanya di notebook):
Pertanyaan A: Menu kopi (kategori == "Coffee") mana yang menyumbang total profit paling besar?
Pertanyaan B: Cabang mana yang memiliki rata-rata nilai belanja per transaksi paling tinggi?
Pertanyaan C: Pada jam berapa (07–22) kedai paling ramai menerima pesanan? (Hint: pakai .dt.hour pada kolom waktu_transaksi).

5. Misi Visualisasi (Simpan ke folder reports/):
Buat 1 Bar Chart yang membandingkan total omzet antar tipe_order (Dine-In, GoFood, dll.).
Buat 1 Line Chart yang menunjukkan tren jumlah transaksi per jam (dari jam 7 pagi sampai 10 malam) untuk melihat peak hour kedai.