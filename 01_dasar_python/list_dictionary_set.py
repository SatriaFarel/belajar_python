daftar_kosong=[]
angka=[1,2,3,4,5]
print(angka)
campuran=["satria", 15, "prog"]
print(campuran)

buah=["pisang", "jeruk"]
buah.append("alpukat")
# Menghapus terbaru
buah.pop()
# Menghapus sesuai yng dinginkna
buah.remove("jeruk")
# menghapus melalu index
del buah[0]
buah=["pisang", "jeruk"]
print(len(buah))

list1 = [1,2,3]
list2 = [4,5,6]
gabungan = list1+list2
print(gabungan)

if "pisang" in buah:
    print("tersedia")

print("Daftar Buah")

for item in buah:
    print("--", item)

siswa = {
    "Nama":"satria",
    "Umur":20,
}
print(siswa)

# buat nambahin atau ubah value
siswa["Umur"]=23

for key in siswa:
    print(key, ":", siswa[key])

buah = {"jeruk", "kelapa"}
buah.add("alpukat")
buah.remove("jeruk")
print(buah)