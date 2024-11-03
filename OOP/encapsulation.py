 #kasus mobil

class Mobil:
    def __init__(self,nama,merek):
        self.nama = nama
        self.__merek = merek

# untuk memanggil atau merubah data sensitive
# seter and geter
    def setMerek(self,merek):
        self.__merek = merek

# get mengambil
    def getMerek(self):
        return self.__merek



honda = Mobil("CIVIC TURBO","HONDA")

print("Saya punya mobil : {nama_mobil}".format(nama_mobil = honda.nama))
print("Dengan Merek : {merek}".format(merek = honda.getMerek()))