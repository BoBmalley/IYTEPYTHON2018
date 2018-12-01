#A3
def kontrol( a1x,a1y,b1x,b1y,c1x,c1y,d1x,d1y,a2x,a2y,b2x,b2y,c2x,c2y,d2x,d2y ):
    Kont=False    
    if a1x < a2x:
        if a1y > a2y:
            if b1x > b2x:
                if b1y > b2y:
                    if c1x > c2x:
                        if c1y < c2y:
                            if d1x < d2x:
                                if d1y < d2y:
                                    Kont=True
    return Kont

print('Koordinatlari arasina nokta koyarak giriniz(Ornek 3.4):')

a1=raw_input('BUYUK dikdortgenin SOL UST kosesinin koordinatlarini giriniz:\n')
a1=a1.split('.')
a1x=a1[0]
a1y=a1[1]

b1=raw_input('BUYUK dikdortgenin SAG UST kosesinin koordinatlarini giriniz:\n')
b1=b1.split('.')
b1x=b1[0]
b1y=b1[1]

c1=raw_input('BUYUK dikdortgenin SAG ALT kosesinin koordinatlarini giriniz:\n')
c1=c1.split('.')
c1x=c1[0]
c1y=c1[1]

d1=raw_input('BUYUK dikdortgenin SOL ALT kosesinin koordinatlarini giriniz:\n')
d1=d1.split('.')
d1x=d1[0]
d1y=d1[1]

a2=raw_input('KUCUK dikdortgenin SOL UST kosesinin koordinatlarini giriniz:\n')
a2=a2.split('.')
a2x=a2[0]
a2y=a2[1]

b2=raw_input('KUCUK dikdortgenin SAG UST kosesinin koordinatlarini giriniz:\n')
b2=b2.split('.')
b2x=b2[0]
b2y=b2[1]

c2=raw_input('KUCUK dikdortgenin SAG ALT kosesinin koordinatlarini giriniz:\n')
c2=c2.split('.')
c2x=c2[0]
c2y=c2[1]

d2=raw_input('KUCUK dikdortgenin SOL ALT kosesinin koordinatlarini giriniz:\n')
d2=d2.split('.')
d2x=d2[0]
d2y=d2[1]

durum=kontrol(a1x,a1y,b1x,b1y,c1x,c1y,d1x,d1y,a2x,a2y,b2x,b2y,c2x,c2y,d2x,d2y)
if True:
    print('Icinde')
else:
    print('Disinda')	
