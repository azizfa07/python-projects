def inputValidation(prompt_text):
    while True: 
        userInput = input(prompt_text)
        try:
            validValue = float(userInput)
            if validValue < 0:
                print("Gaji tidak boleh negatif.")
                continue
            return validValue
        except ValueError:
            print("Input salah, harap masukkan angka.")

def taxAccumulation(salary):
    taxBill = 0
 
    if salary <= 50000000:
       taxBill = salary * 0.05
    elif 50000000 < salary <= 150000000:
       taxBill = salary * 0.15
    elif 150000000 < salary <= 500000000:
       taxBill = salary * 0.25
    else: 
       taxBill = salary * 0.30
    
 
    print(f"\nGaji Anda: Rp {salary:,.0f}")
    print(f"Pajak yang harus dibayar: Rp {taxBill:,.0f}")

def main():
    print("=== Penentu Tagihan Pajak Penghasilan ===")
    salary = inputValidation("Masukkan besaran gaji anda (Rupiah): ")
    taxAccumulation(salary)

if __name__ == "__main__":
    main()