from post_comment_module import comment, post

def app_menu():
    while True:
        print("Program Post Comment")
        print("1. Lihat Daftar Post")
        print("2. Keluar")
        
        pilihan = int(input("Masukkan Pilihan anda: "))
        if pilihan == 1:
            post.menu_post()
        elif pilihan == 2:
            print("Program di tutup!")
            break
        else:
            print("Input tidak sesuai")
            
app_menu()