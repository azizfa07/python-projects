print("--- Simulasi Tegangan Tetap, Resistor Berubah ---")

V = float(input("Masukkan Tegangan Sumber (V): "))

print(f"\n[Info] Tegangan dikunci pada {V} Volt.")
print("Silakan masukkan nilai-nilai R secara berulang.")
print("Tekan ENTER saja (kosong) pada input R untuk BERHENTI.\n")

while True:
    raw_R = input(f"Masukkan Hambatan (R) untuk V={V}: ")

    if raw_R == "":
        print("Selesai. Terimakasih!")
        break

    try:
        R = float(raw_R)
        
        if R == 0:
            print("  Warning: Hambatan 0 menyebabkan korsleting (Infinite Current)!\n")
        else:
            Iseri = V / R
            print("  -> Arus yang mengalir: %.2f Ampere" % Iseri)
            print("-" * 20) 

    except ValueError:
        print("  Error: Masukkan angka yang valid!\n")