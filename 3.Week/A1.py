#A1
yil=raw_input('Bir yil giriniz...')
test=str.isdigit(yil)
if str.isdigit(yil):
		yil=int(yil)
		if yil < 400:
			   if yil % 4 == 0:
					   print('Bu yil ARTIK yildir...')
			   else:
					   print('Bu yil NORMAL yildir...')
		elif yil < 4000:
			if yil % 4 == 0:
					print('Bu yil ARTIK yildir...')
			elif yil % 400 == 0:
					print('Bu yil ARTIK yildir...')
			else:
					print('Bu yil NORMAL yildir...')        
		else:
			if yil % 4 == 0:
					print('Bu yil ARTIK yildir...')					
			elif yil % 400 == 0:
					print('Bu yil ARTIK yildir...')					
			elif yil % 4000 == 0:
					print('Bu yil NORMAL yildir...')
			else:
					print('Bu yil ARTIK yildir...')
				
else:
		print('Sadece yil giriniz...')
