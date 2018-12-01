#A1
def uzunluk( x1,y1,z1,x2,y2,z2 ):
    import math
    ilk=(x1-x2)**2
    ikinci=(y1-y2)**2
    ucuncu=(z1-z2)**2
    toplam=ilk+ikinci+ucuncu
    arasi=float(math.sqrt(toplam))
    return arasi
x1=int(raw_input('X1\n'))
y1=int(raw_input('Y1\n'))
z1=int(raw_input('Z1\n'))
x2=int(raw_input('X2\n'))
y2=int(raw_input('Y2\n'))
z2=int(raw_input('Z2\n'))
uzun=uzunluk(x1,y1,z1,x2,y2,z2)
print('Iki nokta arasi uzunluk:')
print(uzun)

