#A6
rehber=open('C:/Users/PC/Desktop/rehber.txt','r')
lines = rehber.read().split(',')
isim=input('Bir isim giriniz...')
isim=isim.capitalize()
soyisim=input('Bir soyisim giriniz...')
soyisim=soyisim.capitalize()
kisi=isim+' '+soyisim
if kisi in lines:
        numarası=lines.index(kisi)+1
        print(kisi+" adlı kişinin numarası="+lines[numarası])
else:
        print("Böyle bir kişi rehberde yoktur...")
