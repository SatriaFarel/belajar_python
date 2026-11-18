# Docs Module OS Link https://docs.python.org/3/library/os.html
import os

print("Directory kerja saat ini =", os.getcwd())
print("Nama sistem =", os.name)
print("Cek file / folder", os.path.exists("text.txt"))
if os.path.exists("text.txt"):
    print(f"""
    Adalah file: {os.path.isfile("text.txt")} \n 
    Adalah directory: {os.path.isdir("text.txt")} \n 
    Ukuran file: {os.path.getsize("text.txt"), "bytes"} \n
    """)

file_path = "kishiyuusha/Downloada/Module\ Belajar/Modules\ Python/text.txt"
print(f"""
Directory : {os.path.dirname(file_path)}
Nama File : {os.path.basename(file_path)}
Nama tanpa ekstensi : {os.path.splitext(file_path)[0]}
Ekstensi : {os.path.splitext(file_path)[1]}    
""")