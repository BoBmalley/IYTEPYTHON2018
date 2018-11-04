#A8
text_1 = "Bu cümlede 4 elma 5 armut 8 tane de muz var"
text_2 = 'bu ikinci cümlede 9 kiraz 3 karpuz var'
text_1=text_1.split(' ')
text_2=text_2.split(' ')
sayi_1=text_1[2]+text_1[4]+text_1[6]
sayi_2=text_2[3]+text_2[5]
sayi_1=int(sayi_1)
sayi_2=int(sayi_2)
print(sayi_1+sayi_2)
