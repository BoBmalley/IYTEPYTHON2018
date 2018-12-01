#A4
calisma=0
while calisma==0:
    girdi=input('İşlem giriniz(Çıkmak için Cikis yazınız):\n ')
    if '*' in girdi:
        girdi=girdi.split("*")
        sonuc=int(girdi[0])*int(girdi[1])
        print(sonuc)
    elif '/' in girdi:
        girdi=girdi.split("/")
        sonuc=int(girdi[0])/int(girdi[1])
        print(sonuc)
    elif '+' in girdi:
        girdi=girdi.split("+")
        sonuc=int(girdi[0])+int(girdi[1])
        print(sonuc)
    elif '-' in girdi:
        girdi=girdi.split("-")
        sonuc=int(girdi[0])-int(girdi[1])
        print(sonuc)
    elif 'Cikis' in girdi:
        break
    else:
        print("Sadece 4 işlem desteklenmektedir")
