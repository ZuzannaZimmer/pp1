suma=0
ilosc=0

while True:
    liczby = float(input("Wpisz liczbę: "))
    ilosc=ilosc+1
    suma= suma + liczby
    if liczby == 0:
        break
srednia=suma/ilosc
print(f'suma liczb:{suma}, ilość liczb: {ilosc}, średnia liczb:{round(srednia,2)}')