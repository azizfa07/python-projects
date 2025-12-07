# Balok

p = float(input("Masukkan panjang (p) : "))
l = float(input("Masukkan lebar (l)   : "))
t = float(input("Masukkan tinggi (t)  : "))

satuanLuas    = "cm2"
satuaKeliling = "cm"
satuanVolume  = "cm3"

KB = 4 * (p + l + t)

LB = p * l

LPB = 2 * ((p * l) + (p * t) + (l * t))

# Volume balok
Volume = p * l * t

print("Keliling                : ", KB, satuaKeliling)
print("Luas alas               : ", LB, satuanLuas)
print("Luas permukaan balok    : ", LPB, satuanLuas)
print("Volume balok            :  %.2f" %Volume, satuanVolume)