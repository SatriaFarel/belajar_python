def ambil_soal():
    soal_asli = []
    with open("bank_soal.txt", "r")as file:
        for line in file:
            if line.strip():
                soal_asli.append(line.strip())
    return soal_asli

def buat_soal():
    soal_asli = ambil_soal()
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

def app_ujian():
    soal_ujian = buat_soal()
    opsi = ["a", "b", "c", "d"]
    
    jawaban_benar = 0
    jawaban_salah = 0
    
    for i in range(len(soal_ujian)):
        soal = soal_ujian[i]
        print(f"Pertanyaan {i+1} : {soal["pertanyaan"]}")
        print("Jawaban :")
        
        for j in range(len(soal["jawaban"])):
            jawaban = soal["jawaban"][j]
            print(opsi[j], ".", jawaban)
        
        jawaban_user = input("Pilihan jawaban A/B/C/D ?")
        jawaban_user_index = opsi.index(jawaban_user)
        jawaban_asli_user = soal["jawaban"][jawaban_user_index]
        
        if jawaban_asli_user == soal["jawaban_benar"]:
            print("Jawaban anda benar")
            jawaban_benar+=1
        else:
            print("Jawaban anda salah")
            jawaban_salah+=1
            
    print("Hasil Ujian")
    print(f"Jawaban benar : {jawaban_benar}")
    print(f"Jawaban salah : {jawaban_salah}")
    print("hasil_ujian =", jawaban_benar / (jawaban_benar+jawaban_salah)*100, "%")
    
    
app_ujian()