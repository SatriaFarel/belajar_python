import requests
from post_comment_module import comment

def menu_post():
    while True:
        print("================")
        print("Menu Post")
        print("1. Tampilkan semua post")
        print("2. Tampilkan post sesuai id")
        print("3. Keluar")
    
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            tampilkan_semua_post()
        elif pilihan == 2:
            post_id = int(input("Masukkan id post: "))
            tampilkan_post_berdasarkan_id(post_id)
            comment.menu_comment(post_id)
        elif pilihan == 3:
            print("=== Program post selesai ===")
            break
        
def ambil_semua_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        list = response.json()
        return list
    else:
        print(response.status_code, "Gagal mengambil response")
        return []
    
def tampilkan_semua_post():
    list_post = ambil_semua_post()
    for post in list_post:
        print("==============")
        print(f"Id Post : {post['id']}")
        print(f"Title : {post['title']}") 
        
    
def tampilkan_post_berdasarkan_id(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    if response.status_code == 200:
        data = response.json()
        print("==============")
        print(f"Id Post : {data['id']}")
        print(f"Title : {data['title']}") 
    else:
        print(response.status_code, "Gagal mengambil response")
        return []
    