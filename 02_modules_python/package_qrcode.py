# Fungsi: Membuat QR code
# pip install qrcode
# Untuk menggunakan package qrcode, kita butuh package pillow sebelumnya
import qrcode

img = qrcode.make("kishiyuusha.my.id")
img.save("assets/demo_qrcode.png")
print("QRcode berhasil dibuat")