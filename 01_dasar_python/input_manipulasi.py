nama = input("Masukkan nama anda: ")
print("Hello, ", nama)

umur_teks = input("Masukkan umur anda: ")
# konversi to int 
umur = int(umur_teks)
print("Umur anda: ",umur)
print("Type data: ", type(umur))

# konversi to string
pesan = "Nama saya " + nama + " umur saya" + str(umur)
print(pesan)
# cek jumlah panjang / length dari pesan
print(len(pesan))

nama = "satria"
print(nama[0]) # karakter pertama dan seterusnya (s)
print(nama[-1]) # karakter terakhir dan seterusnya (a)
print(nama[0:3]) # dari pertama sampai huruf ke 3 (sat)
print(nama[:4]) # dari awal sampai ke 4 (satr)
print(nama[2:]) # dari 2 sampai akhir (tria)
print(nama[:]) # print semuanya (satria)

nama = "john doe"
# auto uppercase
print(nama.upper())
# auto lowercase
print(nama.lower())
# auto text title
print(nama.title())
# auto huruf awal kapital
print(nama.capitalize())
constrip = "    john doe"
# menghapus space kosong
print(constrip.strip())
kalimat = "I Love Java"
# replace isi string
print(kalimat.replace("Java", "Python"))

kalimat = "baris pertama \n baris kedua"
print(kalimat)
kalimat = "nama:\t alice\t umur:\t 30"
print(kalimat)
kalimat = "I\'am satria"
print(kalimat)
kalimat = "dia berkata \"saya suka kamu\" begitu"
print(kalimat)

nama = "satria"
umur = 18
kota = "jakarta"

# f string agar varibel bisa di masukkan dengan {} tanpa +
profil = f"Halo, nama saya {nama}, umur saya {umur}, saya tinggal di {kota}"
print(profil)

harga=1000
jumlah=5
total = f"Total: {harga*jumlah:,}"
print(total)

nama = "john doe"
print(f"Halo {nama.upper()}")
