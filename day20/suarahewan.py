class HewanPeliharaan:
 
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def bersuara(self):
   
        if self.jenis == "Kucing":
             print(f"{self.nama} mengeong.")
        elif self.jenis == "Anjing":
            print(f"{self.nama} menggonggong.")
        else:
            print(f"{self.nama} mengeluarkan suara.")  # Suara default

# Memuat objek hewan peliharaan
kucingku = HewanPeliharaan("Luna", "Kucing")
anjingku = HewanPeliharaan("Snoopy", "Anjing")
peliharaanMisterius = HewanPeliharaan("Misteri", "Tidak Diketahui")

# Memanggil fungsi bersuara untuk setiap objek
kucingku.bersuara()
anjingku.bersuara()
peliharaanMisterius.bersuara()
