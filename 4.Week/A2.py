text_1=input('Bir yazı giriniz...')
text_2=input('Kontrol edilecek yazı giriniz...')
text_1=str.lower(text_1)
text_2=str.lower(text_2)
if text_2 in text_1:
    print('İkinci yazdığınız ilk yazdığınızda GEÇİYOR...')
else:
    print('İkinci yazdığınız ilk yazdığınızda GEÇMİYOR...')