najwieksza=None
najmniejsza=None
while True:
    zbior=input("Wprowadź liczbę: ")
    if zbior =='gotowe':
      break
    try:
      x=int(zbior)
    except:
        print("Nie wprowadzono liczby: ")
        continue
    for y in [zbior] :
       if najwieksza is None or y > najwieksza :
        najwieksza =  y 
    for z in [zbior] :
        if najmniejsza is None or z < najmniejsza :
            najmniejsza = z    
print("najwieksza", najwieksza)
print("najmneijsza", najmniejsza)