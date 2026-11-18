angka_rahasia = 7

while True:
    tebakan = int(input("Pilih angka tebakan dari 1-10? "))
    if tebakan == angka_rahasia:
        print("Selamat jawaban anda benar")
        break
    else:
        print("Coba lagi")