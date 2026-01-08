# =========================================
# Program Hitung Luas dan Keliling Bangun Datar
# Organisasi: IMPMBL
# =========================================

def luas_persegi(sisi):
    return sisi * sisi

def keliling_persegi(sisi):
    return 4 * sisi

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def keliling_persegi_panjang(panjang, lebar):
    return 2 * (panjang + lebar)

def menu():
    print("===================================")
    print(" IMPIBL - Aplikasi Bangun Datar ")
    print("===================================")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Keluar")

def main():
    while True:
        menu()
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            sisi = float(input("Masukkan sisi: "))
            print("Luas:", luas_persegi(sisi))
            print("Keliling:", keliling_persegi(sisi))

        elif pilihan == "2":
            p = float(input("Masukkan panjang: "))
            l = float(input("Masukkan lebar: "))
            print("Luas:", luas_persegi_panjang(p, l))
            print("Keliling:", keliling_persegi_panjang(p, l))

        elif pilihan == "3":
            print("Terima kasih - IMPMBL")
            break

        else:
            print("Pilihan tidak valid")

main()
