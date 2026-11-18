def tebak_angka():
    import random
    percobaan = 0
    max_percobaan = 3
    tebakan_benar = random.randint(1,10)

    while percobaan < max_percobaan:
        try:
            tebakan = int(input("Masukkan tebakan angka dari 1-10 ="))
            percobaan+=1
            if tebakan > tebakan_benar:
                print("Tebakan terlalu besar")
                print(f"Percobaan ke {percobaan}, maksimal percobaan 3 kali")
            elif tebakan < tebakan_benar:
                print("Tebakan terlalu kecil")
                print(f"Percobaan ke {percobaan}, maksimal percobaan 3 kali")
            else:
                print("Selamat anda berhasil menebak angka yang benar yaitu =", tebakan_benar)
                break
        except ValueError:
            print("Masukkan inputan angka yang sesuai")
    else:
        print("Sayang sekali percobaan telah habis")


def app_menu():
    while True:
        print("===== Game tebak Angka =====")
        print("1. Tebak Angka")
        print("2. Keluar")
        try:
            pilihan = int(input("Pilihan = "))

            if pilihan == 1:
                tebak_angka()
            elif pilihan == 2:
                print("Selesai")
                break
            else:
                print("Input pilihan tidak valid")
        except ValueError:
            print("Masukkan angka yang valid")
        
app_menu()