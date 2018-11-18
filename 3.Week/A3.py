#A3
kelime=raw_input('Bir kelime giriniz...')
kelime=str.lower(kelime)
if len(list(kelime)) == len(set(kelime)):
        print('Bu kelime bir isogramdir...')
else:
        print('Bu kelime bir isogram DEGILDIR...')
