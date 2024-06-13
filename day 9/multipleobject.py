class Kucing():
    def __init__(self, ras, umur):
        self.ras = ras
        self.umur = umur

    def tampil(self):
        print(f"Kucingku berjenis {self.ras} dengan umur{self.umur} bulan")

kucing_saya = Kucing("persia",2)
kucing_dia = Kucing("anggora",3)

kucing_saya.tampil()
kucing_dia.tampil()