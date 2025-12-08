print("Penentuan bilangan terbesar")
print("diantara 2 bilangan")
print("---------------------------")

bilanganX = int(input("Bilangan pertama         : "))
bilanganY = int(input("Bilangan kedua           : "))

bilanganTerbesar = bilanganX
if bilanganX < bilanganY :
    bilanganTerbesar = bilanganY
    
print("Bilangan terbesar adalah :", bilanganTerbesar)