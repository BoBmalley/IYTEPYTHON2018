import math
girdi = int(input('Bir sayı giriniz...\n'))
liste = []
baslangic = 2
if girdi >= 2 :
    while girdi != 1:
        while girdi % baslangic == 0:
            liste.append(baslangic)
            girdi = girdi / baslangic 
            if girdi == 1:
                break
        baslangic += 1       
    print (liste)
else:
    print('2 veya daha büyük sayı giriniz...')