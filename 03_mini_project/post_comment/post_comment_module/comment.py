import requests

def menu_comment(post_id):
    while True:
        print("=============")
        print("Menu Comment")
        print(f"1. Tampilkan semua comment dari post {post_id}")
        print(f"2. Tampilkan comment berdasarkan id comment dari post {post_id}")
        print("3. Keluar")
        
        pilihan = int(input("Masukkan pilihan: "))
        if pilihan == 1:
            tampilkan_semua_comment(post_id)
        elif pilihan == 2:
            comment_id = int(input("Masukkan id comment: "))
            tampilkan_comment_berdasarkan_id(post_id, comment_id)
        elif pilihan == 3:
            print("Program comment di tutup")
            break
        else:
            print("Masukkan nilai tidak valid")
            
def ambil_semua_comment(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}/comments")
    if response.status_code == 200:
        list = response.json()
        return list
    else:
        print(f"{response.status_code}, Data gagal diambil")
        return [ ]
    
def tampilkan_semua_comment(post_id):
    data = ambil_semua_comment(post_id)
    for comment in data:
        print("==============")
        print(F"Id Comment : {comment['id']}")
        print(F"Name : {comment['name']}")
        
    
    
def tampilkan_comment_berdasarkan_id(post_id, comment_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/comments/{comment_id}")
    if response.status_code == 200:
        data = response.json()
        if data["postId"] == post_id:
            print("========")
            print(f"Id Comment : {data["id"]}")
            print(f"Name : {data["name"]}")
            print(f"Body : {data["body"]}")
        else:
            print("Id comment tidak sesuai")
        
    else:
        print(f"{response.status_code}, Data gagal diambil")