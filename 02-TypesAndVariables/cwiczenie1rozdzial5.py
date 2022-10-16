suma=0
ilosc=0
while True:
   line = input("Wprowadź liczbę:")
   if line == 'gotowe':
    break
   try:
     linee = int(line)
   except:
     print("Błąd:")
     continue
   ilosc=ilosc+1
   suma=suma+linee
   srednia=suma/ilosc
print(f'Łącznie wpisałeś {ilosc} liczb')
print(f'Suma wpisanych liczb wynosi:{suma}')
print(f'Średnia wpisanych liczb wynosi:{srednia}')  