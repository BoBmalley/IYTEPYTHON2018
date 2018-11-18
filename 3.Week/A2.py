#A2
kelime=raw_input("Bir kelime giriniz\n")
kelime=str.lower(kelime)
if kelime[::-1]==kelime:
    print(str.capitalize(kelime)+' '+"kelimesi palindromik bir kelimedir...")
else:
    print(str.capitalize(kelime)+' '+"kelimesi palindromik bir kelime degildir...")
