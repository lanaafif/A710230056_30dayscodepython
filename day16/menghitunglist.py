# Meminta jumlah karakter yang akan dimasukkan
n = int(input("Berapa jumlah karakter yang akan dimasukkan? "))

# Inisialisasi daftar untuk menyimpan karakter
arr = []

# Mengumpulkan karakter dari pengguna
for _ in range(n):
    arr.append(input("Masukkan karakter apapun, boleh juga kata: "))

# Meminta karakter yang dicari
karakter_yang_dicari = input("Karakter apa yang kamu cari dari deret diatas? ")

# Menghitung jumlah kemunculan karakter yang dicari dalam deret
jumlah_kemunculan = arr.count(karakter_yang_dicari)

# Menampilkan hasil
print(f"Karakter '{karakter_yang_dicari}' muncul {jumlah_kemunculan} kali.")
