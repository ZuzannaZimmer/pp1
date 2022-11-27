file=open('numbers.txt','r')
x=0
for line in file:
    z=int(line)
    suma=suma+z
print('suma: ',suma)
file.close()