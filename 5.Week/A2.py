#A2
def alan( x1,x2,y1,y2):
    import math
    area=(math.sqrt((x1-x2)**2))*(math.sqrt((y1-y2)**2))
    return area
x1=int(raw_input('X1\n'))
y1=int(raw_input('Y1\n'))
x2=int(raw_input('X2\n'))
y2=int(raw_input('Y2\n'))
alani=alan(x1,x2,y1,y2)
print('Istediginiz alan:')
print(alani)

