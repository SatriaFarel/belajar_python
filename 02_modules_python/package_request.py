# Fungsi: Untuk membuat HTTP requests (GET, POST, etc.)
# https://pypi.org/project/requests/ 
# pip install requests

import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200 :
    data = response.json()
    print(F"Title : {data["title"]}")
    print(f"Body : {data["body"]}")
else:
    print("Error", response.status_code)