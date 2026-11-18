# Docs Module Random Link https://docs.python.org/3/library/random.html
import random

print("Random angka 1-10 =", random.randint(1,10))
print("Random angka decimal 0.0 - 9.9", random.uniform(0.0, 9.9))
buah = ["pisang", "apel", "jeruk", "semangka"]
pilihan = random.choice(buah)
print("Buah terpilih =", pilihan)