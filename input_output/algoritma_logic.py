nilai_raport = 10
#if
#if(kondisi yang di mau)
if nilai_raport > 5:
    print("wah nilai saya bagus nih !")

print("===== Soal 2 =====")
#if else
# petik satu itu artinya char karakter
# petik dua itu artinya string
# char nama[12] ini artinya panjang variabel nama max 12 karakter
# char nama[12] berubah jadi char nama [255] === string
# java (ex)
nilai_raport = 'F'
if nilai_raport == 'A' :
    print("Selamat kamu lulus ujian ini !")
else :
    print("Sana kamu remedial lagi!!!!!")
print("====== Soal 3 =====")
nilai_raport = 'C'
if nilai_raport == 'A' :
    print("Selamat kamu lulus dengan nilai sempurna !")
elif nilai_raport == 'B':
    print("Selamat kamu lulus belajar sedikit lagi ya !")
elif nilai_raport == 'C':
    print("Selamat kamu lulus tapi nilainya pas ni belajar lagi")
else :
    print("Sana kamu remedial lagi !!!!")

print("===== Tenary =====")
a = 10
b = 12
bandingkan = "Posisi A Menang" if a > b else "Posisi B Menang"
print(bandingkan)      