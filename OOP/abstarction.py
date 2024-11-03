from abc import ABC , abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def nyalakan_mesin (self):
        pass


class Mobil(Kendaraan):
    def nyalakan_mesin(self):
        return "Start"

class Motor(Kendaraan):
    def nyalakan_mesin(self):
        return "Motor Mogok"


# kendaraan = Kendaraan()
# print(kendaraan.nyalakan_mesin())
mobil = Mobil()
print(mobil.nyalakan_mesin())