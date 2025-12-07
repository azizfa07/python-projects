import math 

print("--- Program Menghitung Limas Segitiga Sama Sisi ---")
s = float(input("Masukkan panjang sisi alas (s) : "))
t = float(input("Masukkan tinggi limas (t)      : "))

satuanLuas    = "cm2"
satuaKeliling = "cm"
satuanVolume  = "cm3"

LA = (s**2 * math.sqrt(3)) / 4

Volume = (1/3) * LA * t

jarak_pusat_ke_sisi = (s * math.sqrt(3)) / 6
t_segitiga_tegak = math.sqrt(t**2 + jarak_pusat_ke_sisi**2)

Luas_Sisi_Tegak = 3 * (0.5 * s * t_segitiga_tegak)
\
L_Permukaan = LA + Luas_Sisi_Tegak
\
rusuk_alas = 3 * s

jarak_pusat_ke_sudut = (s * math.sqrt(3)) / 3
panjang_rusuk_tegak = math.sqrt(t**2 + jarak_pusat_ke_sudut**2)

Total_Rusuk = rusuk_alas + (3 * panjang_rusuk_tegak)

print("-" * 30)
print("Luas alas (segitiga)    :  %.2f" %LA, satuanLuas)
print("Luas selimut (3 sisi)   :  %.2f" %Luas_Sisi_Tegak, satuanLuas)
print("Luas permukaan total    :  %.2f" %L_Permukaan, satuanLuas)
print("Total panjang rusuk     :  %.2f" %Total_Rusuk, satuaKeliling)
print("Volume limas            :  %.2f" %Volume, satuanVolume)