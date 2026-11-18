def hitung_luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print("luas persegi panjang adalah =", luas)

hitung_luas_persegi_panjang(5, 2)

# default 10 tapi kalau ada definisi luar lebih diutamakan
def hitung_luas_lingkaran(radius=10):
    pi = 3.14
    luas = 3.14*radius*radius
    return luas

luas1 = hitung_luas_lingkaran(15)
print("Luas lingkaran radius 10 =", luas1)

var_global = "saya seorang mahasiswa"
def perkenalan(nama, umur, kota):
    global var_global
    print(f"halo nama saya {nama}, umur saya {umur}, saya tinggal di {kota}, {var_global}")

perkenalan(umur=20, nama="satria", kota="jakarta")

def cetak_list(*list):
    for item in list:
        print(item)
cetak_list(1,2,3,4)

def cetak_dict(**dict):
    for key, value in dict.items():
        print(f"{key}: {value}")
cetak_dict(nama="satria", umur=20)

try:
    a = int(input("Masukkan nilai a = "))
    b = int(input("Masukkan nilai b = "))
    c = a/b
    print("Hasilnya =", c)

except ValueError:
    print("Masukkan angka yang valid")
except ZeroDivisionError:
    print("Tidak bisa dibagi dengan nol")
except:
    print("Terjadi kesalahan")

try:
    angka = int(input("Masukkan nilai a = "))

except ValueError:
    print("Masukkan angka yang valid")

else:
    if angka > 0:
        print("Angka Positif")
    elif angka < 0:
        print("Angka Negatif")
    else:
        print("Angka Nol")

finally:
    print("Selesai")