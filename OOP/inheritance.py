# kasus
# manusia

class Ibu:
    panggilan = "default"
    # def __init__(self,panggilan): #contruktor ini harus di isi saat dipanggil
    #      self.panggilan = panggilan

    def __init__(self,panggilan,sifat):
        self.panggilan = panggilan
        self.__sifat = sifat

    def memanggil(self):
        print("Iya, Ada apa?")
    def setSifat(self,sifat):
        self.__sifat = sifat
    def getSifat(self):
        return self.__sifat

class Anak(Ibu):
    def suruh(self):
        print("nanti dulu lah!!!")

sekolah = Anak("ucok","malas")

print("Siapa nama anak ini : {nama_anak}".format(nama_anak = sekolah.panggilan))
sekolah.memanggil()
