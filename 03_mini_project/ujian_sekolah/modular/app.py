from ujian_sekolah_package import app

def app_ujian():
    soal_ujian = app.buat_soal("bank_soal.txt")
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