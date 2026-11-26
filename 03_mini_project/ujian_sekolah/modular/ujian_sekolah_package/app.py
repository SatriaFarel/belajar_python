def ambil_soal(lokasi_file):
    soal_asli = []
    with open(lokasi_file, "r")as file:
        for line in file:
            if line.strip():
                soal_asli.append(line.strip())
    return soal_asli

def buat_soal(lokasi_file):
    soal_asli = ambil_soal(lokasi_file)
    import random
    
    random.shuffle(soal_asli)
    soal_ujian = []
    for i in range(10):
        soal = soal_asli[i]
        data = soal.split("|")
        
        pertanyaan = data[0]
        semua_jawaban = data[1]
        
        jawaban = semua_jawaban.split(",")
        jawaban_benar = jawaban[0]
        random.shuffle(jawaban)
        
        soal_ujian.append({
            "pertanyaan": pertanyaan,
            "jawaban": jawaban,
            "jawaban_benar": jawaban_benar
        })
        
    return soal_ujian