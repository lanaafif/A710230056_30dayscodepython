class Tiket:
    def __init__(self, jenis):
        self.jenis = jenis
    
    def hitung_harga(self, jumlah):
        pass

class TiketBiasa(Tiket):
    def __init__(self):
        super().__init__('Biasa')
        self.harga = 50000  # Harga tiket biasa

    def hitung_harga(self, jumlah):
        return self.harga * jumlah

class TiketVIP(Tiket):
    def __init__(self):
        super().__init__('VIP')
        self.harga = 100000  # Harga tiket VIP

    def hitung_harga(self, jumlah):
        return self.harga * jumlah

class TiketGold(Tiket):
    def __init__(self):
        super().__init__('Gold')
        self.harga = 150000  # Harga tiket Gold

    def hitung_harga(self, jumlah):
        return self.harga * jumlah

def main():
    jenis_tiket = input("Masukkan jenis tiket (biasa/vip/gold) : ").strip().lower()
    jumlah_tiket = int(input("Masukkan jumlah tiket : "))
    
    if jenis_tiket == 'biasa':
        tiket = TiketBiasa()
    elif jenis_tiket == 'vip':
        tiket = TiketVIP()
    elif jenis_tiket == 'gold':
        tiket = TiketGold()
    else:
        print("Jenis tiket tidak valid!")
        return

    total_harga = tiket.hitung_harga(jumlah_tiket)
    print(f"Total Harga Tiket : Rp {total_harga}")

if __name__ == "__main__":
    main()