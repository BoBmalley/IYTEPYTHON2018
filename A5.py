#A5
import math
girdi=int(input('Bir sayı giriniz...\n'))
while girdi % 2 == 0:
    print ('2',)
    girdi = girdi / 2
   
    for sayi in range (3,int(math.sqrt(girdi))+1,2):
        while girdi % sayi == 0:
            print (sayi,)
            girdi = girdi / sayi
        if girdi > 2 :
            print(girdi)