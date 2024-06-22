def konversi_suhu():
    print("Pilih konversi suhu:")
    print("1. Celcius ke Fahrenheit")
    print("2. Fahrenheit ke Celcius")

    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == '1':
        celcius = float(input("Masukkan suhu dalam Celcius: "))
        fahrenheit = (celcius * 9/5) + 32
        print(f"Suhu dalam Fahrenheit: {fahrenheit}")
    elif pilihan == '2':
        fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        celcius = (fahrenheit - 32) * 5/9
        print(f"Suhu dalam Celcius: {celcius}")
    else:
        print("Pilihan tidak valid.")

konversi_suhu()
