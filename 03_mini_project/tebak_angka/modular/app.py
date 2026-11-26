from tebak_angka_modules import tebak_angka

def app_menu():
    while True:
        print("===== Game tebak Angka =====")
        print("1. Tebak Angka")
        print("2. Keluar")
        try:
            pilihan = int(input("Pilihan = "))

            if pilihan == 1:
                tebak_angka.tebak_angka()
            elif pilihan == 2:
                print("Selesai")
                break
            else:
                print("Input pilihan tidak valid")
        except ValueError:
            print("Masukkan angka yang valid")
        
app_menu()