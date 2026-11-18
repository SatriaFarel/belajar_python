# Docs Module DateTime Link https://docs.python.org/3/library/datetime.html
import datetime

# Ambil tanggal sekarang
sekarang = datetime.datetime.now()
# Ambil hari ini
hari_ini = datetime.date.today()
# ambil jam sekarang 
waktu_sekarang = datetime.datetime.now().time()
# membuat tanggal kegiatan
tgl_kegiatan = datetime.date(2026, 10, 30)
# membuat tanggal kegiatan lengkap
acara = datetime.datetime(2026, 5, 20, 12, 30, 0)

print(f"""
      Sekarang tanggal {sekarang} \n
      sekarang hari {hari_ini} \n
      jam sekarang {waktu_sekarang} \n
      tanggal kegiatan {tgl_kegiatan} \n
      detail waktu acara {acara} \n
""")

print(f"""
Format ID = {sekarang.strftime("%d/%m/%y %M:%H:%S")} \n
Format Panjang = {sekarang.strftime("%A, %d %B %Y")} \n
Format Custom {sekarang.strftime("%d-%m-%y jam %H:%M")}
""")