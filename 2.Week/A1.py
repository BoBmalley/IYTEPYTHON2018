#A1
ilk_numara=input('Birinci numarayı giriniz')
ikinci_numara=input('Ikinci numarayı giriniz')
if ilk_numara.isdigit():
    if ikinci_numara.isdigit():
        ilk_numara=int(ilk_numara)
        ikinci_numara=int(ikinci_numara)
        toplam=ilk_numara+ikinci_numara
        print(toplam)

    else:
        print('HATA=Sadece rakam girebilirsiniz.')
else:
    print('HATA=Sadece rakam girebilirsiniz.')
    
