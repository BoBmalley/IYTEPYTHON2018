#A4
yazi=open('C:/Users/PC/Desktop/text.txt','r')
string=yazi.read()
result = ''.join([i for i in string if not i.isdigit()])
file=open("C:/Users/PC/Desktop/text2.txt","w")
file=file.write(result)
print(result)

