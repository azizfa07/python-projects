def inputValidation(choice):
    while True:
        userInput = input(choice)
        try:
            validValue = float(userInput)
            return validValue
        except ValueError:
            print("Input salah, harap masukkan angka.")

def bmiValidation(weight, tall):
    bmi = weight / (tall * tall)

    print(f"Skor BMI Anda: {bmi:.2f}")

    if bmi < 18.5:
       result = "kurus"
    elif 18.5 <= bmi < 25:
       result = "normal"
    elif 25 <= bmi < 30:
       result = "kelebihan berat badan"
    else:
       result = "kegemukan"

    print(f"Anda termasuk orang yang {result}")

def main():
        print("=== Penentu idealnya seseorang berdasarkan indeks BMI ===")
        weight = inputValidation("Masukkan berat badan anda (Kg) : ")
        tall = inputValidation("Masukkan tinggi badan anda (Meter, cth: 1.75) : ") 
        bmiValidation(weight, tall)

if __name__ == "__main__":
    main()