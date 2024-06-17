class Car:
    def __init__(self, merk, model, tahun):
        self.merk = merk
        self.model = model
        self.tahun = tahun
        self.odometer = 0

    def keterangan(self):
        print(f"Mobil baru saya {self.merk} {self.model} tahun {self.tahun} kilometernya masih {self.odometer}")


class ElectricCar(Car):
    def __init__(self, merk, model, tahun):
        super().__init__(merk, model, tahun)


teslaku = ElectricCar('tesla', 'model X', '2022')
print(teslaku.keterangan())