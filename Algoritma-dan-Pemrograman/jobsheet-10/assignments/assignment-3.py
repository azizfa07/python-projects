def programOhm(R1, R2):
    rangkaianSeri = R1 + R2
    rangkaianParalel = (R1 * R2) / (R1 + R2)
    print(f"besar hambatan pada rangkain seri adalah {rangkaianSeri:.2f} ohm")
    print(f"besar hambatam pada rangkaian paralel adalah {rangkaianParalel:.2f} ohm")
    
def konversSuhu(celcius):
    celciuusReamur = 4 /5 * celcius
    celciusFahrenheit = (9 / 5 * celcius) + 32
    celciusKelvin = celcius + 273
    print(f"Hasil konversi celcius ke reamur adalah {celciuusReamur:.2f} R")
    print(f"Hasil konversi celcius ke fahrenheit adalah {celciusFahrenheit:.2f} F")
    print(f"Hasil konversi celcius ke kelvin adalah {celciusKelvin:.2f} K")

def konversiMataUang(rupiah):
    rupiahDollarAs = rupiah / 16300
    rupiahRinggit = rupiah /3650
    rupiahEuro = rupiah / 17500
    print(f"hasil konversi rupiah ke dollar as adalah {rupiahDollarAs:.2f}")
    print(f"hasil konversi rupiah ke ringgit adalah {rupiahRinggit:.2f}")
    print(f"hasil konversi rupiah ke euro adalah {rupiahEuro:.2f}")

def validasiInput(pilihan):
    while True:
        inputPengguna = input(pilihan)
        try: 
            nilaiValid = float(inputPengguna)
            return nilaiValid
        except ValueError:
            print("Input salah")

def main():
    while True :
        print("=== Kalkulaor Multifungsi ===")
        print("1. Penghitung hambatan total (Ohm)")
        print("2. penghitung konversi suhu dari celcius")
        print("3. penghitung konversi mata uang dari rupiah")

        pilihanMenu = validasiInput("Masukkan pilihan anda : ")

        if pilihanMenu == 1 :
            R1 = validasiInput("Masukkan R1 : ")
            R2 = validasiInput("Masukkan R2 : ")
            programOhm(R1, R2)

        elif pilihanMenu == 2:
            celcius = validasiInput("Masukkan besar suhu celcius : ")
            konversSuhu(celcius)

        elif pilihanMenu == 3:
            rupiah = validasiInput("Masukkan besar uang dalam rupiah : ")
            konversiMataUang(rupiah)
        else:
            print("input tidak ada di menu")
if __name__ == "__main__":
    main()

 

 