import math

def hitung_persegi():
    print("\n--- Luas Persegi ---")
    sisi = float(input("Masukkan panjang sisi: "))
    print(f"Luas Persegi: {sisi * sisi} cm2")

def hitung_lingkaran():
    print("\n--- Luas Lingkaran ---")
    r = float(input("Masukkan jari-jari: "))
    luas = math.pi * (r**2)
    print(f"Luas Lingkaran: {luas:.2f} cm2")

def hitung_segitiga():
    print("\n--- Luas Segitiga ---")
    a = float(input("Masukkan alas: "))
    t = float(input("Masukkan tinggi: "))
    luas = 0.5 * a * t
    print(f"Luas Segitiga: {luas:.2f} cm2")

# Program Utama
while True:
    print("\n=== APLIKASI GEOMETRI ===")
    print("1. Hitung Persegi")
    print("2. Hitung Lingkaran")
    print("3. Hitung Segitiga")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        hitung_persegi()
    elif pilihan == '2':
        hitung_lingkaran()
    elif pilihan == '3':
        hitung_segitiga()
    elif pilihan == '4':
        print("Terima kasih!")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")