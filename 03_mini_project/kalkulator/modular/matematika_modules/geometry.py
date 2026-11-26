import math

def luas_persegi():
    try:
        sisi = int(input("Masukkan nilai sisi : "))
        hasil = sisi*sisi
        print("Hasil luas persegi =", hasil)
    except ValueError:
        print("Masukkan inputan yang valid")

def luas_persegi_panjang():
    try:
        panjang = int(input("Masukkan nilai panjang : "))
        lebar = int(input("Masukkan nilai lebar : "))
        hasil = panjang*lebar
        print("Hasil luas persegi panjang =", hasil)
    except ValueError:
        print("Masukkan inputan yang valid")

def luas_lingkaran():
    try:
        radius = int(input("Masukkan nilai radius : "))
        hasil = math.pi*radius*radius
        print("Hasil luas lingkaran =", hasil)
    except ValueError:
        print("Masukkan inputan yang valid")
