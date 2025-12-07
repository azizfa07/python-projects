# Tabung

phi = 3.14
r   = float(input("Masukkan r : "))
t   = float(input("Masukkan t : "))

satuanLuas    = "cm2"
satuaKeliling = "cm"
satuanVolume  = "cm3"

KAL = 2 * phi * r

LAL = phi * r * r

LST = 2 * phi * r * t

LPA = 2 * phi * r * (r * t)

# Volume tabung
Volume = phi * r * r * t

print("Keliling alas lingkaran : ", KAL, satuaKeliling)
print("Luas alas lingkaran     : ", LAL, satuanLuas)
print("Luas selimut tabung     : ", LST, satuanLuas)
print("Luas permukaan alas     : ", LPA, satuanLuas)
print("Volume tabung           :  %.2f" %Volume, satuanVolume)