print("Penentuan dislkon")
print("-----------------")

besarPembelian = int(input("Nilai nominal pembelian : "))

if besarPembelian >= 200000 :
    diskon = 0.5 * besarPembelian
else :
    diskon = 0
    
besarPembayaran = besarPembelian - diskon

print()
print("Pembelian  :", besarPembelian)
print("Diskon     :", diskon)
print("Pembayaran :", besarPembayaran)
