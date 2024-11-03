 #kasus
 # kita disuruh amati hewan

class Hewan: #Hewan itu nama class
    nama_hewan = "" # nama_hewan object
    jenis_hewan = ""
    umur_hewan = 10 #object property dimaa umur_hewan tidak dapat diubah private

    def __init__(self,nama,jenis): #contruktor
     self.nama_hewan = nama
     self.jenis_hewan = jenis

    def makan(self):
        print("hewan sedang makan !!!")

# cara panggil
kucing = Hewan("tom","anggora")
kucing = Hewan()
# variabel
print("nama kucing {nama}".format(nama = kucing.nama_hewan))
print("jenis kucing {jenis}".format(jenis = kucing.jenis_hewan))
print("umur hewan {umur}".format(umur = kucing.umur_hewan))
# memanggil function atau method
print("Sedang apa kucing ? ")
kucing.makan()
