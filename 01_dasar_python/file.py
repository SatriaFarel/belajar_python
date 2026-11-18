print("Simpan data Nilai")

file = open("siswa.txt", "w")

while True:
    nama = input("Nama siswa = ")
    if nama == "":
        break
    nilai = input("Nilai = ")

    file.write(nama + "," + nilai + "\n")
    print(f"Data {nama} telah tersimpan")

file.close()
print("Semua data berhasil disimpan")

print("Menampilkan data nilai")

# ada dua pilih ada saran sih kedua
# file = open("siswa.txt", "r")

# for line in file:
#     data = line.strip().split(",")
#     print(f"{data[0]} : {data[1]}")
try:
    with open("siswa.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            print(f"{data[0]} : {data[1]}")
except FileNotFoundError:
    print("File siswa.txt tidak ditemukan")

# file close untuk cara pertama
# file.close()
print("Selesai")