#A7
secenek=input("Bir secenek seciniz(1 numara ekleme,2 numara sorgusu)...")
if secenek==("1"):
	isim=input("İsim giriniz...")
	isim=isim.capitalize()
	isim=","+isim
	soyisim=input("Soyisim giriniz...")
	soyisim=soyisim.capitalize()
	numara=input("Numarasını giriniz...")
	numara=","+numara
	with open("C:/Users/PC/Desktop/rehber.txt", "a") as myfile:
		myfile.write(isim+" "+soyisim)
		myfile.write(numara)
	print("Rehbere kaydedilmiştir")
	rehber=open('C:/Users/PC/Desktop/rehber.txt','r')
	lines = rehber.read().split(',')
	print(lines)
elif secenek==("2"):
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
		print("Böyle biri rehberde yoktur...")
else:
	print("Ya 1 yada 2 giriniz...")
