
for a in range(5):
    sayi = int(input("Sayı {fa+1}'i girin"))
    

    if sayi > 3:
        for i in range(3,sayi):
            t = False
            if (sayi % i) == 0:
                print(sayi," asal sayı değildir")
                t = True
                break
        if t == False:
            print(sayi," asal sayıdır")
    else: 
        print(sayi," asal sayı değildir")
   f