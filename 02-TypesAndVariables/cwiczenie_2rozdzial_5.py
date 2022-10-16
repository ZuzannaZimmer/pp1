najwieksza=None
najmniejsza=None
suma=0
ilosc=0
while True:
    zbior=input("Wprowadź liczbę: ")
    if zbior =='gotowe':
      break
    try:
      x=int(zbior)
    except:
        print("Nie wprowadzono liczby: ")
        continue
    ilosc=ilosc+1
    suma=suma+x
    for y in [zbior] :
       if najwieksza is None or y > najwieksza :
        najwieksza =  y 
    for z in [zbior] :
        if najmniejsza is None or z < najmniejsza :
            najmniejsza = z 
print(f'Łącznie wpisałeś {ilosc} liczb')
print(f'Suma wpisanych liczb wynosi:{suma}')               
print("najwieksza", najwieksza)
print("najmneijsza", najmniejsza)