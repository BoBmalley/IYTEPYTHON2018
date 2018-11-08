#A6
rehber=open('C:/Users/PC/Desktop/rehber.txt','r+')
with open('rehber.txt') as f:
  d = dict(x.rstrip().split(None, 1) for x in f)
isim=input('Bir isim giriniz')
isim=isim.capitalize()
soyisim=input('Bir soyisim giriniz')
soyisim=soyisim.capitalize()
kisi=isim+' '+soyisim
if kisi in open ('rehber.txt').read():
        print(rehber.get('kisi'))
