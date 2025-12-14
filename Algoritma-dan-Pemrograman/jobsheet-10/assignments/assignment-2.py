print("Penentu bilangan terbesar hingga terkecil")
print("-----------------------------------------")

bilangan1 = int(input("Masukkan bilangan pertama : "))
bilangan2 = int(input("Masukkan bilangan kedua   : "))
bilangan3 = int(input("Masukkan bilangan ketiga  : "))

if bilangan1 > bilangan2 > bilangan3 :
    print("Urutan bilangannya dari terbesar : ", bilangan1, bilangan2, bilangan3)
if bilangan1 > bilangan3 > bilangan2 :
    print("Urutan bilangannya dari terbesar : ", bilangan1, bilangan3, bilangan2)
elif bilangan3 > bilangan1 > bilangan2 :
    print("Urutan bilangannya dari terbesar : ", bilangan3, bilangan1, bilangan2)
elif bilangan3 > bilangan2 > bilangan1 :
    print("Urutan bilangannya dari terbesar : ", bilangan3, bilangan2, bilangan1)
elif bilangan2 > bilangan1 > bilangan3 :
    print("Urutan bilangannya dari terbesar : ", bilangan2, bilangan1, bilangan3)
elif bilangan2 > bilangan3 > bilangan1 :
    print("Urutan bilangannya dari terbesar hingga terkecil : ", bilangan2, bilangan3, bilangan1)
else :
    print("bilangan sama semua")