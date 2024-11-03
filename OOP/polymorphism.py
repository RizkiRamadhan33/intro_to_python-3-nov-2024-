# kasus mobil

class Mobil:
    def hidupkan_mesin(self):
        return "Mobil Menyala"

class ElectricMobil(Mobil):
    def hidupkan_mesin(self):
        return "Akinya soak"



def start(Mobil):
    print(Mobil.hidupkan_mesin())


# cara panggil
mobil = Mobil()
listrik = ElectricMobil()

start(mobil)
start(listrik)
