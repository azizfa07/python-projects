print("Penentuan nama hari")
print(" 0 = Minggu       1 = Senin")
print(" 2 = Selasa       3 = Rabu")
print(" 4 = Kamis        5 = Jum'at")
print(" 6 = Sabtu")
print("---------------------------")

kodeHari = int(input("Masukkan kode hari :"))

if kodeHari == 0 :
    print("Minggu")
elif kodeHari == 1 :
    print("Senin")
elif kodeHari == 2 :
    print("Selasa")
elif kodeHari == 3 :
    print("Rabu")
elif kodeHari == 4 :
    print("Kamis")
elif kodeHari == 5 :
    print("Jum'at")
elif kodeHari == 6 :
    print("Sabtu")
else :
    print("Kode salah")