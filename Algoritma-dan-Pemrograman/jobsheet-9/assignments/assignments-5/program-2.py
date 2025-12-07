print("=== PROGRAM KASIR SEDERHANA ===")
print("Ketik nama barang, lalu harganya.")
print("Tekan ENTER kosong pada 'Nama Barang' untuk selesai belanja.\n")

daftar_barang = []  
total_harga = 0     

while True:
    nama = input("Nama Barang : ")

    if nama == "":
        break
    
    try:
        harga = float(input(f"Harga {nama} : Rp "))
        
        daftar_barang.append([nama, harga])
        
        total_harga = total_harga + harga
        print("--> Barang ditambahkan!\n")
        
    except ValueError:
        print("Error: Harga harus berupa angka!\n")

print("\n" + "="*30)
print("STRUK BELANJA ANDA")
print("="*30)

for barang in daftar_barang:
    print(f"- {barang[0]} \t: Rp {barang[1]:,.0f}")

print("-" * 30)
print(f"TOTAL BAYAR \t: Rp {total_harga:,.0f}")
print("="*30)