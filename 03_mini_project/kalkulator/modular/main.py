from matematika_modules import dasar, geometry

def app_menu():
    while True:
        print("===== Kalkulator Sederhana =====")
        print("Pilih menu :")
        print("1. Operasi dasar")
        print("2. Operasi Geometri")
        print("3. Keluar ")
        try:
            pilihan_menu = int(input("Pilihan = "))
            if pilihan_menu == 1:
                print("Pilih operasi apa :")
                print("1. Penjumlahan")
                print("2. Pengurangan")
                print("3. Perkalian ")
                print("4. Pembagian ")
                print("5. Kembali ")
                        
                pilihan = int(input("Pilihan = "))
                if pilihan == 1:
                    dasar.operasi_penjumlahan()
                elif pilihan == 2:
                    dasar.operasi_pengurangan()
                elif pilihan == 3:
                    dasar.operasi_perkalian()
                elif pilihan == 4:
                    dasar.operasi_pembagian()
                elif pilihan == 5:
                    print("Kembali ke menu awal!")
                else:
                    print("Input pilihan tidak valid")
            elif pilihan_menu == 2:
                print("Pilih operasi apa :")
                print("1. Menghitung Luas Persegi")
                print("2. Menghitung Luas Persegi Panjang")
                print("3. Menghitung Luas Lingkaran ")
                print("4. Kembali ")
                        
                pilihan = int(input("Pilihan = "))
                if pilihan == 1:
                    geometry.luas_persegi()
                elif pilihan == 2:
                    geometry.luas_persegi_panjang()
                elif pilihan == 3:
                    geometry.luas_lingkaran()
                elif pilihan == 4:
                    print("Kembali ke menu awal!")
                else:
                    print("Input pilihan tidak valid")
            elif pilihan_menu == 3:
                print("=== Selesai ===")
                break
            else:
                print("Input tidak sesuai!")
        except ValueError:
            print("Masukkan nomor pilihan yang valid")

app_menu()