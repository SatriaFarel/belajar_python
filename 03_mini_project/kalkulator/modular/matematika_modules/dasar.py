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