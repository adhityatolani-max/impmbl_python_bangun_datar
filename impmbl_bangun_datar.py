# ==========================================
# APLIKASI EDUKASI IMPMBL
# Hitung Luas & Keliling Bangun Datar
# Bidang Pendidikan
# ==========================================

def luas_persegi(s):
    return s * s

def keliling_persegi(s):
    return 4 * s

def luas_persegi_panjang(p, l):
    return p * l

def keliling_persegi_panjang(p, l):
    return 2 * (p + l)


def menu():
    print("===================================")
    print("IMPMBL")
    print("Ikatan Montolutusan Pemuda Mahasiswa Banggai Laut")
    print("Bidang Pendidikan")
    print("===================================")
    print("1. Luas Persegi")
    print("2. Keliling Persegi")
    print("3. Luas Persegi Panjang")
    print("4. Keliling Persegi Panjang")
    print("5. Keluar")

    pilih = input("Pilih menu (1-5): ")

    if pilih == "1":
        s = float(input("Masukkan sisi: "))
        print("Hasil Luas:", luas_persegi(s))

    elif pilih == "2":
        s = float(input("Masukkan sisi: "))
        print("Hasil Keliling:", keliling_persegi(s))

    elif pilih == "3":
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        print("Hasil Luas:", luas_persegi_panjang(p, l))

    elif pilih == "4":
        p = float(input("Masukkan panjang: "))
        l = float(input("Masukkan lebar: "))
        print("Hasil Keliling:", keliling_persegi_panjang(p, l))

    elif pilih == "5":
        print("Terima kasih, Salam IMPMBL")
        return

    else:
        print("Pilihan tidak valid")

    print()
    menu()


menu()
