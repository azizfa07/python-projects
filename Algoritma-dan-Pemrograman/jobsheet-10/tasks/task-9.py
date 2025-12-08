print("Penentuan skor mata pelajaran")
print("-----------------------------")

nilai = int(input("Nilai (0 s/d 100) : "))

if nilai <= 0 or nilai > 100 : 
    print("Nilai tidak valid")
elif nilai >= 90 :
    print("Skor A")
elif nilai >= 80 :
    print("Skor B")
elif nilai >= 70 :
    print("Skor C")
elif nilai >= 60:
    print("Skor D")
else :
    print("Skor E")