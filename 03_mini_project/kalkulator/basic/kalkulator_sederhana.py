def operasi_penjumlahan():
    try:
        a = int(input("Masukkan angka pertama : "))
        b = int(input("Masukkan angka kedua : "))
        hasil = a + b
        print("Hasil penjumlahan =", hasil)
    except ValueError:
        print("Masukkan inputan yang valid")

def operasi_pengurangan():
    try:
        a = int(input("Masukkan angka pertama : "))
        b = int(input("Masukkan angka kedua : "))
        hasil = a - b
        print("Hasil pengurangan =", hasil)
    except ValueError:
        print("Masukkan inputan yang valid")

def operasi_perkalian():
    try:
        a = int(input("Masukkan angka pertama : "))
        b = int(input("Masukkan angka kedua : "))
        hasil = a * b
        print("Hasil perkalian =", hasil)
    except ValueError:
        print("Masukkan inputan yang valid")

def operasi_pembagian():
    try:
        a = int(input("Masukkan angka pertama : "))
        b = int(input("Masukkan angka kedua : "))
        hasil = a / b
        print("Hasil pembagian =", hasil)
    except ValueError:
        print("Masukkan inputan yang valid")

def app_menu():
    while True:
        print("===== Kalkulator Sederhana =====")
        print("Pilih operasi apa :")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian ")
        print("4. Pembagian ")
        print("5. Keluar ")
        try:
            pilihan = int(input("Pilihan = "))
            if pilihan == 1:
                operasi_penjumlahan()
            elif pilihan == 2:
                operasi_pengurangan()
            elif pilihan == 3:
                operasi_perkalian()
            elif pilihan == 4:
                operasi_pembagian()
            elif pilihan == 5:
                print("===== Selesai =====")
                break
            else:
                print("Input pilihan tidak valid")
        except ValueError:
            print("Masukkan nomor pilihan yang valid")
        

app_menu()
