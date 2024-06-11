def lirik_anak_bebek(jumlah):
    for i in range(jumlah, 0, -1):
        if i == 1:
            print(f"Anak bebek turun {i}, mati satu tinggal induknya")
        else:
            print(f"Anak bebek turun {i}, mati satu tinggal {i-1}")

# Meminta input jumlah anak bebek dari pengguna
jumlah_anak_bebek = int(input("Masukkan jumlah anak bebek: "))
lirik_anak_bebek(jumlah_anak_bebek)
