# Fungsi: Menambahkan warna dan styling pada output terminal
# https://pypi.org/project/colorama/ 
# pip install colorama

from colorama import Fore, init

init()

print(Fore.RED + "Teks Merah")
print(Fore.YELLOW + "Teks Kuning")
print(Fore.GREEN + "Teks Hijau")
print(Fore.BLUE + "Teks Biru")
print(Fore.CYAN + "Teks Biru Muda")
print(Fore.MAGENTA + "Teks Merah Muda")
