import re

f=open("grades.txt",'r')
oceny=f.read()
oc="\d.\d"
lista = re.findall(oc,oceny)
suma=0.0
for i in lista:
    suma=suma+float(i)
print((round(suma/len(lista),2)))