#A2
ilk_numara=input('Birinci sayıyı giriniz')
ikinci_numara=input('Ikinci sayıyı giriniz')
secenek=input('Seçeneği giriniz')
if ilk_numara.isdigit():
	if ikinci_numara.isdigit():
		if secenek.isdigit():
			ilk_numara=int(ilk_numara)
			ikinci_numara=int(ikinci_numara)
			secenek=int(secenek)
			if secenek==0:
				toplam=ilk_numara+ikinci_numara
				print('Toplamları=',toplam)
			elif secenek==1:
				if ilk_numara<ikinci_numara:
					fark=ikinci_numara-ilk_numara
					print('Farkları=',fark)
				else:
					fark=ilk_numara-ikinci_numara
					print('Farkları=',fark)
			elif secenek==2:
				carpim=ilk_numara*ikinci_numara
				print('Çarpımları=',carpim)
			elif secenek==3:
				if ilk_numara<ikinci_numara:
					bolum=ikinci_numara/ilk_numara
					print('Bölümleri=',bolum)
				else:
					bolum=ilk_numara/ikinci_numara
					print('Bölümleri=',bolum)
			else:
				print('Böyle bir seçecek yok!')
		else:
		 print('Girdiğiniz sayıları kontrol edin')		
	else:
		print('Girdiğiniz sayıları kontrol edin')	
else:
	print('Girdiğiniz sayıları kontrol edin')
