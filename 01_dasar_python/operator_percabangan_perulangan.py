# Operator aritmatika
# +, -, *, /
# // pembagian bulat, % modulo pembagian sisa, ** pangkat

# Operator assigment
# =, +=, -=, /=, *=

# Operator banding
# <, >, ==, >=, <=, !=

# Operator logika
# and, or, not

# in untuk cek apakah text ada dalam string
kalimat = "Python bahasa terbaik"
print("Python" in kalimat) 
print("Javascript" in kalimat)
# repeat kalimat sesuai beberapa kalinya
print(kalimat*2)

angka = int(input("Masukkan nilai angka: "))
if angka > 0:
    print("Angka Positif")
elif angka < 0:
    print("Angka Negatif")
elif angka == 0:
    print("Angka Nol")


hari = input("Masukkan hari ini: ").lower()
match hari:
    case "senin" | "selasa" | "rabu" | "kamis" | "jumat":
        print("Hari Kerja")
    case "sabtu" | "Minggu":
        print("Hari Libur")
    case _:
        print("Hari tidak valid")



for i in range(5):
    print(i)

for i in range(1, 5):
    print(i)

for i in range(5, 1, -1):
    print(i)

nama = "python"
for huruf in nama:
    print(huruf)

angka = 1
while angka <= 5:
    print(angka)
    angka+=1

# Hanya mencetak ganjil
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)


kata = input("Masukkan kata? ")
cari = input("Masukkan huruf yang dicari? ")

for huruf in kata:
    if huruf == cari:
        print("Huruf ", cari, " ditemukan dalam kata")
        break
else:
    print("Huruf", cari, "tidak ditemukan dalam kata")


password_benar="12345"
max_percobaan = 3
percobaan= 0

while percobaan < max_percobaan:
    masukan = input("Masukkan password? ")
    percobaan+=1
    if masukan == password_benar:
        print("Berhasil login")
        break
    else:
        print("Password salah! percobaan ke ",percobaan," maksimal percobaan ", max_percobaan)
else:
    print("Terlalu banyak percobaan")

print("Tabel perkailian")
for i in range(1, 6):
    for j in range(1, 6):
        hasil = i*j 
        print(i,"*" ,j ,"=" ,hasil)
    print("---")